def minSubarraySum(nums):
    summ = 0
    maxSumm = 0
    res = float('inf')
    for n in nums:
        summ += n
        res = min(res, summ - maxSumm)
        maxSumm = max(summ, maxSumm)

    return res


print minSubarraySum([1, 2, 3, 9])
