from utils.file_reader import read_range_input


def is_doubled_pattern(num: int) -> bool:
    num_str = str(num)
    length_num = len(num_str)

    # Only check if the number can be split into two equal halves
    if length_num % 2 == 0:
        half_length = length_num // 2
        first_half = num_str[:half_length]
        second_half = num_str[half_length:]

        return first_half == second_half

    return False


def has_repeating_pattern(num: int) -> bool:
    num_str = str(num)
    length_num = len(num_str)

    # Check all possible pattern lengths (from 1 to half the string length)
    for pattern_length in range(1, length_num // 2 + 1):
        # Only check if the pattern length divides evenly into the total length
        if length_num % pattern_length == 0:
            pattern = num_str[:pattern_length]
            repetitions = length_num // pattern_length

            # Check if repeating the pattern at least twice creates the original string
            if repetitions >= 2 and pattern * repetitions == num_str:
                return True

    return False


def get_invalid_sum(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for val in range(start, end + 1):
            if is_doubled_pattern(val):
                total += val

    return total


def get_invalid_sum_part2(ranges: list[tuple[int, int]]) -> int:
    total = 0
    for start, end in ranges:
        for val in range(start, end + 1):
            if has_repeating_pattern(val):
                total += val

    return total


def main():
    ranges = read_range_input(
        "advent_of_code/2025/inputs/day_02.txt",
        True,
    )
    print("Part 1 (doubled pattern):", get_invalid_sum(ranges))
    print("Part 2 (repeated at least twice):", get_invalid_sum_part2(ranges))


if __name__ == "__main__":
    main()
