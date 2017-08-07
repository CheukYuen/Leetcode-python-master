import collections


class Solution:
    # @param {int} numCourses a total of n courses
    # @param {int[][]} prerequisites a list of prerequisite pairs
    # @return {boolean} true if can finish all courses or false
    def canFinish(self, numCourses, prerequisites):
        # Write your code here
        hashmap = {}
        for pre in prerequisites:
            if pre[0] not in hashmap:
                hashmap[pre[0]] = 1
            else:
                hashmap[pre[0]] += 1

        queue = collections.deque()

        for pre in prerequisites:
            if pre[1] not in hashmap:
                queue.append(pre)

        count = 0

        while queue:
            count += 1
            print count
            pre = queue.popleft()
            hashmap[pre[0]] -= 1
            if hashmap[pre[0]] == 0:
                queue.append(pre)

        return numCourses == count


t = Solution()

print t.canFinish(2, [[1, 0]])