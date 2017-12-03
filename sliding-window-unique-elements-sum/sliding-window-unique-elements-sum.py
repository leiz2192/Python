#!/usr/bin/python
# coding=utf-8


class Solution:
    """
    @param: : the given array
    @param: : the window size
    @return: the sum of the count of unique elements in each window
    """
    def slidingWindowUniqueElementsSum(self, nums, k):
        # write your code here
        sum = 0
        nums_size = len(nums)
        win_count = 0
        ele_count = 0
        if nums_size < k:
            win_count = 1
            ele_count = nums_size
        else:
            win_count = nums_size - k + 1
            ele_count = k

        win_eles = []
        rep_eles = {}
        for ele_index in range(ele_count):
            ele = nums[ele_index]
            if win_eles.count(ele) > 0:
                win_eles.remove(ele)
                rep_eles[ele] = 1

            if ele in rep_eles:
                rep_eles[ele] += 1
            else:
                win_eles.append(ele)
        sum += len(win_eles)

        for win_index in range(1, win_count):
            ele = nums[win_index - 1]
            if ele in rep_eles:
                if rep_eles[ele] == 2:
                    win_eles.append(ele)
                    del rep_eles[ele]
                elif rep_eles[ele] > 2:
                    rep_eles[ele] -= 1
            else:
                win_eles.remove(ele)

            ele = nums[ele_count + win_index  - 1]
            if win_eles.count(ele) > 0:
                win_eles.remove(ele)
                rep_eles[ele] = 1

            if ele in rep_eles:
                rep_eles[ele] += 1
            else:
                win_eles.append(ele)
            sum += len(win_eles)
        return sum


if __name__ == '__main__':
    nums = [27,14,60,87,37,53,100,18,51,37,14,57,22,95,50,83,41,43,36,48,52,97,16,46,75,24,47,13,40,40,48,45,56,58,77,3,78,60,31,27,40,53,57,29,30,65,37,77,1,40,89,100,50,49,100,51,22,66,33,33,70,36,64,70,11,27,57,77,17,28,62,70,32,88,12,47,69,30,93,3,47,69,64,88,7,40,38,5,23,4,58,97,19,55,17,23]
    k = 21
    solution = Solution()
    print(solution.slidingWindowUniqueElementsSum(nums, k))



