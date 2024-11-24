import random

def generate_random_graph(num_nodes, num_edges):
    """
    Генерирует случайный граф с заданным количеством вершин и рёбер.
    :param num_nodes: Количество вершин
    :param num_edges: Количество рёбер
    :return: Граф в виде словаря смежности
    """
    graph = {i: [] for i in range(num_nodes)}
    edges = set()

    while len(edges) < num_edges:
        u, v = random.randint(0, num_nodes - 1), random.randint(0, num_nodes - 1)
        if u != v and (u, v) not in edges and (v, u) not in edges:
            graph[u].append(v)
            graph[v].append(u)
            edges.add((u, v))

    return graph
