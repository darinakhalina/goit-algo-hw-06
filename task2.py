from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def dfs_recursive(graph, vertex, visited=None):
    if visited is None:
        visited = set()
    visited.add(vertex)
    print(vertex, end=" ")  # Відвідуємо вершину
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs_recursive(graph, neighbor, visited)


def bfs_recursive(graph, queue, visited=None):
    # Перевіряємо, чи існує множина відвіданих вершин, якщо ні, то ініціалізуємо нову
    if visited is None:
        visited = set()
    # Якщо черга порожня, завершуємо рекурсію
    if not queue:
        return
    # Вилучаємо вершину з початку черги
    vertex = queue.popleft()
    # Перевіряємо, чи відвідували раніше дану вершину
    if vertex not in visited:
        # Якщо не відвідували, друкуємо вершину
        print(vertex, end=" ")
        # Додаємо вершину до множини відвіданих вершин.
        visited.add(vertex)
        # Додаємо невідвіданих сусідів даної вершини в кінець черги.
        queue.extend(set(graph[vertex]) - visited)
    # Рекурсивний виклик функції з тією ж чергою та множиною відвіданих вершин
    bfs_recursive(graph, queue, visited)


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
print(list(dfs_tree.nodes()))
dfs_recursive(graph, "0")

bfs_tree = nx.bfs_tree(G, "0")
print(list(bfs_tree.nodes()))
bfs_recursive(graph, deque(["0"]))
