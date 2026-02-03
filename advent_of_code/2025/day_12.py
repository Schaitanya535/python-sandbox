from utils.file_reader import read_blocks


def remove_shape(grid: list[list[str]], shape: list[list[str]], pos: tuple[int, int]):
    return None


def add_shape(grid: list[list[str]], shape: list[list[str]], pos: tuple[int, int]):
    return None


def generate_grid(dimensions: tuple[int, int]):
    return []


def get_number_of_valid_regions():
    return 1


def main():
    _input_path_test = "advent_of_code/2025/inputs/day_12_test.txt"
    input_path = "advent_of_code/2025/inputs/day_12.txt"
    blocks = read_blocks(_input_path_test)

    region_queries = blocks.pop()

    def get_parsed_region(region: str):
        dimensions, shapes_to_fit = region.split(":")

        x, y = [int(val) for val in dimensions.split("x")]
        no_of_shpaes = [int(val) for val in shapes_to_fit.strip().split(" ")]
        return ((x, y), no_of_shpaes)

    regions = [get_parsed_region(query) for query in region_queries.strip().split("\n")]
    shapes = [(block.splitlines()[1:]) for block in blocks]

    def get_rotated_shape_variants(shape: list[str]) -> list[list[str]]:
        return []

    shapes_with_variants = [get_rotated_shape_variants(shape) for shape in shapes]

    print(regions, "regions")
    print(shapes, "shapes")

    print(
        "Part 1 ():",
        # get_total_paths(connections),
    )
    print(
        "Part 2 ():",
        # get_total_paths_conditionally(connections),
    )


if __name__ == "__main__":
    main()
