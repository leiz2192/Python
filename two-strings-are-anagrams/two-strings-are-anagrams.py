#!/usr/bin/python
# -*- coding:utf-8 -*-

class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """
    def anagram(self, s, t):
        # write your code here
        s_list = []
        for c in s: s_list.append(c)
        s_list.sort()

        t_list = []
        for c in t: t_list.append(c)
        t_list.sort()

        return s_list == t_list


if __name__ == '__main__':
    solution = Solution()
    s = "abcd"
    t = "dcba"
    print(solution.anagram(s, t))