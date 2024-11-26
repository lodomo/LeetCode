class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        hasLost = set()
        hasWon = set()

        if len(edges) == 0:
            if n == 1:
                return 0
            else:
                return -1

        for edge in edges:
            hasLost.add(edge[1])
            hasWon.add(edge[0])

        champion = hasWon - hasLost
        total = hasWon.union(hasLost)

        if len(total) < n:
            return -1

        if len(champion) == 1:
            return champion.pop()
        else:
            return -1
