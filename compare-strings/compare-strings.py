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

    """
    @param: strs: A list of strings
    @return: A list of strings
    """
    def anagrams(self, strs):
        if strs is None: return []
        result={}
        for str in strs:
            c_hash = [0 for i in range(26)]
            for c in str: c_hash[ord(c) - ord('a')] += 1
            c_str = "".join('%s' %c for c in c_hash)
            if c_str in result: result[c_str].append(str)
            else: result[c_str] = [str]

        final_result = []
        for c_str in result:
            if len(result[c_str]) > 1:
                final_result += result[c_str]
        return final_result

    """
    @param: A: A string
    @param: B: A string
    @return: the length of the longest common substring.
    """
    def longestCommonSubstring(self, A, B):
        len_A = len(A)
        len_B = len(B)
        record = [[0 for i in range(len_B + 1)] for j in range(len_A + 1)]
        max_len = 0
        for i in range(len_A):
            for j in range(len_B):
                if A[i] != B [j]: continue
                record[i + 1][j + 1] = record[i][j] + 1
                if max_len < record[i + 1][j + 1]: max_len = record[i + 1][j + 1]
        return max_len

    """
    @param: strs: A list of strings
    @return: The longest common prefix
    """
    def longestCommonPrefix(self, strs):
        if strs is None: return ""
        if len(strs) == 0: return ""
        strs.sort(key=lambda x:len(x))
        longest_prefix = strs[0]
        max_len_prefix = len(longest_prefix)
        for i in range(max_len_prefix):
            for one_str in strs:
                if longest_prefix[i] != one_str[i]:
                    return longest_prefix[:i]
        return longest_prefix

if __name__ == "__main__":
    A = "ABCD"
    B = "AACD"
    sol = Solution()
    print(sol.compareStrings(A, B))

    source = "abcdabcdefg"
    target = "bcd"
    print(sol.strStr(source, target))

    strs = ["lint","intl","inlt","code"]
    print(sol.anagrams(strs))

    A = "ABCD"
    B = "CBCE"
    print(sol.longestCommonSubstring(A, B))

    strs = ["ABCDEFG", "ABCEFG", "ABCEF"]
    print(sol.longestCommonPrefix(strs))
