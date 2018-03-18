#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param nums: A list of integers
    @return: An integer denotes the middle number of the array
    """
    def median(self, nums):
        nums.sort()
        nums_size = len(nums)
        if nums_size & 1:
            return nums[int(nums_size / 2)]
        else:
            return nums[int(nums_size / 2) - 1]


def main():
    print(Solution().median([4, 5, 1, 2, 3]))
    print(Solution().median([7, 9, 4, 5]))


if __name__ == '__main__':
    main()
