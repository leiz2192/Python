#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param n: An integer
    @return: true if this is a happy number or false
    """
    def isHappy(self, n):
        while n != 1 and n != 4:
            t = 0
            while n != 0:
                t += (n % 10) * (n % 10)
                n = int(n / 10)

            n = t
        return n == 1


def main():
    print(Solution().isHappy(19))


if __name__ == '__main__':
    main()
