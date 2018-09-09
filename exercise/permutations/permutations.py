#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: nums: A list of integers.
    @return: A list of permutations.
    """
    def permute(self, nums):
        if not nums:
            return [[]]
        nums_size = len(nums)
        if nums_size == 1:
            return [nums]
        res = []
        for i in range(nums_size):
            for j in self.permute(nums[:i] + nums[i+1:]):
                res.append([nums[i]] + j)
        return res


def main():
    print(Solution().permute([1, 2]))
    print(Solution().permute([1, 2, 3]))


if __name__ == '__main__':
    main()
