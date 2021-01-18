#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/12/16 12:34 下午
@Author:  pulinghao
@File: 290. 单词规律.py
@Software: PyCharm
"""

import leetcode_utils
import collections


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        dict = collections.defaultdict(str)
        dict2 = collections.defaultdict(str)
        s_array = s.split(' ')
        if len(pattern) != len(s_array):
            return False

        for i in range(len(pattern)):
            if dict[pattern[i]] != '':
                if s_array[i] != dict[pattern[i]]:
                    return False
            else:
                dict[pattern[i]] = s_array[i]

            if dict2[s_array[i]] != '':
                if pattern[i] != dict2[s_array[i]]:
                    return False
            else:
                dict2[s_array[i]] = pattern[i]

        return True


if __name__ == '__main__':
    pattern = "abba"
    test = "dog dog dog dog"
    out = Solution().wordPattern(pattern, test)

    print out
