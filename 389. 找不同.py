#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/18 11:46 下午
 @Author  :pulinghao@baidu.com
 @File     :389. 找不同.py
 @Description :
"""


class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        lists = list(s)
        listt = list(t)
        lists.sort()
        listt.sort()

        news = "".join(lists)
        newt = "".join(listt)

        for i in range(len(news)):
            if news[i] != newt[i]:
                return newt[i]

        return newt[-1]


if __name__ == '__main__':
    s = "ae"
    t = "aea"
    out = Solution().findTheDifference(s, t)
    print out