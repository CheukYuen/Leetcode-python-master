class Solution:
    def main(self, nums):
        if not nums:
            return nums
        self.sort(nums, len(nums))
        return nums

    def sort(self, nums, size):

        while size > 1:

            mi = self.findMax(nums, size)
            if mi != size - 1:
                self.filp(nums, mi)
                self.filp(nums, size - 1)
            size -= 1

    def findMax(self, nums, size):
        mi = 0
        maxNum = nums[0]
        for i in range(0, size):
            if nums[i] > maxNum:
                maxNum = nums[i]
                mi = i
        return mi

    def filp(self, nums, i):
        start = 0
        while start < i:
            nums[start], nums[i] = nums[i], nums[start]
            start += 1
            i -= 1


test = Solution()

print test.main([23, 10, 20, 11, 12, 6, 7])
