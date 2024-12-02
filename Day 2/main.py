# Day 1
def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    not_safe_list = []
    safe_list = []

    for line in lines:
        is_safe = test_if_safe(line)
        if is_safe:
            # print(f"Line {line} YES")
            safe_list.append(line)
        else:
            print(f"Line {line} NO")
            not_safe_list.append(line)

    print(f"Safe: {len(safe_list)}")
    print(f"Not Safe: {len(not_safe_list)}")

    return safe_list, not_safe_list


def test_if_safe(line):
    line = line.split(" ")

    # check if there are any duplicates
    if len(line) != len(set(line)):
        # print(f"Line {line} has duplicates")
        return False

    # check if ascending or descending
    if line == sorted(line) or line == sorted(line, reverse=True):

        # if any numbers have a difference of more than 2
        for i in range(1, len(line)):
            if abs(int(line[i]) - int(line[i - 1])) > 4:
                print(f"Line {line} has a difference of more than 4")
                return False

        return True

    # print(f"Line {line} is not in order")
    return False


def main():
    _ = load_data("./Day 2/input.txt")


if __name__ == "__main__":
    main()
