#!/usr/bin/python
# -*- coding:utf-8 -*-
import math


class Solution:
    """
    @param: n: An integer
    @return: An integer, denote the number of trailing zeros in n!
    """
    def trailingZeros(self, n):
        count = 0
        i = 1
        m = math.pow(5, i)
        while math.pow(5, i) < n:
            count += (int)(n / m)
            i += 1
            m = math.pow(5, i)
        return count


def main():
    print(Solution().trailingZeros(26))
    print(Solution().trailingZeros(1000))


if __name__ == '__main__':
    main()

