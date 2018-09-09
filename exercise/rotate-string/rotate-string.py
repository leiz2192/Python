#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param str: An array of char
    @param offset: An integer
    @return: nothing
    """
    def rotateString(self, str, offset):
        if not str:
            return str
        if offset < 0:
            return str
        str_size = len(str)
        offset = offset % str_size
        right_rotate = str[:(str_size - offset)]
        left_rotate = str[(str_size - offset):]
        after_rotate = left_rotate + right_rotate
        return after_rotate


def main():
    str = "abcdefg"
    print(Solution().rotateString(str, 2))
    print(Solution().rotateString("abcdefg", 3))
    print(Solution().rotateString("abc", 2))


if __name__ == '__main__':
    main()
