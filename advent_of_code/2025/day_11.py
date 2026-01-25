from utils.file_reader import read_lines


def get_connections(lines: list[str]):
    connections: dict[str, list[str]] = {}

    for line in lines:
        key, val = line.split(":")
        parsed_vals = val.strip().split(" ")
        connections[key] = parsed_vals
    return connections


def get_total_paths_conditionally(
    connections: dict[str, list[str]],
    start: str = "svr",
    end: str = "out",
    must_visit: set[str] | None = None,
):
    if must_visit is None:
        must_visit = set(["fft", "dac"])

    memo = {}

    def dfs(node: str, visited_set: set[str], required_visited: frozenset[str]) -> int:
        if node == end:
            return 1 if len(required_visited) == len(must_visit) else 0

        # Memoization key: (current_node, which_required_nodes_visited)
        key = (node, required_visited)
        if key in memo:
            return memo[key]

        count = 0
        for next_node in connections.get(node, []):
            if next_node not in visited_set:
                new_visited = visited_set | {next_node}
                new_required = required_visited | (
                    {next_node} if next_node in must_visit else set()
                )
                count += dfs(next_node, new_visited, frozenset(new_required))

        memo[key] = count
        return count

    initial_required = frozenset({start} if start in must_visit else set())
    return dfs(start, {start}, initial_required)


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
    _input_path_test = "advent_of_code/2025/inputs/day_11_test_1.txt"
    input_path = "advent_of_code/2025/inputs/day_11.txt"
    lines = read_lines(input_path)
    connections = get_connections(lines)
    print(
        "Part 1 (Get total no. of paths from you to out):",
        get_total_paths(connections),
    )
    print(
        "Part 2 (Get total no. of paths which include  of paths):",
        get_total_paths_conditionally(connections),
    )


if __name__ == "__main__":
    main()
