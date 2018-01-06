#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    def simplicity_fast_power(self, a, b, n):
        ans = 1
        for i in range(n):
            ans *= a
            ans %= b
        ans = 1 % b if n == 0 else ans
        return ans

    """
    @param: a: A 32bit integer
    @param: b: A 32bit integer
    @param: n: A 32bit integer
    @return: An integer
    """
    def fastPower(self, a, b, n):
        if n == 0:
            return 1 % b

        ans = 1
        a %= b
        while(n):
            if n & 1:
                ans = ans * a % b
            n >>= 1
            a = a * a % b
        return ans


def main():
    print(Solution().fastPower(3, 7, 5))
    print(Solution().fastPower(2, 3, 31))
    print(Solution().fastPower(2, 1, 0))
    print(Solution().fastPower(2, 2, 0))
    print(Solution().fastPower(2, 2147483647, 2147483647))


if __name__ == '__main__':
    main()
