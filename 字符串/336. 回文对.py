#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/8/6 6:53 下午
@Author:  pulinghao
@File: 336. 回文对.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # 遍历words并保存索引
        dict = {}
        for i, word in enumerate(words):
            # 保存所有字符串的逆序
            dict[word[::-1]] = i

        def findWord(word, left, right):
            if word[left:right + 1] in dict.keys():
                return dict[word[left:right + 1]]
            else:
                return -1

        def isPalindrome(word, left, right):
            subword = word[left:right + 1]
            reverseWords = subword[::-1]
            if reverseWords == subword:
                return True
            else:
                return False

        ret = []
        for i, word in enumerate(words):
            m = len(word)
            for j in range(m + 1):
                # 从j到m-1位置的字符串是否为回文串，如果是的话，判断0到j-1的字符串是否在字典里
                if isPalindrome(word, j, m - 1):
                    # 找到剩下部分是否在字典里
                    find = findWord(word, 0, j - 1)
                    if find != -1 and find != i:  # 不是自己
                        ret.append([i, find])

                # 从0到j-1位置的字符串是否为回文串，如果是的话，判断j到m-1的字符串是否在字典里
                if j > 0 and isPalindrome(word, 0, j - 1):
                    find = findWord(word, j,m - 1)
                    if find != -1 and find != i:
                        ret.append([find,i])
        return ret


if __name__ == '__main__':
    out = Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])
    print out
