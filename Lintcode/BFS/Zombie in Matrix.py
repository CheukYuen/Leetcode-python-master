class Solution:
    # @param {int[][]} grid  a 2D integer grid
    # @return {int} an integer
    def zombie(self, grid):
        # Write your code here
        if grid is None or len(grid) == 0 or len(grid) == 0:
            return -1
        people = 0
        zombies = []
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    people += 1
                elif grid[i][j] == 1:
                    zombies.append([i, j])
        days = 0
        if people == 0:
            return 0
        dx = [1, 0, -1, 0]
        dy = [0, 1, 0, -1]

        # turn by BFS
        while zombies:
            days += 1
            size = len(zombies)
            for i in range(size):
                z = zombies.pop(0)
                for k in range(4):
                    x = dx[k] + z[0]
                    y = dy[k] + z[1]
                    if not self.isPeople(x, y, grid):
                        continue
                    zombies.append([x, y])
                    grid[x][y] = 1
                    people -= 1
                    if people == 0:
                        return days

        return -1

    def isPeople(self, x, y, grid):
        m = len(grid)
        n = len(grid[0])
        if x < 0 or x >= m:
            return False

        if y < 0 or y >= n:
            return False

        return grid[x][y] == 0


case = [[0, 1, 2, 0, 0], [1, 0, 0, 2, 1], [0, 1, 0, 0, 0]]
test = Solution()
print test.zombie(case)

