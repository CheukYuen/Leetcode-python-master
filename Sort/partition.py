arr = [10, 80, 30, 90, 40, 50, 70]

def partition(nums):
    pivot = 70
    left = 0
    for i in range(len(nums)):
        if nums[i] <= 70:
            nums[i], nums[left] = nums[left], nums[i]
            left += 1
    return nums

print partition(arr)