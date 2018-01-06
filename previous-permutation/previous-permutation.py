#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: nums: A list of integers
    @return: A list of integers that's previous permuation
    """
    def previousPermuation(self, nums):
        n = len(nums)
        right = n - 1
        # 从右往左，找第一个升序
        while right > 0:
            if nums[right] < nums[right - 1]:
                break
            else:
                right -= 1
        # 如果整个数组是降序排列，颠倒过来
        if right == 0:
            nums.reverse()
            return nums
        # 定位需要交换的高位
        right -= 1
        index = n - 1
        # 从右往左，找第一个比这个高位小的低位
        while index > right:
            # 交换高地位
            if nums[index] < nums[right]:
                nums[index], nums[right] = nums[right], nums[index]
                break
            else:
                index -= 1
        # 将被交换的高位之后的部分数组按逆序排列，因为只是上1个
        return nums[:right + 1] + sorted(nums[right + 1:], reverse=True)


def main():
    print(Solution().previousPermuation([1,3,2,3]))
    print(Solution().previousPermuation([1,2,3,4]))


if __name__ == '__main__':
    main()
