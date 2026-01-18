"""
Direction constants for grid-based problems (e.g., Advent of Code).

Provides commonly used direction patterns for navigating 2D grids.
"""

# 4 directions: up, down, left, right (cardinal directions)
DIRECTIONS_4 = [
    (-1, 0),  # up
    (1, 0),  # down
    (0, -1),  # left
    (0, 1),  # right
]

# 8 directions: cardinal + diagonal directions
DIRECTIONS_8 = [
    (-1, -1),
    (-1, 0),
    (-1, 1),  # top-left, top, top-right
    (0, -1),
    (0, 1),  # left, right
    (1, -1),
    (1, 0),
    (1, 1),  # bottom-left, bottom, bottom-right
]


# Named directions for more readable code
class Direction4:
    """Named constants for 4-directional movement."""

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)


class Direction8:
    """Named constants for 8-directional movement."""

    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)
    UP_LEFT = (-1, -1)
    UP_RIGHT = (-1, 1)
    DOWN_LEFT = (1, -1)
    DOWN_RIGHT = (1, 1)
