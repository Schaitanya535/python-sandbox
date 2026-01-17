# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based Advent of Code (AoC) solution sandbox. Solutions are organized by year and day, with shared utilities for common input parsing patterns.

## Running Solutions

**Execute individual day solutions:**
```bash
# Set PYTHONPATH to project root for imports to work
PYTHONPATH=/Users/chaitanyasura/Projects/python-sandbox python advent_of_code/2025/day_XX.py
```

**Note:** The project uses a virtual environment (`.venv`) but it's not strictly required since there are no external dependencies currently.

## Project Structure

```
advent_of_code/
├── 2025/              # Year-specific solutions
│   ├── day_XX.py     # Solution files (executed directly)
│   └── inputs/       # Input data files
│       ├── day_XX.txt        # Main puzzle input
│       └── day_XX_test.txt   # Test/example input
utils/
└── file_reader.py    # Shared file parsing utilities
```

## Architecture Patterns

### Solution File Structure
Each day's solution follows this pattern:
```python
from utils.file_reader import read_*

def solve_part1(data):
    # Part 1 logic
    pass

def solve_part2(data):
    # Part 2 logic
    pass

def main():
    data = read_*("./inputs/day_XX.txt")
    print("Part 1:", solve_part1(data))
    print("Part 2:", solve_part2(data))

if __name__ == "__main__":
    main()
```

### File Reader Utilities

The `utils/file_reader.py` module provides specialized parsers for common AoC input patterns:

- `read_lines(path)` - List of stripped lines
- `read_raw(path)` - Entire file as single string
- `read_ints(path)` - List of integers (one per line)
- `read_grid(path)` - 2D character grid
- `read_comma_separated_input(path)` - Parse CSV-style input
- `read_range_input(path, convert_to_int=False)` - Parse range tuples like "10-20"

### Input File Paths

**Important:** There's currently an inconsistency in path handling:
- Day 1 uses relative paths: `"./inputs/day_01_input.txt"`
- Day 2 uses absolute paths: `"/Users/chaitanyasura/Projects/python-sandbox/advent_of_code/2025/inputs/day_02.txt"`

**Preferred approach:** Use relative paths from the solution file location to maintain portability.

## Adding New Solutions

1. Create `advent_of_code/YYYY/day_XX.py`
2. Add input files in `advent_of_code/YYYY/inputs/`
3. Import appropriate utilities from `utils.file_reader`
4. Implement `main()` with part 1 and part 2 solutions
5. Test with example input first (`day_XX_test.txt`)

## Python Module Imports

The project root must be in `PYTHONPATH` for relative imports to work:
```bash
export PYTHONPATH=/Users/chaitanyasura/Projects/python-sandbox
```

Or use the inline version shown in "Running Solutions" above.
