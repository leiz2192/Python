#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
    """
    def threeSum(self, numbers):
        if numbers is None: return []
        if not numbers: return []
        nums_size = len(numbers)
        numbers.sort()
        triplets = []
        for i in range(nums_size):
            j = i + 1
            k = nums_size - 1
            while j < k:
                calc_sum = numbers[i] + numbers[j] + numbers[k]
                if calc_sum > 0: k -= 1
                elif calc_sum < 0: j += 1
                else:
                    find_tup = ((numbers[i], numbers[j], numbers[k]))
                    if find_tup not in triplets: triplets.append(find_tup)
                    k -= 1
                    j += 1
        return triplets


if __name__ == '__main__':
    print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))
    print(Solution().threeSum([-2,-3,5,-1,-4,5,-11,7,1,2,3,4,-7,-1,-2,-3,-4,-5]))