#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: nums: An array of integers
    @return: nothing
    """
    def nextPermutation(self, nums):
        n = len(nums)
        right = n - 1
        # 从右往左，找第一个升序
        while right > 0:
            if nums[right] > nums[right - 1]:
                break
            else:
                right -= 1
        # 如果整个数组是降序排列，颠倒过来
        if right == 0:
            nums.reverse()
            return nums
        # 定位需要交换的低位
        right -= 1
        index = n - 1
        # 从右往左，找第一个比这个高位小的低位
        while index > right:
            # 交换高低位
            if nums[index] > nums[right]:
                nums[index], nums[right] = nums[right], nums[index]
                break
            else:
                index -= 1
        # 将被交换的高位之后的部分数组按逆序排列，因为只是上1个
        return nums[:right + 1] + sorted(nums[right + 1:], reverse=False)


def main():
    print(Solution().nextPermutation([1, 2, 7, 4, 3, 1]))
    print(Solution().nextPermutation([1, 3, 2]))


if __name__ == '__main__':
    main()
