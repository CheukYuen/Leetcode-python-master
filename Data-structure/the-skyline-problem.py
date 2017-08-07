class Solution(object):
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        if not buildings:
            return []
        hashmap = {}
        for build in buildings:
            hashmap[build[0]] = build[2]
            hashmap[build[1]] = 0

        for build in buildings:
            for point in buildings:
                if build is point:
                    continue
                if build[0] <= point[0] < build[1]:
                    height1 = max(build[2], hashmap[point[0]])
                    hashmap[point[0]] = height1

                if build[0] <= point[1] < build[1]:
                    height2 = max(build[2], hashmap[point[1]])
                    hashmap[point[1]] = height2

        arr = []
        ans = []
        for key, value in hashmap.items():
            arr.append([key, value])
        arr.sort(key=lambda x:x[0])

        ans.append(arr[0])
        for i in range(1, len(arr)):
            if arr[i - 1][1] == arr[i][1]:
                continue
            ans.append(arr[i])
        return ans


t = [[2, 5, 10], [3, 6, 12], [4, 7, 11]]
t2 = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
t3 = [[2, 9, 10], [9, 12, 15]]
s = Solution()
print s.getSkyline(t3)
