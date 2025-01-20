class List(list):
    pass


class Position:
    def __init__(self):
        self.cost = "inf"
        self.visited = False

    def __str__(self):
        if self.visited:
            return f"{self.cost}v"
        return f"{self.cost}x"

    def __repr__(self):
        return self.__str__()


class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])

        cost = [[Position()] * m for _ in range(n)]

        current = [0, 0]

        cost[0][0].cost = 0

        while True:
            x, y = current

            if x == n - 1 and y == m - 1:
                break

            cost[x][y].visited = True

            for i in range(4):
                if i == 0:
                    dx, dy = 0, 1
                elif i == 1:
                    dx, dy = 0, -1
                elif i == 2:
                    dx, dy = 1, 0
                else:
                    dx, dy = -1, 0

                nx, ny = x + dx, y + dy

                if nx < 0 or nx >= n or ny < 0 or ny >= m:
                    continue

                if i + 1 == grid[x][y]:
                    if cost[nx][ny].cost > cost[x][y].cost:
                        cost[nx][ny].cost = cost[x][y].cost
                else:
                    if cost[nx][ny].cost > cost[x][y].cost + 1:
                        cost[nx][ny].cost = cost[x][y].cost + 1

            min_cost = "inf"
            for i in range(n):
                for j in range(m):
                    if not cost[i][j].visited and cost[i][j].cost < min_cost:
                        min_cost = cost[i][j].cost
                        current = [i, j]

        return cost[n - 1][m - 1]


grid = [[1, 1, 1, 1], [2, 2, 2, 2], [1, 1, 1, 1], [2, 2, 2, 2]]

print(Solution().minCost(grid))
