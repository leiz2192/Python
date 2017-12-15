#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers includes the index of the first number and the index of the last number
    """
    def subarraySum(self, nums):
        if nums is None: return []
        if not nums: return []
        if nums[0] == 0: return [0, 0]
        sum_hash = {}
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum == 0: return [0, i]
            if sum in sum_hash: return [sum_hash[sum] + 1, i]
            sum_hash[sum] = i
        return []

if __name__ == '__main__':
    nums = [-2, 1, 2, -3, 4]
    sol = Solution()
    print(sol.subarraySum(nums))
    print(sol.subarraySum([]))
    print(sol.subarraySum([0, -3]))

