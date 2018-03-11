#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: x: the base number
    @param: n: the power number
    @return: the result
    """
    def myPow(self, x, n):
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x

        positive_n = int(abs(n) / 2)
        result = self.myPow(x, positive_n)
        result *= result

        if n & 1:
            result *= x

        if n < 0:
            return 1.0 / result
        return result


def main():
    print(Solution().myPow(3, 4))
    print(Solution().myPow(8.88023, 3))
    print(Solution().myPow(2.00000, -2147483648))
    print(Solution().myPow(8.95371, -1))
    print(Solution().myPow(2.0, 20))


if __name__ == '__main__':
    main()
