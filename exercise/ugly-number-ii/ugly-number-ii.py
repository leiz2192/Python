#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param n: An integer
    @return: the nth prime number as description.
    """
    def nthUglyNumber(self, n):
        ugly_nums = [1]
        cnt = 1
        index_for_2 = 0
        index_for_3 = 0
        index_for_5 = 0
        while cnt < n:
            next_ugly_num = min(ugly_nums[index_for_2] * 2, ugly_nums[index_for_3] * 3)
            next_ugly_num = min(next_ugly_num, ugly_nums[index_for_5] * 5)
            ugly_nums.append(next_ugly_num)
            if int(next_ugly_num / ugly_nums[index_for_2] == 2):
                index_for_2 += 1
            if int(next_ugly_num / ugly_nums[index_for_3] == 3):
                index_for_3 += 1
            if int(next_ugly_num / ugly_nums[index_for_5] == 5):
                index_for_5 += 1
            cnt += 1

        return ugly_nums[n - 1]


def main():
    print(Solution().nthUglyNumber(9))
    print(Solution().nthUglyNumber(2))


if __name__ == '__main__':
    main()
