class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        graph_len = len(graph)
        visited = [0] * graph_len
        is_not_safe = [0] * graph_len

        for i in range(graph_len):
            visited[i] = 1
            search(i, graph, visited, is_not_safe)

    def search(self, index, graph, visited, is_not_safe):
        # fuck idk
