def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines


def count_xmas(lines):
    rows = len(lines)
    cols = len(lines[0]) if rows > 0 else 0
    num_xs = 0

    for i in range(rows):
        for j in range(cols):
            # Check if the current cell contains 'A'
            if lines[i][j].upper() == "A":
                nw_se_found = False
                ne_sw_found = False

                # Check for diag-left and diag-right MAS
                if (i - 1 >= 0 and j - 1 >= 0) and (i + 1 < rows and j + 1 < cols):
                    c1 = lines[i - 1][j - 1].upper()
                    c2 = lines[i + 1][j + 1].upper()

                    # Check for 'M-A-S' or 'S-A-M'
                    if (c1 == "M" and c2 == "S") or (c1 == "S" and c2 == "M"):
                        nw_se_found = True

                # Check for diag-right and diag-left MAS
                if (i - 1 >= 0 and j + 1 < cols) and (i + 1 < rows and j - 1 >= 0):
                    c1 = lines[i - 1][j + 1].upper()
                    c2 = lines[i + 1][j - 1].upper()

                    # Check for 'M-A-S' or 'S-A-M'
                    if (c1 == "M" and c2 == "S") or (c1 == "S" and c2 == "M"):
                        ne_sw_found = True

                if nw_se_found and ne_sw_found:
                    num_xs += 1

    return num_xs


def main():
    lines = load_data("./Day 4/input.txt")

    xmas_count = count_xmas(lines)
    print(f"Number of X-MAS patterns: {xmas_count}")


if __name__ == "__main__":
    raise SystemExit(main())
