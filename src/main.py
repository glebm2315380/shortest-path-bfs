from collections import deque

def bfs_shortest_path(graph, start):
    """
    Реализация поиска кратчайших путей (BFS) для графов с единичными длинами рёбер.
    :param graph: Словарь смежности, описывающий граф
    :param start: Стартовая вершина
    :return: Словарь с минимальными расстояниями от стартовой вершины до остальных
    """
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = deque([start])

    while queue:
        current = queue.popleft()
        for neighbor in graph[current]:
            if distances[neighbor] == float('inf'):
                distances[neighbor] = distances[current] + 1
                queue.append(neighbor)

    return distances
