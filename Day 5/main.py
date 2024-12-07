def load_data(filename):
    with open(filename, "r") as f:
        rules = []
        update = []
        lines = [line.strip() for line in f.readlines()]

    for line in lines:
        if "|" in line:
            rules.append(line.split("|"))
        else:
            if line == "":
                continue

            update.append(line)

    return rules, update


def create_rule_set(rules):
    rule_left = []
    rule_right = []
    for rule in rules:
        # get rid  of the pipes
        rule_left.append(rule[0].strip())
        rule_right.append(rule[1].strip())

    combined = rule_left + rule_right

    return rule_left, rule_right, combined


def remove_duplicates(combined):
    seen = set()
    return [x for x in combined if x not in seen and not seen.add(x)]


def find_index(list, num):
    if num not in list:
        return -1
    return list.index(num)


def sort_update(update_list, rule_right, rule_left):
    sorted_list = []
    pending = update_list.copy()

    while pending:
        added = False
        for num in pending[:]:
            if num not in rule_right:
                sorted_list.append(num)
                pending.remove(num)
                added = True
            else:
                indices = [i for i, x in enumerate(rule_right) if x == num]
                can_add = True
                max_pos = -1

                for index in indices:
                    dependent_num = rule_left[index]
                    if dependent_num in pending:
                        can_add = False
                        break
                    if dependent_num in sorted_list:
                        max_pos = max(max_pos, sorted_list.index(dependent_num))

                if can_add:
                    if max_pos >= 0:
                        sorted_list.insert(max_pos + 1, num)
                    else:
                        sorted_list.append(num)
                    pending.remove(num)
                    added = True

        if not added and pending:
            sorted_list.extend(pending)
            break

    return sorted_list


def main():
    rules, update = load_data("./Day 5/input.txt")
    rule_left, rule_right, combined = create_rule_set(rules)

    rule_right = [int(num) for num in rule_right]
    rule_left = [int(num) for num in rule_left]

    update_list = []
    middle_vals = []
    fixed_middle_vals = []

    for line in update:
        for num in line.split(","):
            update_list.append(int(num))

        sorted_update = sort_update(update_list, rule_right, rule_left)
        middle_index = len(sorted_update) // 2

        if sorted_update == update_list:
            middle_vals.append(sorted_update[middle_index])
        else:
            fixed_middle_vals.append(sorted_update[middle_index])

        update_list = []

    print(f"Middle sum: {sum(middle_vals)}")
    print(f"Fixed middle sum: {sum(fixed_middle_vals)}")


if __name__ == "__main__":
    raise SystemExit(main())
