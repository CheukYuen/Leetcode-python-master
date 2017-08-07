

def search(nums, target):
    start, end = 0, len(nums) - 1

    while start + 1 < end:
        mid = (start + end) / 2
        if nums[mid] < target:
            start = mid
        else:
            end = mid

    if target > nums[end]:
        return nums[end]
    return nums[start]


print search([1, 3, 5, 7, 9], 6)
