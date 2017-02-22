class Solution(object):
    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        total = sum(machines)
        length = len(machines)
        if total % length != 0:
            return -1
        avg = total / length
        count = 0
        left = 0
        for i in range(length):
            steps = 0
            if i > 0:
                left += machines[i-1]
            right = total - left - machines[i]
            if left < i * avg:
                steps += i * avg - left
            if right < (length - i - 1) * avg:
                steps += (length - i - 1) * avg - right
            count = max(count, steps)
        return count


test = Solution()
print test.findMinMoves([1, 0, 5])

# time: O(n)
#https://leetcode.com/contest/leetcode-weekly-contest-20/problems/super-washing-machines/

