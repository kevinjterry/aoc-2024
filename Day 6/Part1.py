def load_data(filename):
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]
    return lines

def create_grid(lines):
    grid = []
    for line in lines:
        grid.append(list(line))
    return grid

def find_caret(grid):
    dir = None
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "^" or grid[i][j] == ">" or grid[i][j] == "<" or grid[i][j] == "v":
                if grid[i][j] == "^":
                    dir = "up"
                elif grid[i][j] == ">":
                    dir = "right"
                elif grid[i][j] == "<":
                    dir = "left"
                elif grid[i][j] == "v":
                    dir = "down"
                return dir, j, i
    return None, None, None

def is_in_bounds(i, j, grid_width, grid_height):
    if i < 0 or i >= grid_width or j < 0 or j >= grid_height:
        return False
    return True

def change_direction(dir):
    if not dir:
        return None
    directions = {
        "up": "right",
        "right": "down",
        "down": "left",
        "left": "up"
    }
    return directions.get(dir, None)

def main():
    lines = load_data("./Day 6/input_test.txt")
    reversed_lines = lines[::-1]

    grid = create_grid(lines)
    grid_width = len(grid[0])
    grid_height = len(grid)

    for line in grid:
        print(line)

    # get initial caret position and direction
    dir, i, j = find_caret(grid)
    print(f"Caret at ({i}, {j}) going {dir}")
    caret_position = (i, j)
    caret_direction = dir

    on_screen = is_in_bounds(caret_position[0], caret_position[1], grid_width, grid_height)
    print(f"On screen: {on_screen}")

    while on_screen:
        # check if caret is still on screen
        on_screen = is_in_bounds(caret_position[0], caret_position[1], grid_width, grid_height)

        if dir == "up" and on_screen:
            grid[caret_position[1]][caret_position[0]] = "^"

            # check fr '#'
            print(f"Next char: {grid[caret_position[1]][caret_position[0] - 1]}")
            if grid[caret_position[1]][caret_position[0] - 1] == "#":
                print(f"Hit wall at ({caret_position[0] - 1}, {caret_position[1]})")
                break
            
            # move caret up
            caret_position = (caret_position[0], caret_position[1] - 1)
            print(f"Move caret to ({caret_position[0]}, {caret_position[1]})")
    
    for line in grid:
        print(line)
            
            


if __name__ == "__main__":
    raise SystemExit(main())
