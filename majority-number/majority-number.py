#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: nums: a list of integers
    @return: find a  majority number
    """
    def majorityNumber(self, nums):
        standard_len = int(len(nums) / 2)
        num_statistics = {}
        for one_num in nums:
            if one_num in num_statistics:
                num_statistics[one_num] += 1
            else:
                num_statistics[one_num] = 1

            if num_statistics[one_num] > standard_len:
                return one_num


def main():
    print(Solution().majorityNumber([1, 1, 1, 1, 2, 2, 2]))


if __name__ == '__main__':
    main()
