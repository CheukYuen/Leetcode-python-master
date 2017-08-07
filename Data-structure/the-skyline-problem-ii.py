import heapq


class Solution(object):
    def getSkyline(self, buildings):
        v_lines = {l for b in buildings for l in (b[0], b[1])}
        heap = []
        i = 0
        res = []
        for vl in sorted(v_lines):
            while i < len(buildings) and buildings[i][0] <= vl:
                heapq.heappush(heap, (-buildings[i][2], buildings[i][1]))
                i += 1
            while heap and heap[0][1] <= vl:
                heapq.heappop(heap)
            h = len(heap) and -heap[0][0]
            if not res or res[-1][1] != h:
                res.append((vl, h))
        return res


c1 = [[1, 10, 1], [2, 9, 2], [3, 8, 3], [4, 7, 4], [5, 6, 5]]
c2 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
c3 = [[2, 5, 10], [3, 6, 12], [4, 7, 11]]
t = Solution()

print t.getSkyline(c1)
