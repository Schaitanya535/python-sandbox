from utils.file_reader import read_lines


def count_zero_crossings(position, instructions):
    count = 0
    for instruction in instructions:
        direction = instruction[0]
        amount = int(instruction[1:])

        if direction == "L":
            new_position = position - amount
            if new_position < 0:
                # How many times we crossed 0
                count += (-new_position + 99) // 100
            position = new_position % 100
        else:
            # Moving forwards: count full rotations past 100 (which wraps through 0)
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
    lines = read_lines("./inputs/day_01.txt")
    print(count_zero_hits(50, lines))
    print(count_zero_crossings(50, lines))


if __name__ == "__main__":
    main()
