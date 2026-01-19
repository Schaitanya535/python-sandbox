from collections import deque

from utils.file_reader import read_grid


def get_number_of_timelines(grid: list[list[str]]):
    # Use memoization: memo[x,y] = number of paths from (x,y) to the bottom
    memo: dict[tuple[int, int], int] = {}

    def count_paths(x: int, y: int) -> int:
        # Base case: out of bounds means we've completed a path
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            return 1

        # Check memo
        if (x, y) in memo:
            return memo[(x, y)]

        # Calculate paths from this position
        if grid[y][x] == "^":
            # Split: count paths going left + paths going right
            result = count_paths(x - 1, y) + count_paths(x + 1, y)
        else:
            # Continue down
            result = count_paths(x, y + 1)

        memo[(x, y)] = result
        return result

    start_x = grid[0].index("S")
    return count_paths(start_x, 0)


def find_beam_starting(line: list[str]):
    return line.index("S")


def get_number_of_splits(grid: list[list[str]]):
    q: deque[tuple[int, int]] = deque()
    q.append((grid[0].index("S"), 0))

    split_set: set[tuple[int, int]] = set()
    visited: set[tuple[int, int]] = set()

    while len(q):
        x, y = q.popleft()

        # Check bounds - CORRECTED
        if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
            continue

        # Skip if already visited
        if (x, y) in visited:
            continue
        visited.add((x, y))

        if grid[y][x] == "^":
            split_set.add((x, y))
            q.append((x - 1, y))
            q.append((x + 1, y))
        else:
            q.append((x, y + 1))
    return len(split_set)


def main():
    input_path = "advent_of_code/2025/inputs/day_07.txt"
    grid = read_grid(input_path)
    print("Part 1 (Get Number of times beam is split): ", get_number_of_splits(grid))
    print("Part 2 (Get number of pahts (timelines)):", get_number_of_timelines(grid))


if __name__ == "__main__":
    main()
