#!/usr/bin/python
# -*- coding:utf-8 -*-


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    """
    @param: intervals: Sorted interval list.
    @param: newInterval: new interval.
    @return: A new interval list.
    """
    def insert(self, intervals, newInterval):
        new_interval_list = []
        insert_pos = 0
        for one_interval in intervals:
            if one_interval.end < newInterval.start:
                new_interval_list.append(one_interval)
                insert_pos += 1
            elif one_interval.start > newInterval.end:
                new_interval_list.append(one_interval)
            else:
                newInterval.start = min(one_interval.start, newInterval.start)
                newInterval.end = max(one_interval.end, newInterval.end)
        new_interval_list.insert(insert_pos, newInterval)
        return new_interval_list


def main():
    new_interval = Interval(2, 5)
    interval_list = [Interval(1, 2), Interval(5, 9)]
    new_interval_list = Solution().insert(interval_list, new_interval)
    for one_interval in new_interval_list:
        print("[", one_interval.start, ",", one_interval.end, "]")

    new_interval = Interval(3, 4)
    new_interval_list = Solution().insert(interval_list, new_interval)
    for one_interval in new_interval_list:
        print("[", one_interval.start, ",", one_interval.end, "]")

if __name__ == '__main__':
    main()
