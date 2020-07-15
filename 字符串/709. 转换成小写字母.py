#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/8 1:19 下午
@Author:  pulinghao
@File: 709. 转换成小写字母.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        newStr = ''
        for i in range(len(str)):
            char = str[i]
            ascii = ord(char)
            if ord(char) >= 65 and ord(char) < 91:
                ascii += 97 - 65
                newChar = chr(ascii)
                newStr += newChar
            else:
                newStr += char

        return newStr

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().toLowerCase("AZllo")

    print out 