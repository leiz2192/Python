#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param numbers: Give an array
    @param target: An integer
    @return: Find all unique quadruplets in the array which gives the sum of zero
    """
    def fourSum(self, numbers, target):
        # write your code here
        n = len(numbers)
        numbers.sort()
        ans = []
        for i in range(n - 3):
            if i > 0 and numbers[i] == numbers[i - 1]: continue
            if numbers[i] + numbers[i + 1] + numbers[i + 2] + numbers[i + 3] > target: break
            if numbers[i] + numbers[n - 3] + numbers[n - 2] + numbers[n - 1] < target: continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and numbers[j] == numbers[j - 1]: continue
                if numbers[i] + numbers[j] + numbers[j + 1] + numbers[j + 2] > target: break
                if numbers[i] + numbers[j] + numbers[n - 2] + numbers[n - 1] < target: continue
                L, R = j + 1, n - 1
                while L < R:
                    temp = numbers[i] + numbers[j] + numbers[L] + numbers[R]
                    if temp == target:
                        ans.append([numbers[i], numbers[j], numbers[L], numbers[R]])
                        L += 1
                        R -= 1
                        while L < R and numbers[L] == numbers[L - 1]: L += 1
                        while R > L and numbers[R] == numbers[R + 1]: R -= 1
                    elif temp > target:
                        R -= 1
                    else:
                        L += 1
        return ans


def main():
    print(Solution().fourSum([1, 0, -1, 0, -2, 2], 0))
    print(Solution().fourSum([2,7,11,15], 3))


if __name__ == '__main__':
    main()
