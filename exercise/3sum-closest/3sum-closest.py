#!/usr/bin/python
# -*- coding:utf-8 -*-

import sys

class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @param: target: An integer
    @return: return the sum of the three integers, the sum closest target.
    """
    def threeSumClosest(self, numbers, target):
        if numbers is None: return None
        if not numbers: return None
        nums_size = len(numbers)
        numbers.sort()
        sum_closest = sys.maxsize
        for i in range(nums_size):
            j = i + 1
            k = nums_size - 1
            while j < k:
                calc_sum = numbers[i] + numbers[j] + numbers[k]
                if calc_sum > target: k -= 1
                elif calc_sum < target: j += 1
                else: return calc_sum
                sum_closest = calc_sum if abs(target - calc_sum) < abs(target - sum_closest) else sum_closest
        return sum_closest



if __name__ == '__main__':
    print(Solution().threeSumClosest([-1, 2], 1))
    print(Solution().threeSumClosest([-1, 1, 2, -4], 1))