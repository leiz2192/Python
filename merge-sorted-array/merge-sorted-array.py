#/usr/bin/python
class Solution:
    """
    @param: A: sorted integer array A which has m elements, but size of A is m+n
    @param: m: An integer
    @param: B: sorted integer array B which has n elements
    @param: n: An integer
    @return: nothing
    """
    def mergeSortedArray(self, A, m, B, n):
        A[m:] = B
        A.sort()
        # one_index = m + n - 1
        # m -= 1
        # n -= 1
        # while m >= 0 and n >= 0:
        #     if A[m] > B[n]:
        #         A[one_index] = A[m]
        #         m -= 1
        #         one_index -= 1
        #     else:
        #         A[one_index] = B[n]
        #         n -= 1
        #         one_index -= 1
        # while m >=0:
        #     A[one_index] = A[m]
        #     m -= 1
        #     one_index -= 1
        #
        # while n >=0:
        #     A[one_index] = B[n]
        #     n -= 1
        #     one_index -= 1

if __name__ == '__main__':
    A = [1, 2, 4, 0, 0, 0]
    B = [3, 4, 5]
    sol = Solution()
    sol.mergeSortedArray(A, len(A) - 3, B, len(B))
    print(A)
