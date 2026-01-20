from utils.file_reader import read_lines


def count_zero_crossings(position, instructions):
    count = 0
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == "L":
            # Moving left (decreasing): count how many times we pass through 0
            # From position P, moving left by A steps
            # We hit 0 after P steps, then every 100 steps after that
            # Total times we pass 0: (P + A) // 100, but only if A > 0
            if amount > 0:
                count += (position + amount) // 100
            position = (position - amount) % 100
        else:
            # Moving right (increasing): count how many times we pass through 0
            # From position P, moving right by A steps
            # We hit 0 after (100 - P) steps, then every 100 steps
            # Total times: (P + A) // 100
            count += (position + amount) // 100
            position = (position + amount) % 100
    return count


def count_zero_hits(start_position: int, instructions: list[str]) -> int:
    position = start_position
    count = 0
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == "L":
            position = (position - amount) % 100
        else:
            position = (position + amount) % 100

        if position == 0:
            count += 1

    return count


def main():
    # Test input first
    test_lines = read_lines("advent_of_code/2025/inputs/day_01_test.txt")
    print("Test - Zero hits:", count_zero_hits(50, test_lines))
    print("Test - Zero crossings:", count_zero_crossings(50, test_lines))
    print()

    # Actual input
    lines = read_lines("advent_of_code/2025/inputs/day_01.txt")
    print("Actual - Zero hits:", count_zero_hits(50, lines))
    print("Actual - Zero crossings:", count_zero_crossings(50, lines))


if __name__ == "__main__":
    main()
