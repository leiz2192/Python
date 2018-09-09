#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param: : a number
    @param: : digit needed to be rorated
    @return: a number
    """

    def leftRotate(self, n, d):
        bin_str = bin(n)[2:]
        supplement_num = 32 - len(bin_str)
        supplement_str = ''.join(str(0) for i in range(supplement_num))
        bin_str = supplement_str + bin_str
        bin_str = bin_str[d:] + bin_str[:d]
        return int(bin_str, 2)


def main():
    print(Solution().leftRotate(123, 4))
    print(Solution().leftRotate(255, 1))

if __name__ == '__main__':
    main()
