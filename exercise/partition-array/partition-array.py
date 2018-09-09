#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: nums: The integer array you should partition
    @param: k: An integer
    @return: The index after partition
    """
    def partitionArray(self, nums, k):
        if nums is None: return None
        if not nums: return 0
        nums_size = len(nums)
        i = 0
        j = nums_size - 1
        pos = 0
        while i < j:
            if nums[i] >= k and nums[j] < k:
                nums[i], nums[j] = nums[j], nums[i]
                pos = j
                i += 1
                j -= 1
            elif nums[i] >= k and nums[j] >= k:
                j -= 1
            elif nums[i] < k and nums[j] < k:
                i += 1
            elif nums[i] < k and nums[j] >=k:
                pos = i
                i += 1
                j -= 1
        return i if nums[i] >= k else (i + 1)

if __name__ == '__main__':
    print(Solution().partitionArray([4, 3, 2, 1, 6], 5))
    print(Solution().partitionArray([3, 2, 2, 1], 2))