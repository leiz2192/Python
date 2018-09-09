#!/usr/bin/python
# -*- coding:utf-8 -*-

import queue


class Solution:
    # @param k & A a integer and an array
    # @return ans a integer
    def kthLargestElement(self, k, A):
        priority_queue = queue.PriorityQueue()
        for element in A:
            priority_queue.put(element)
        array_size = len(A)
        result = 0
        cnt = 0
        while cnt < (array_size - k + 1):
            result = priority_queue.get()
            cnt += 1
        return result


def main():
    print(Solution().kthLargestElement(3, [9, 3, 2, 4, 8]))
    print(Solution().kthLargestElement(1, [9, 3, 2, 4, 8]))
    print(Solution().kthLargestElement(5, [9, 3, 2, 4, 8]))

if __name__ == '__main__':
    main()
