#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: nums: Given an integers array A
    @return: A long long array B and B[i]= A[0] * ... * A[i-1] * A[i+1] * ... * A[n-1]
    """
    def productExcludeItself(self, nums):
        if nums is None: return []
        if not nums: return []
        len_nums = len(nums)
        product_nums = [1 for i in range(len_nums)]
        product = 1
        for i in range(len_nums):
            product_nums[i] = product
            product *= nums[i]

        product = 1
        for i in range(len_nums - 1, -1, -1):
            product_nums[i] *= product
            product *= nums[i]

        return product_nums


if __name__ == '__main__':
    nums = [2, 3, 5]
    sol = Solution()
    print(sol.productExcludeItself(nums))

