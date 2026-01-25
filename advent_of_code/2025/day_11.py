from utils.file_reader import read_lines


def get_connections(lines: list[str]):
    connections: dict[str, list[str]] = {}

    for line in lines:
        key, val = line.split(":")
        parsed_vals = val.strip().split(" ")
        connections[key] = parsed_vals
    return connections


def get_total_paths(
    connections: dict[str, list[str]], start: str = "you", end: str = "out"
):
    if start == end:
        return 1
    connected_nodes = connections.get(start, [])
    if len(connected_nodes) == 0:
        return 0

    return sum(get_total_paths(connections, node, end) for node in connected_nodes)


def main():
    input_path = "advent_of_code/2025/inputs/day_11.txt"
    lines = read_lines(input_path)
    connections = get_connections(lines)
    print(
        "Part 1 (Get total no. of paths from you to out):",
        get_total_paths(connections),
    )
    print(
        "Part 2 (Get total no. of paths which include  of paths):",
    )


if __name__ == "__main__":
    main()
