import networkx as nx
import matplotlib.pyplot as plt

G = nx.DiGraph()
edges = [
    ("0", "1", 9),
    ("0", "2", 5),
    ("0", "3", 6),
    ("0", "4", 5),
    ("1", "5", 4),
    ("5", "6", 4),
    ("6", "12", 11),
    ("2", "7", 6),
    ("7", "8", 8),
    ("3", "9", 4),
    ("3", "11", 6),
    ("9", "10", 4),
    ("4", "5", 7),
    ("3", "2", 2),
    ("3", "5", 6),
    ("9", "8", 4),
]

pos = {
    "0": ([0, 0]),
    "1": ([4, -2]),
    "2": ([4, 8]),
    "3": ([4, 2]),
    "4": ([4, -6]),
    "5": ([10, -4]),
    "6": ([16, -4]),
    "7": ([10, 8]),
    "8": ([16, 8]),
    "9": ([16, 4]),
    "10": ([20, 4]),
    "11": ([20, 0]),
    "12": ([20, -2]),
}

G.add_weighted_edges_from(edges)

fig, ax = plt.subplots(figsize=(10, 6))
nx.draw_networkx_nodes(G, pos, node_size=300, node_color="skyblue", ax=ax)
nx.draw_networkx_labels(G, pos, font_size=8, ax=ax)
edge_labels = nx.get_edge_attributes(G, "weight")
nx.draw_networkx_edges(G, pos, width=1, ax=ax, edge_color="black", arrows=True)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=edge_labels, font_color="red", font_size=8
)

plt.show()

num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()

print(f"Список ребер: {list(G.edges)}")
print(f"Кількість вершин: {num_nodes}")
print(f"Кількість ребер: {num_edges}")
