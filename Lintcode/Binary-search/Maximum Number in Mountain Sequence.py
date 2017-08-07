def mountainSequence(nums):
    # Write your code here
    if not nums or len(nums) == 0:
        return None
    start = 0
    end = len(nums) - 1
    while start + 1 < end:
        mid1 = (end - start) / 2 + start
        mid2 = end - (end - mid1) / 2
        if nums[mid1] < nums[mid2]:
            start = mid1 + 1
        elif nums[mid1] > nums[mid2]:
            end = mid2 - 1
        else:
            start = mid1
            end = mid2

    return max(nums[start], nums[end])


print mountainSequence([1, 3, 8, 5, 4])
