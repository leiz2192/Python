#!/usr/bin/python
# -*- coding:utf-8 -*-

import collections

class Solution:
    """
    @param: s: a string
    @return: it's index
    """
    def firstUniqChar(self, s):
        s_map = collections.OrderedDict()
        for i, c in enumerate(s):
            if c in s_map:
                s_map[c]["count"] += 1
            else:
                s_map[c] = {"index": i, "count": 1}

        for c in s_map:
            if s_map[c]["count"] == 1:
                return s_map[c]["index"]
        return -1


def main():
    print(Solution().firstUniqChar("lintcode"))
    print(Solution().firstUniqChar("lovelintcode"))


if __name__ == '__main__':
    main()
