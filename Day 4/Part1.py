def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def transpose_lines(lines):
    max_length = max(len(line) for line in lines)
    normalized_lines = [line.ljust(max_length) for line in lines]

    transposed = zip(*normalized_lines)
    vertical_lines = ["".join(chars).rstrip() for chars in transposed]

    return vertical_lines


def find_horizontal_xmas(lines):
    num_xmas = 0
    for line in lines:
        num_xmas += line.count("XMAS")
    for line in lines:
        num_xmas += line.count("SAMX")

    return num_xmas


def find_vertical_xmas(lines):
    num_xmas = 0
    lines_vertical = transpose_lines(lines)

    for line in lines_vertical:
        num_xmas += line.count("XMAS")

    for line in lines_vertical:
        num_xmas += line.count("SAMX")

    return num_xmas


def shift_right(lines):
    shifted_lines = []
    line_len = len(lines[0])

    for idx, line in enumerate(lines):
        line = line + "O" * (line_len - idx)
        line = "O" * idx + line
        shifted_lines.append(line)

    return shifted_lines


def shift_left(lines):
    shifted_lines = []
    line_len = len(lines[0])

    for idx, line in enumerate(lines):
        line = "O" * (line_len - idx) + line
        line = line + "O" * idx
        shifted_lines.append(line)

    return shifted_lines


def main():
    lines = load_data("./Day 4/input.txt")

    horizontal = find_horizontal_xmas(lines)
    vertical = find_vertical_xmas(lines)
    diag_left = find_vertical_xmas(shift_right(lines))
    diag_right = find_vertical_xmas(shift_left(lines))

    sum = horizontal + vertical + diag_right + diag_left

    print(f"Number of 'XMAS' in word search: {sum}")


if __name__ == "__main__":
    raise SystemExit(main())
