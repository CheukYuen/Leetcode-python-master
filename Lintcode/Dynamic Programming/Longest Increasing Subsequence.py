class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        tails = []

        for i in range(size):
            if len(tails) == 0:
                tails.append(nums[i])
            elif tails[0] > nums[i]:
                tails[0] = nums[i]
            elif tails[-1] == nums[i]:
                continue
            elif tails[-1] < nums[i]:
                tails.append(nums[i])
            # replace tails[i] with smaller one
            else:
                start = 0
                end = len(tails) - 1
                while start + 1 < end:
                    mid = (start + end) / 2
                    if tails[mid] >= nums[i]:
                        end = mid
                    else:
                        start = mid
                index = start if tails[start] == nums[i] else end
                tails[index] = nums[i]
        return len(tails)


test = Solution()
print test.lengthOfLIS([4, 10, 4, 3, 8, 9])
