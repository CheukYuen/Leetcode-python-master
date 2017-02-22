class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        sumToIndex = dict()
        sumToIndex[0] = -1
        maxLen = 0
        summ = 0
        for i in range(len(nums)):
            summ += nums[i]
            if summ in sumToIndex:
                maxLen = max(maxLen, i - sumToIndex[summ])
            else:
                sumToIndex[summ] = i
        return maxLen

# time: O(n)
# 525. Contiguous Array
# https://leetcode.com/contest/leetcode-weekly-contest-20/problems/contiguous-array/

