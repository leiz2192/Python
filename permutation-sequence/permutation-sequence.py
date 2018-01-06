#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: n: n
    @param: k: the k th permutation
    @return: return the k-th permutation
    """
    def getPermutation(self, n, k):
        nums = [(i + 1) for i in range(n)]
        print(nums)
        factorial = 1
        for i in range(n):
            factorial *= (i + 1)

        k -= 1
        permutation = [0 for i in range(n)]
        for i in range(n):
            factorial /= (n - i)
            num_choose = nums[int(k / (factorial))]
            permutation[i] = num_choose
            nums.remove(num_choose)
            k %= factorial
        print(permutation)
        return ''.join(str(num) for num in permutation)


def main():
    print(Solution().getPermutation(3, 4))


if __name__ == '__main__':
    main()
