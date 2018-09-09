#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: numbers: An array of Integer
    @param: target: target = numbers[index1] + numbers[index2]
    @return: [index1 + 1, index2 + 1] (index1 < index2)
    """
    def twoSum(self, numbers, target):
        if numbers is None: return []
        if not numbers: return []
        num_hash = []
        for i in range(len(numbers)):
            expect = target - numbers[i]
            if (expect) in num_hash: return [num_hash.index(expect), i]
            num_hash.append(numbers[i])

if __name__ == "__main__":
    numbers = [2, 11, 7, 15]
    target = 9
    sol = Solution()
    print(sol.twoSum(numbers, target))

