#!/usr/bin/python
# -*- coding:utf-8 -*-


import queue


class Solution(object):
    # @param nestedList a list, each element in the list
    # can be a list or integer, for example [1,2,[1,2]]
    # @return {int[]} a list of integer
    def flatten(self, nestedList):
        list_queue = queue.Queue()
        for one_ele in nestedList:
            list_queue.put(one_ele)

        result_list = []
        while not list_queue.empty():
            one_ele = list_queue.get()
            if isinstance(one_ele, int):
                result_list.append(one_ele)
            elif isinstance(one_ele, list):
                for one in one_ele:
                    list_queue.put(one)

        return result_list


def main():
    print(Solution().flatten([1, 2, [1, 2]]))
    print(Solution().flatten([4, [3, [2, [1]]]]))
    print(Solution().flatten([[1, 1], 2, [1, 1]]))


if __name__ == '__main__':
    main()
