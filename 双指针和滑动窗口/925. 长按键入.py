#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/10/21 12:59 下午
@Author:  pulinghao
@File: 925. 长按键入.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        j = 0
        while j < len(typed):
            if i < len(name) and name[i] == typed[j]:
                i += 1
                j += 1
            elif j > 0 and typed[j - 1] == typed[j]:
                j += 1
            else:
                return False

        return True if i == len(name) else False


if __name__ == '__main__':
    name = "alex"
    typed = "aaleex"
    out = Solution().isLongPressedName(name, typed)

    print out
