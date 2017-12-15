#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        if nums is None: return 0
        nums_len = len(nums)
        if nums_len == 0: return 0
        if nums_len == 1: return 1
        # elem = nums[nums_len - 1]
        # for i in range(nums_len - 2, -1, -1):
        #     if nums[i] != elem: elem = nums[i]
        #     else: nums.remove(elem)

        last_index = 0
        for i in range(1, nums_len):
            if nums[i] != nums[last_index]:
                last_index += 1
                nums[last_index] = nums[i]
        del nums[last_index + 1:nums_len]
        print(nums)
        return len(nums)

if __name__ == '__main__':
    nums = [1, 1, 2, 2]
    sol = Solution()
    print(sol.removeDuplicates(nums))
    print(sol.removeDuplicates([1, 2]))

