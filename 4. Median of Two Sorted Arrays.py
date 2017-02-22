class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        n = len(nums1) + len(nums2)
        if n % 2 == 1:
            return self.findKth(nums1, nums2, n / 2 + 1)
        else:
            greater = self.findKth(nums1, nums2, n / 2 + 1)
            smaller = self.findKth(nums1, nums2, n / 2)
            return (greater + smaller) / 2.0

    def findKth(self, A, B, k):
        if not A:
            return B[k - 1]
        if not B:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])
        a = A[k / 2 - 1] if len(A) >= k / 2 else float('inf')
        b = B[k / 2 - 1] if len(B) >= k / 2 else float('inf')
        if a > b:
            return self.findKth(A, B[k / 2:], k - k / 2)
        else:
            return self.findKth(A[k / 2:], B, k - k / 2)

# Time: O(log(n+m))
# https://leetcode.com/problems/median-of-two-sorted-arrays/?tab=Description
# http://www.cnblogs.com/yuzhangcmu/p/4138184.html
# 举例证明
# A: 6 7 8
#
# B: 1 2 3 4 5
#
# 找第8th的数字，

# 1. 我们借用findKthNumber的思想。先实现findKthNumber，如果是偶数个，则把中间2个加起来平均，奇数就用中间的。
#
# 2. 为了达到LOG级的复杂度，我们可以这样：
#
# 每次在A，B取前k/2个元素。有以下这些情况：
#
# 1).  A的元素不够k/2. 则我们可以丢弃B前k/2. 反之亦然
#
# 证明：
#
# 我们使用反证法。
#
# 假设第K大在B的前k/2中，例如位置在索引m(m <= k/2-1)那么A必然拥有前k中的k -(m+1)个元素，而
#
# m <= k/2-1,则 m+1 <= k/2  , k - (m+1) > k/2与条件：A的元素不够k/2矛盾，所以假设不成立，得证。
#
# 举个栗子：
#

#
# 2). A[mid] < B[mid] (mid是k/2 -1索引处的元素）。
#
# 这种情况下，我们可以丢弃A前k/2。
#
# 证明：
#
# 我们使用反证法。
#
# 假设第K大在A的前k/2中记为maxK，例如位置在索引m(m <= k/2-1)那么B必然拥有前k中的k -(m+1)个元素，而
#
# m <= k/2-1,则 m+1 <= k/2  , k - (m+1) > k/2
#
# 推出B[mid] <= maxK
#
# 而A[mid] >= maxK 推出 A[mid]>=B[mid], 与题设矛盾。所以假设不能成立。