my_graph = {
    "A": [("B", 5), ("C", 3), ("E", 11)],
    "B": [("A", 5), ("C", 1), ("F", 2)],
    "C": [("A", 3), ("B", 1), ("D", 1), ("E", 5)],
    "D": [("C", 1), ("E", 9), ("F", 3)],
    "E": [("A", 11), ("C", 5), ("D", 9)],
    "F": [("B", 2), ("D", 3)],
}


def shortest_path(graph, start, target=""):
    unvisited = list(graph)
    distances = {node: 0 if node == start else float("inf") for node in graph}
    paths = {node: [] for node in graph}
    paths[start].append(start)

    while unvisited:
        current = min(unvisited, key=distances.get)
        for node, distance in graph[current]:
            if distance + distances[current] < distances[node]:
                distances[node] = distance + distances[current]
                if paths[node] and paths[node][-1] == node:
                    paths[node] = paths[current][:]
                else:
                    paths[node].extend(paths[current])
                paths[node].append(node)
        unvisited.remove(current)

    targets_to_print = [target] if target else graph
    for node in targets_to_print:
        if node == start:
            continue
        print(
            f'\n{start}-{node} distance: {distances[node]}\nPath: {" -> ".join(paths[node])}'
        )

    return distances, paths


if __name__ == "__main__":
    shortest_path(my_graph, "A")
    # A-B distance: 4
    # Path: A -> C -> B

    # A-C distance: 3
    # Path: A -> C

    # A-D distance: 4
    # Path: A -> C -> D

    # A-E distance: 8
    # Path: A -> C -> E

    # A-F distance: 6
    # Path: A -> C -> B -> F

    shortest_path(my_graph, "A", "F")
    # A-F distance: 6
    # Path: A -> C -> B -> F
