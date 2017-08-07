class Solution:
    # @param {int} k an integer
    # @param {int[]} nums an integer array
    # return {int} kth smallest element
    def kthSmallest(self, k, nums):
        # Write your code here
        return self.quickSort(nums, 0, len(nums) - 1, k)

    def quickSort(self, nums, l, r, k):

        pivot = nums[(l + r) / 2]
        left = l
        right = r
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
            while left <= right and nums[right] > pivot:
                right -= 1
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        if l < r and k <= right:
            return self.quickSort(nums, l, right, k)
        elif l < r and k >= left:
            return self.quickSort(nums, left, r, k)
        else:
            return nums[k - 1]


test = Solution()

print test.kthSmallest(3, [3, 2, 1, 2, 5])
