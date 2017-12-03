#!/usr/bin/python
# coding=utf-8

class Solution:
    """
    @param: A: A string
    @param: B: A string
    @return: if string A contains all of the characters in B return true else return false
    """
    def compareStrings(self, A, B):
        A_hash = [ 0 for i in range(26) ]
        for c in A: A_hash[ord(c) - ord('A')] += 1

        B_hash = [ 0 for i in range(26) ]
        for c in B: B_hash[ord(c) - ord('A')] += 1

        for i in range(26):
            if A_hash[i] < B_hash[i]: return False
        return True

    """
    @param: source: source string to be scanned.
    @param: target: target string containing the sequence of characters to match
    @return: a index to the first occurrence of target in source, or -1  if target is not part of source.
    """
    def strStr(self, source, target):
        if source is None: return -1
        if target is None: return -1
        return source.find(target)


if __name__ == "__main__":
    A = "ABCD"
    B = "AACD"
    sol = Solution()
    print(sol.compareStrings(A, B))

    source = "abcdabcdefg"
    target = "bcd"
    print(sol.strStr(source, target))