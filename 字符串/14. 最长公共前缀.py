#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/15 12:02 下午
@Author:  pulinghao
@File: 14. 最长公共前缀.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""

        # 获取最短、最长的字符串，然后比较即可
        # 这步操作，实际上对字符串中的每个字符都比较了
        s1 = min(strs)
        s2 = max(strs)
        for i, x in enumerate(s1):
            if x != s2[i]:
                return s2[:i]
        return s1

if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().longestCommonPrefix(strs= ["flower","flow","flight"])

    print out 