#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: A: An array of integers
    @return: An integer
    """
    def firstMissingPositive(self, A):
        if A is None: return None
        if not A: return 1
        i = 0
        A_size = len(A)
        while i < A_size:
            if A[i] == i + 1: i += 1
            else:
                value = A[i]
                if A[i] > 0 and A[i] <= A_size and A[value - 1] != value:
                    A[i], A[value - 1] = A[value - 1], value
                else: i += 1
        for i in range(A_size):
            if A[i] != i + 1: return (i + 1)
        return (A_size + 1)


if __name__ == '__main__':
    print(Solution().firstMissingPositive([3, 4, -1, 1]))
    print(Solution().firstMissingPositive([0, 2, -1, 1]))