#!/usr/bin/python
# -*- coding:utf-8 -*-

import math


class Solution:
    """
    @param n: the given number
    @return: true if it has exactly three distinct factors, otherwise false
    """

    def isThreeDisctFactors(self, n):
        square_root = int(math.sqrt(n))
        if square_root * square_root != n:
            return False

        if square_root <= 1:
            return False

        if square_root == 2:
            return True

        for i in range(2, int(math.sqrt(square_root)) + 1):
            if square_root % i == 0:
                return False

        return True


def main():
    print(Solution().isThreeDisctFactors(9))
    print(Solution().isThreeDisctFactors(10))
    print(Solution().isThreeDisctFactors(10000001400000049))


if __name__ == '__main__':
    main()
