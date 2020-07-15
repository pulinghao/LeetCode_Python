#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/14 9:44 上午
@Author:  pulinghao
@File: 151. 翻转字符串里的单词.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strList = s.strip().split(' ')
        strList.reverse()
        res = ''
        for str in strList:
            if len(str) == 0:
                continue
            res += str + ' '

        ans = res[:-1]
        return ans

if __name__ == '__main__':
    line = "[]"
    out = Solution().reverseWords("a good   example")

    print out 