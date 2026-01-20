from utils.file_reader import read_lines


def get_sqared_distance(
    first_box: tuple[int, int, int], second_box: tuple[int, int, int]
) -> int:
    x1, y1, z1 = first_box
    x2, y2, z2 = second_box
    return (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2


def get_distances(box_coordinates: list[tuple[int, int, int]]):
    number_of_boxes = len(box_coordinates)
    distances: list[tuple[int, int, int]] = []
    for i in range(0, number_of_boxes - 1):
        for j in range(i + 1, number_of_boxes):
            distances.append(
                (get_sqared_distance(box_coordinates[i], box_coordinates[j]), i, j)
            )
    return sorted(distances)


# applying union find
def find(parent: dict[int, int], node: int) -> int:
    """Find the root parent of a node with path compression"""
    if node not in parent:
        parent[node] = node
    if parent[node] != node:
        parent[node] = find(parent, parent[node])  # Path compression
    return parent[node]


def connect(parent: dict[int, int], box1: int, box2: int) -> bool:
    """Union operation - connect two boxes"""
    root1 = find(parent, box1)
    root2 = find(parent, box2)
    if root1 != root2:
        parent[root1] = root2

    return root1 != root2


def get_product_of_last_connected_boxes(box_coordinates: list[tuple[int, int, int]]):
    distances = get_distances(box_coordinates)
    # Pre-fill parent dictionary - each node is its own parent initially
    parent: dict[int, int] = {i: i for i in range(len(box_coordinates))}

    last_connection = (distances[0][1], distances[0][2])

    for connection_number in range(0, len(distances)):
        _distance, box1, box2 = distances[connection_number]
        if connect(parent, box1, box2):
            last_connection = (box1, box2)

    final_box1, final_box2 = last_connection
    final_box1_x = box_coordinates[final_box1][0]
    final_box2_x = box_coordinates[final_box2][0]

    return final_box1_x * final_box2_x


def get_product_of_boxes_in_crucuit(
    box_coordinates: list[tuple[int, int, int]], no_of_connections: int, top_n: int = 3
):
    distances = get_distances(box_coordinates)

    # Pre-fill parent dictionary - each node is its own parent initially
    parent: dict[int, int] = {i: i for i in range(len(box_coordinates))}

    # Use the minimum of requested connections and available connections
    max_connections = min(no_of_connections, len(distances))
    for connection_number in range(0, max_connections):
        _distance, box1, box2 = distances[connection_number]
        connect(parent, box1, box2)

    # Count nodes in each component
    component_sizes: dict[int, int] = {}
    for node in range(len(box_coordinates)):
        root = find(parent, node)
        component_sizes[root] = component_sizes.get(root, 0) + 1

    # Get the top N largest circuits and multiply them
    sizes = sorted(component_sizes.values(), reverse=True)
    result = 1
    for i in range(min(top_n, len(sizes))):
        result *= sizes[i]
    return result


def main():
    input_path = "advent_of_code/2025/inputs/day_08.txt"
    lines = read_lines(input_path)
    co_ordinates: list[tuple[int, int, int]] = [
        tuple(int(coordinate) for coordinate in line.split(","))  # type: ignore
        for line in lines
    ]

    print(
        "Part 1 (Get product of no. of nodes in circuits): ",
        get_product_of_boxes_in_crucuit(co_ordinates, 1000),
    )
    print(
        "Part 2 (Get the product of x coordinates of the nodes that complted the full circuit):",
        get_product_of_last_connected_boxes(co_ordinates),
    )


if __name__ == "__main__":
    main()
