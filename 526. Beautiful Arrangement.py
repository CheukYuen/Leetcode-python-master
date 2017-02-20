class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        visited = set()
        self.ans = 0
        self.dfs(visited, N, 1)
        return self.ans

    def dfs(self, visited, N, depth):
        if depth == N+1:
            self.ans += 1
            return
        for i in range(N):
            if i + 1 in visited or (i + 1) % depth != 0 and depth % (i + 1) != 0:
                continue
            visited.add(i + 1)
            self.dfs(visited, N, depth + 1)
            visited.remove(i + 1)


test = Solution()
print test.countArrangement(10)

# Time: O(n!)

# https://leetcode.com/contest/leetcode-weekly-contest-20/problems/beautiful-arrangement/
# 526. Beautiful Arrangement
# Suppose you have N integers from 1 to N. We define a beautiful arrangement as an array that is
# constructed by these N numbers successfully if one of the following is true for the ith position
# (1 <= i <= N) in this array:
#
# The number at the ith position is divisible by i.
# i is divisible by the number at the ith position.
# Now given N, how many beautiful arrangements can you construct?
#
# Example 1:
# Input: 2
# Output: 2
# Explanation:
#
# The first beautiful arrangement is [1, 2]:
#
# Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).
#
# The second beautiful arrangement is [2, 1]:
#
# Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
#
# Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.
# Note:
# N is a positive integer and will not exceed 15.