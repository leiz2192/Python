#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param n: An integer
    @return: A list of strings.
    """
    def fizzBuzz(self, n):
        str_list = []
        if n < 1:
            return str_list

        for num in range(1, n + 1):
            if num % 3 == 0 and num % 5 == 0:
                str_list.append('fizz buzz')
            elif num % 3 == 0:
                str_list.append('fizz')
            elif num % 5 == 0:
                str_list.append('buzz')
            else:
                str_list.append(str(num))

        return str_list


def main():
    print(Solution().fizzBuzz(15))


if __name__ == '__main__':
    main()
