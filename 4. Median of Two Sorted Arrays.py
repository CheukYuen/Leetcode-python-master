class Solution:
    """
    @param A: An integer array.
    @param B: An integer array.
    @return: a double whose format is *.5 or *.0
    """

    def findMedianSortedArrays(self, A, B):
        # write your code here
        if not A and not B:
            return None
        n = len(A) + len(B)
        if n % 2 == 1:
            return self.findMid(A, B, n / 2 + 1)
        else:
            return (self.findMid(A, B, n / 2+1) + self.findMid(A, B, n / 2)) / 2.0

    def findMid(self, A, B, k):
        if not A:
            return B[k - 1]
        if not B:
            return A[k - 1]
        # k == 1
        if k <= 1:
            return min(A[0], B[0])
        n, m = len(A), len(B)
        # n/2 and m/2 is must being drop
        if k-1 <= n / 2 + m / 2:
            if A[n / 2] < B[m / 2]:
                return self.findMid(A, B[:m / 2], k)
            else:
                return self.findMid(A[:n / 2], B, k)
        else:
            # n/2 or m/2
            if A[n / 2] < B[m / 2]:
                return self.findMid(A[n / 2+1:], B, k - n / 2 - 1)
            else:
                return self.findMid(A, B[m / 2+1:], k - m / 2 - 1)


t = Solution()
print t.findMedianSortedArrays([1, 2], [3, 4])
