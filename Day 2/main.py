# Day 1
def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    safe_list = [line for line in lines if test_if_safe(line)]
    unsafe_list = [line for line in lines if not test_if_safe(line)]

    print(f"Safe: {len(safe_list)}")
    print(f"Unsafe: {len(unsafe_list)}")

    return safe_list, unsafe_list


def test_if_safe(line):
    numbers = [int(x) for x in line.split()]
    ascending = sorted(numbers)
    descending = sorted(numbers, reverse=True)

    if numbers == ascending or numbers == descending:
        for i in range(1, len(numbers)):
            if abs(numbers[i] - numbers[i - 1]) > 3:
                return False

        if len(numbers) != len(set(numbers)):
            return False

        return True

    return False


def main():
    _ = load_data("./Day 2/input.txt")


if __name__ == "__main__":
    raise SystemExit(main())
