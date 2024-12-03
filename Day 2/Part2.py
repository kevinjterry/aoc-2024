# Day 2
def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    unsafe_list = []
    safe_list = []

    for line in lines:
        is_safe = test_if_safe(line)
        if is_safe:
            safe_list.append(line)
        else:
            unsafe_list.append(line)

    print(f"Safe: {len(safe_list)}")
    print(f"Not Safe: {len(unsafe_list)}")

    return safe_list, unsafe_list


def test_if_safe(line):
    numbers = [int(x) for x in line.split()]

    if is_valid_sequence(numbers):
        return True

    for i in range(len(numbers)):
        test_numbers = numbers[:i] + numbers[i + 1 :]
        if is_valid_sequence(test_numbers):
            return True

    return False


def is_valid_sequence(numbers):
    ascending = all(numbers[i] < numbers[i + 1] for i in range(len(numbers) - 1))
    descending = all(numbers[i] > numbers[i + 1] for i in range(len(numbers) - 1))

    if not (ascending or descending):
        return False

    for i in range(1, len(numbers)):
        if abs(numbers[i] - numbers[i - 1]) > 3:
            return False

    return True


def main():
    _ = load_data("./Day 2/input.txt")


if __name__ == "__main__":
    raise SystemExit(main())
