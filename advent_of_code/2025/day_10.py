from utils.file_reader import read_lines


def get_min_no_switch_flip(row: tuple[int, list[int], list[int]]) -> int:
    pattern, ops, _zoltage = row

    def get_min_flips(curr_pat: int, index: int, curr_flips: int) -> int:
        # Check if current pattern matches ANY of the target switches
        if index >= len(ops):
            return len(ops) + 1

        if curr_pat == ops[index]:
            return curr_flips

            # Try not flipping this switch
        no_flip = get_min_flips(curr_pat, index + 1, curr_flips)

        # Try flipping this switch
        flip = get_min_flips(curr_pat ^ ops[index], index + 1, curr_flips + 1)

        return min(no_flip, flip)

    return get_min_flips(pattern, 0, 0) + 1


def get_sum_of_min_switch_flips(rows: list[tuple[int, list[int], list[int]]]):
    return sum(get_min_no_switch_flip(row) for row in rows)


def parse_line_to_bin_numbers(line: str) -> tuple[int, list[int], list[int]]:
    line_split = line.split(" ")
    pattern = line_split[0]
    pattern_num = sum(1 << index for index, ch in enumerate(pattern[1:-1]) if ch == "#")

    zoltage = line_split[-1]
    parsed_zoltage = [int(zolt) for zolt in zoltage[1:-1].split(",")]

    switch_groups = line_split[1:-1]

    def parse_switchs_to_switch_number(switches: str):
        parsed_switchs = switches[1:-1].split(",")
        return sum(1 << int(switch) for switch in parsed_switchs)

    swtich_group_nums = [
        parse_switchs_to_switch_number(switches) for switches in switch_groups
    ]

    return (pattern_num, swtich_group_nums, parsed_zoltage)


def main():
    input_path = "advent_of_code/2025/inputs/day_10.txt"
    lines = read_lines(input_path)
    parsed_input = [parse_line_to_bin_numbers(line) for line in lines]
    print(
        "Part 1 (Get Sum of Min Switch Flips): ",
        get_sum_of_min_switch_flips(parsed_input),
    )
    print(
        "Part 2 (Get Sum of Min Switches with Matching Zoltage):",
    )


if __name__ == "__main__":
    main()
