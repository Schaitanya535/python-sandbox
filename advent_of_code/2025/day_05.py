from utils.file_reader import parse_ranges, read_blocks


def get_merged_ranges(
    fresh_ingredient_range: list[tuple[int, int]],
) -> list[tuple[int, int]]:
    """
    Merge overlapping or adjacent ranges.

    Example: [(1, 3), (2, 5), (7, 9)] -> [(1, 5), (7, 9)]
    """
    if not fresh_ingredient_range:
        return []

    # Sort ranges by start position
    sorted_ranges = sorted(fresh_ingredient_range)

    merged = [sorted_ranges[0]]

    for start, end in sorted_ranges[1:]:
        last_start, last_end = merged[-1]

        # Check if current range overlaps or is adjacent to the last merged range
        if start <= last_end + 1:
            # Merge by extending the end of the last range
            merged[-1] = (last_start, max(last_end, end))
        else:
            # No overlap, add as new range
            merged.append((start, end))

    return merged


def get_no_of_fresh_ingredients(
    fresh_ingredient_range: list[tuple[int, int]], ingredient_ids_list: list[int]
):
    count = 0
    for ingredient in ingredient_ids_list:
        for start, end in fresh_ingredient_range:
            if start <= ingredient <= end:
                count += 1
                break
    return count


def get_fresh_ingredients_by_ranges(
    merged_fresh_ingredient_range: list[tuple[int, int]],
):
    return sum([end - start + 1 for start, end in merged_fresh_ingredient_range])


def main():
    fresh_ingredient_list_block, ingredients_query_block = read_blocks(
        "/Users/chaitanyasura/Projects/python-sandbox/advent_of_code/2025/inputs/day_05.txt",
    )
    parsed_fresh_ingredient_ranges = [
        parse_ranges(range) for range in fresh_ingredient_list_block.split("\n")
    ]
    parsed_ingredient_list = [int(val) for val in ingredients_query_block.split("\n")]
    merged_ranges = get_merged_ranges(parsed_fresh_ingredient_ranges)
    print(
        "Part 1 (number of fresh_ingredients):",
        get_no_of_fresh_ingredients(merged_ranges, parsed_ingredient_list),
    )
    print(
        "Part 2 (directly count the ingredients only from the given ranges):",
        get_fresh_ingredients_by_ranges(merged_ranges),
    )


if __name__ == "__main__":
    main()
