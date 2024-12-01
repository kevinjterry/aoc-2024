# Day 1
def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    left_list = []
    right_list = []

    for line in lines:
        left, right = line.split("   ")
        left_list.append(int(left))
        right_list.append(int(right))

    return left_list, right_list


def calculate_difference(left_list, right_list):
    left_sorted = sorted(left_list)
    right_sorted = sorted(right_list)

    diff_list = [abs(left_sorted[i] - right_sorted[i]) for i in range(len(left_sorted))]
    return sum(diff_list)


def calculate_similarity(left_list, right_list):
    count = 0
    sim_list = []
    for i in range(len(left_list)):
        for j in range(len(right_list)):
            if left_list[i] == right_list[j]:
                count += 1
        sim_list.append(count * left_list[i])
        count = 0

    return sum(sim_list)


def main():
    left_list, right_list = load_data("./Day 1/input.txt")
    result = calculate_difference(left_list, right_list)
    print(f"Difference: {result}")
    sim = calculate_similarity(left_list, right_list)
    print(f"Similarity: {sim}")


if __name__ == "__main__":
    main()
