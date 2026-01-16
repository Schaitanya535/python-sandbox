# utils/file_reader.py


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
