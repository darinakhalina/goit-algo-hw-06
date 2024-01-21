import networkx as nx


def find_shortest_paths(graph, start, end_vertices):
    shortest_paths = {}
    for end in end_vertices:
        try:
            shortest_path = nx.shortest_path(graph, source=start, target=end)
            shortest_path_length = nx.shortest_path_length(
                graph, source=start, target=end
            )
            shortest_paths[end] = {
                "path": shortest_path,
                "length": shortest_path_length,
            }
        except nx.NetworkXNoPath:
            shortest_paths[end] = {"path": None, "length": float("inf")}
    return shortest_paths
