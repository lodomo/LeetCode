# I'm not happy with this because I don't understand it very well.
# But it works.

import heapq

queries = [[2, 4], [0, 2], [0, 4]]


class Graph:
    def __init__(self, nodes: dict):
        self.nodes = nodes

    def add_edge(self, u, v, weight=1):
        self.nodes[u][v] = weight


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph.nodes}
    predecessors = {node: None for node in graph.nodes}
    distances[start] = 0

    # Priority queue to store (distance, node) pairs
    priority_queue = [(0, start)]

    while priority_queue:
        # Get the smallest distance
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the distance is not better (outdated entry)
        if current_distance > distances[current_node]:
            continue

        # Check neighbors
        for neighbor, weight in graph.nodes[current_node].items():
            tentative_distance = current_distance + weight

            # If the new distance is smaller, update and push to the queue
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (tentative_distance, neighbor))

    return distances


def shortestDistanceAfterQueries(n: int, queries: list[list[int]]) -> list[int]:
    graph = {i: {} for i in range(n)}
    answer = []

    for i in range(n - 1):
        graph.add_edge(i, i + 1)

    for query in queries:
        start, end = query
        graph.add_edge(start, end)
        distances = dijkstra(graph, 0)
        answer.append(distances[n - 1])

    return answer


print(shortestDistanceAfterQueries(5, queries))
