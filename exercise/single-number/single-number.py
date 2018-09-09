#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param A: An integer array
    @return: An integer
    """
    def singleNumber(self, A):
        duplicate_list = []
        while A:
            one_element = A.pop()
            if one_element in A:
                duplicate_list.append(one_element)
            if one_element not in duplicate_list:
                return one_element


def main():
    print(Solution().singleNumber([1,2,2,1,3,4,3]))
    print(Solution().singleNumber([1,1,2,2,3,4,4]))


if __name__ == '__main__':
    main()
