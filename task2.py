from collections import deque
import networkx as nx
from dfs import dfs_recursive
from bfs import bfs_recursive

# Граф
graph = {
    "0": ["1", "2", "3", "4"],
    "1": ["5"],
    "2": ["7"],
    "3": ["2", "5", "9", "11"],
    "4": ["5"],
    "5": ["6"],
    "6": ["12"],
    "7": ["8"],
    "9": ["8", "10"],
    "8": set(),
    "10": set(),
    "11": set(),
    "12": set(),
}

G = nx.Graph(graph)

dfs_tree = nx.dfs_tree(G, "0")
dfs_recursive(graph, "0")

bfs_tree = nx.bfs_tree(G, "0")
bfs_recursive(graph, deque(["0"]))
