#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: A: A list of integers
    @param: elem: An integer
    @return: The new length after remove
    """
    def removeElement(self, A, elem):
        if A is None: return 0,[]
        if not A: return 0,[]
        while elem in A: A.remove(elem)
        # result = [e for e in A if e != elem]
        return len(A), A

if __name__ == '__main__':
    A = [0,4,4,0,4,4,4,0,2]
    elem = 4
    sol = Solution()
    print(sol.removeElement(A, elem))
    print(sol.removeElement(None, elem))
    print(sol.removeElement([], elem))
