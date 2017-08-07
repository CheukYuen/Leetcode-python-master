import collections


def numIslands(grid):
    def check(x, y, grid, visited):
        n = len(grid)
        m = len(grid[0])
        if 0 <= x < n and 0 <= y < m and visited[x][y] == False and grid[x][y] == 1:
            return True
        return False

    def bfs(x, y, grid, visited, count):
        if check(x, y, grid, visited):
            queue = collections.deque()
            queue.append((x, y))
            dx = [1, 0, -1, 0]
            dy = [0, 1, 0, -1]
            while queue:
                coor = queue.popleft()
                for i in range(4):
                    cx = coor[0] + dx[i]
                    cy = coor[1] + dy[i]
                    if check(cx, cy, grid, visited):
                        queue.append((cx, cy))
                        visited[cx][cy] = True
            count[0] += 1

    if not grid or not grid[0]:
        return 0
    n = len(grid)
    m = len(grid[0])
    visited = [[False for _ in range(m)] for _ in range(n)]
    count = [0]
    for i in range(n):
        for j in range(m):
            bfs(i, j, grid, visited, count)
    return count[0]
