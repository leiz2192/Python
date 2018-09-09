#!/usr/bin/python
# -*- coding:utf-8 -*-


from collections import Iterable


def iter_flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from iter_flatten(x)
        else:
            yield x


class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        if isinstance(nestedList, int):
            return [nestedList]

        return [x for x in iter_flatten(nestedList)]

        # result_list = []
        # while nestedList:
        #     one_element = nestedList.pop(0)
        #     if isinstance(one_element, int):
        #         result_list.append(one_element)
        #     elif isinstance(one_element, list):
        #         while one_element:
        #             nestedList.insert(0, one_element.pop())
        # return result_list


def main():
    print(Solution().flatten([1, 2, [1, 2]]))
    print(Solution().flatten([4, [3, [2, [1]]]]))
    print(Solution().flatten([[1, 1], 2, [1, 1]]))
    print(Solution().flatten(10))


if __name__ == '__main__':
    main()
