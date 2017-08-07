class Solution:
    def main(self, nums):
        start, end = 0, len(nums) - 1
        minNum = 0
        for i in range(0, len(nums)):
            iMin = i
            for j in range(i, len(nums)):
                if nums[j] < nums[iMin]:
                    iMin = j
            if iMin != i:
                nums[iMin], nums[i] = nums[i], nums[iMin]
        return nums


t = Solution()

print t.main([64, 25, 12, 22, 11])
