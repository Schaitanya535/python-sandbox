from utils.file_reader import read_lines


def calculate_area(p1: tuple[int, int], p2: tuple[int, int]) -> int:
    x1, y1 = p1
    x2, y2 = p2

    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1

    return width * height


def get_largest_rectangle_area(points_list: list[tuple[int, int]]) -> int:
    largest_area = 0
    for i in range(len(points_list) - 1):
        for j in range(i, len(points_list)):
            area = calculate_area(points_list[i], points_list[j])
            largest_area = max(area, largest_area)

    return largest_area


def main():
    input_path = "advent_of_code/2025/inputs/day_09.txt"
    lines = read_lines(input_path)
    co_ordinates_list: list[tuple[int, int]] = [
        tuple(int(coordinate) for coordinate in line.split(","))  # type: ignore
        for line in lines
    ]

    print(
        "Part 1 (Get Max Area Rectangle from Co ordinates): ",
        get_largest_rectangle_area(co_ordinates_list),
    )
    print(
        "Part 2 (Get the product of x coordinates of the nodes that complted the full circuit):",
    )


if __name__ == "__main__":
    main()
