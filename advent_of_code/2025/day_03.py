from utils.file_reader import read_lines


def get_cummulative_joltage_of_n_batteries(battery_banks: list[str], n: int) -> int:
    total = 0
    for bank in battery_banks:
        curr_voltage = ""
        prev_bat_idx = -1
        for battery_number in range(1, n + 1):
            battery, battery_idx = get_max_volts_in_bank(
                bank, prev_bat_idx + 1, len(bank) - n + battery_number
            )
            curr_voltage += battery
            prev_bat_idx = battery_idx
        total += int(curr_voltage)
    return total


def get_max_volts_in_bank(bank: str, start: int, end: int):
    max, max_idx = bank[start], start
    for curr_idx in range(start, end):
        if bank[curr_idx] > bank[max_idx]:
            max = bank[curr_idx]
            max_idx = curr_idx
    return max, max_idx


def get_cummulative_joltage_of_two(battery_banks: list[str]) -> int:
    total = 0
    for bank in battery_banks:
        first_battery, first_battery_idx = get_max_volts_in_bank(bank, 0, len(bank) - 1)
        second_battery, _second_battery_idx = get_max_volts_in_bank(
            bank, first_battery_idx + 1, len(bank)
        )
        total += int(first_battery + second_battery)
    return total


def main():
    battery_banks = read_lines(
        "/Users/chaitanyasura/Projects/python-sandbox/advent_of_code/2025/inputs/day_03.txt",
    )
    print(
        "Part 1 (cummulative joltage of 2):",
        get_cummulative_joltage_of_two(battery_banks),
    )
    print(
        "Part 2 (cummulative joltage of 12):",
        get_cummulative_joltage_of_n_batteries(battery_banks, 12),
    )
    print(
        "Testing Part 2 (cummulative joltage of 2):",
        get_cummulative_joltage_of_n_batteries(battery_banks, 2),
    )


if __name__ == "__main__":
    main()
