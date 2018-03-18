#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param a: An integer
    @param b: An integer
    @return: An integer
    """
    def bitSwapRequired(self, a, b):
        # print('{:031b}'.format(-1))
        c = a ^ b
        cnt = 0
        while c:
            cnt += c & 1
            c >>= 1
        return cnt


def main():
    print(Solution().bitSwapRequired(31, 14))
    print(Solution().bitSwapRequired(31, 67))
    # print(Solution().bitSwapRequired(1, -1))


if __name__ == '__main__':
    main()
