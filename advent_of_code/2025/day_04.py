from utils.directions import DIRECTIONS_8
from utils.file_reader import read_grid


def can_remove_roll(rolls_grid: list[list[str]], row: int, col: int):
    adjacent_roll_count = 0
    rows = len(rolls_grid)
    cols = len(rolls_grid[0]) if rows > 0 else 0

    # Check all 8 adjacent positions
    for dr, dc in DIRECTIONS_8:
        new_row = row + dr
        new_col = col + dc

        # Check if position is within grid bounds
        if 0 <= new_row < rows and 0 <= new_col < cols:
            if rolls_grid[new_row][new_col] == "@":
                adjacent_roll_count += 1

    # Return False if 4 or more adjacent rolls (not accessible)
    # Return True if less than 4 adjacent rolls (accessible)
    return adjacent_roll_count < 4


def count_accessable_rolls_after_removing(rolls_grid: list[list[str]]):
    total_count = 0
    while True:
        count = 0
        for row_idx, row in enumerate(rolls_grid):
            for item_idx, item in enumerate(row):
                if item == "@" and can_remove_roll(rolls_grid, row_idx, item_idx):
                    count += 1
                    rolls_grid[row_idx][item_idx] = "."
        total_count += count
        if count == 0:
            break
    return total_count


def count_accessable_rolls(rolls_grid: list[list[str]]):
    count = 0
    for row_idx, row in enumerate(rolls_grid):
        for item_idx, item in enumerate(row):
            if item == "@" and can_remove_roll(rolls_grid, row_idx, item_idx):
                count += 1
    return count


def main():
    rolls_grid = read_grid(
        "/Users/chaitanyasura/Projects/python-sandbox/advent_of_code/2025/inputs/day_04.txt",
    )
    print(
        "Part 1 (no. of accessable papers):",
        count_accessable_rolls(rolls_grid),
    )
    print(
        "Part 2 (no. of accessable papers after removing):",
        count_accessable_rolls_after_removing(rolls_grid),
    )


if __name__ == "__main__":
    main()
