def parse_ranges(range_string: str) -> tuple[int, int]:
    start, end = range_string.split("-")
    return int(start), int(end)


def read_lines(filepath: str) -> list[str]:
    """Read file and return list of lines (stripped)."""
    with open(filepath) as f:
        return [line.strip() for line in f]


def read_raw(filepath: str) -> str:
    """Read entire file as single string."""
    with open(filepath) as f:
        return f.read().strip()


def read_ints(filepath: str) -> list[int]:
    """Read file where each line is an integer."""
    return [int(line) for line in read_lines(filepath)]


def read_grid(filepath: str) -> list[list[str]]:
    """Read file as 2D character grid."""
    return [list(line) for line in read_lines(filepath)]


def read_comma_separated_input(filepath: str):
    """Read file and take the comma separated input and give the list of strings"""
    with open(filepath) as f:
        return [item.strip() for line in f for item in line.split(",") if item.strip()]


def read_range_input(
    filepath: str, comma_separated: bool = False
) -> list[tuple[int, int]]:
    """Read file and take the input as range with a delimiter."""
    range_strings = (
        read_comma_separated_input(filepath)
        if comma_separated
        else read_lines(filepath)
    )
    return [parse_ranges(range_string) for range_string in range_strings]


def read_blocks(filepath: str) -> list[str]:
    """
    Read the nth block from a file where blocks are separated by 2+ blank lines.

    Args:
        filepath: Path to the file to read
        block_number: Zero-indexed block number to retrieve

    Returns:
        The content of the nth block as a string

    Raises:
        IndexError: If block_number is out of range
    """
    with open(filepath) as f:
        content = f.read()

    # Split by two or more consecutive newlines
    return [block.strip() for block in content.split("\n\n") if block.strip()]
