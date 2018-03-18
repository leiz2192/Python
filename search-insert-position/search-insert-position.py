#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param A: an integer sorted array
    @param target: an integer to be inserted
    @return: An integer
    """
    def searchInsert(self, A, target):
        for index, one_num in enumerate(A):
            if one_num >= target:
                return index

        return len(A)


def main():
    print(Solution().searchInsert([1, 3, 5, 6], 5))
    print(Solution().searchInsert([1, 3, 5, 6], 2))
    print(Solution().searchInsert([1, 3, 5, 6], 7))
    print(Solution().searchInsert([1, 3, 5, 6], 0))


if __name__ == '__main__':
    main()
