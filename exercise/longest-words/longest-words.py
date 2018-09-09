#!/usr/bin/python
# -*- coding:utf-8 -*-


class Solution:
    """
    @param: dictionary: an array of strings
    @return: an arraylist of strings
    """
    def longestWords(self, dictionary):
        max_word_len = 0
        words_statistics = {}
        for one_word in dictionary:
            word_len = len(one_word)
            if word_len > max_word_len:
                max_word_len = word_len
            if word_len in words_statistics:
                words_statistics[word_len].append(one_word)
            else:
                words_statistics[word_len] = [one_word]

        return words_statistics[max_word_len]


def main():
    print(Solution().longestWords({"dog", "google", "facebook", "internationalization", "blabla"}))
    print(Solution().longestWords({"like", "love", "hate", "yes"}))


if __name__ == '__main__':
    main()
