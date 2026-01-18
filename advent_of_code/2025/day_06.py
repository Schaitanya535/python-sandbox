from utils.file_reader import parse_to_grid, read_columns, read_lines


def get_grand_total(grid: list[list[str]]):
    grand_total = 0
    ops = grid[-1]
    rows = len(grid)
    cols = len(ops)

    for col in range(0, cols):
        op = ops[col]
        total = 1 if op == "*" else 0
        for row in range(0, rows - 1):
            if op == "*":
                total *= int(grid[row][col])
            else:
                total += int(grid[row][col])
        grand_total += total

    return grand_total


def get_grand_total_reading_columns(grid: list[list[str]]):
    grand_total = 0
    for line in grid:
        op = line[-1]
        total = 1 if op == "*" else 0
        for val in line[:-1]:
            if op == "*":
                total *= int(val)
            else:
                total += int(val)
        grand_total += total

    return grand_total


def main():
    input_path = "advent_of_code/2025/inputs/day_06_test.txt"
    lines = read_lines(input_path)
    grid = [parse_to_grid(line) for line in lines]
    col_grid = read_columns(input_path, " ")
    print(col_grid)

    print("Part 1 (): ", get_grand_total(grid))
    print("Part 1 (columns): ", get_grand_total_reading_columns(col_grid))
    print("Part 2 ():")


if __name__ == "__main__":
    main()
