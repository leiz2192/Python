#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: a: An integer
    @param: b: An integer
    @return: The sum of a and b
    """
    def aplusb(self, a, b):
        minuend = 0
        if a < 0:
            a = abs(a)
            minuend += 2 * a
        if b < 0:
            b = abs(b)
            minuend += 2 * b
        while b != 0:
            sum = a ^ b
            carry = (a & b) << 1
            a = sum
            b = carry
        return a - minuend


def main():
    print(Solution().aplusb(5, 6))
    print(Solution().aplusb(13, 6))
    print(Solution().aplusb(-6, 3))


if __name__ == '__main__':
    main()
