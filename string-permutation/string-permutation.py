#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: A: a string
    @param: B: a string
    @return: a boolean
    """
    def Permutation(self, A, B):
        A_map = {}
        for c in A:
            if c in A_map:
                A_map[c] += 1
            else:
                A_map[c] = 1

        B_map = {}
        for c in B:
            if c in B_map:
                B_map[c] += 1
            else:
                B_map[c] = 1

        if len(A_map) != len(B_map):
            return False

        for c in A_map:
            if c in B_map and A_map[c] == B_map[c]:
                continue
            else:
                return False
        return True


def main():
    A = "^&*#$@%@%@$%@$!*&*&*)))!)()())( **jsafhjhsajfhthisisa lint"
    B = "^&)!)(%))thijhsajfhs)())( **jsafh*#$@%@$!*&*&sa lint*@%@$i"
    print(Solution().Permutation(A, B))


if __name__ == '__main__':
    main()
