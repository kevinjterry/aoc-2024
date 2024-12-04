import re


def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def split_into_chunks(lines):
    lines = "\n".join(lines)

    chunk = []
    do_lines = lines.split("do()")
    for line in do_lines:
        dont_lines = line.split("don't()")
        if len(dont_lines) > 0:
            chunk.append(dont_lines[0])

    return chunk


def get_product_sum(chunk):
    pattern = r"mul\(\d+,\d+\)"
    matches = re.findall(pattern, "\n".join(chunk))

    sums = []
    for match in matches:
        match = match[4:-1]
        left, right = match.split(",")
        product = int(left) * int(right)
        sums.append(product)

    return sum(sums)


def main():
    lines = load_data("./Day 3/input.txt")

    # split into chunks of do() and don't()
    chunk = split_into_chunks(lines)

    # print the sum of the products
    print(get_product_sum(chunk))


if __name__ == "__main__":
    raise SystemExit(main())
