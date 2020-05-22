#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/21 9:06 下午
@Author:  pulinghao
@File: 524. 通过删除字母匹配到字典里最长单词.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        d.sort()
        ptlist = []
        for string in d:
            pair = [0, len(string)]
            ptlist.append(pair)

        p = 0
        while p < len(s):
            char = s[p]
            for i in range(len(d)):
                str = d[i]
                pt = ptlist[i]
                idx = pt[0]
                length = pt[1]
                if idx < length:
                    if str[idx] == char:
                        idx += 1
                    ptlist[i] = [idx,length]
            p += 1
        maxLength = 0
        res_index = -1
        for pair in ptlist:
            idx = pair[0]
            length = pair[1]
            if idx == length:
                if length > maxLength:
                    maxLength = length
                    res_index = ptlist.index(pair)

        if res_index == -1:
            return ""
        else:
            return d[res_index]


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().findLongestWord(s="bab",d = ["ba", "ab", "a", "b"])
    # "bab"
    # ["ba", "ab", "a", "b"]
    print out 