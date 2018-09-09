#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: : An integer
    @param: : An integer
    @return: An integer denote the count of digit k in 1..n
    """
    def digitCounts(self, k, n):
        result = 0 if k != n else 1
        base = 1
        base_num = int(n / base)
        while base_num > 0:
            cur = int(base_num % 10)
            low = n - base_num * base
            high = int(n / (base * 10))

            if cur == k:
                result += high * base + low + 1
            elif cur < k:
                result += high * base
            elif cur > k:
                result += (high + 1) * base
            base *= 10
            base_num = int(n / base)

        if k == 0 and n != 0:
            cnt = 10
            while int(n / cnt) > 0:
                result -= cnt
                cnt *= 10
        if k == 0 and n == 0:
            result = 1

        return result


def main():
    print(Solution().digitCounts(1, 12))
    print(Solution().digitCounts(0, 19))


if __name__ == '__main__':
    main()
