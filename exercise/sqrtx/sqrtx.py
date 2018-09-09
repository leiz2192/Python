#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param x: An integer
    @return: The sqrt of x
    """
    def sqrt(self, x):
        boundary = int(x / 2) + 1
        pre_num = 0
        for i in range(boundary + 1):
            square = i * i
            if square == x:
                return i
            if square < x:
                pre_num = i
            if square > x:
                return pre_num
        return pre_num


def main():
    print(Solution().sqrt(3))
    print(Solution().sqrt(5))


if __name__ == '__main__':
    main()
