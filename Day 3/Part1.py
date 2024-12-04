import re

def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def main():
    lines = load_data("./Day 3/input.txt")

    pattern = r'mul\(\d+,\d+\)'
    matches = re.findall(pattern, '\n'.join(lines))

    sums = []
    for match in matches:
        match = match[4:-1]
        left, right = match.split(',')
        product = int(left) * int(right)
        sums.append(product)

    print(sum(sums))

if __name__ == "__main__":
    raise SystemExit(main())