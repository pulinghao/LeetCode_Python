#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/5 8:32 下午
 @Author  :pulinghao@baidu.com
 @File     :830. 较大分组的位置.py
 @Description :
"""


class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        if len(s) == 0:
            return []
        start = s[0]
        st = 0
        res = []

        i = 1
        while i < len(s):
            if s[i] == start:
                pass
            else:
                if i - st > 2:
                    res.append([st, i - 1])
                start = s[i]
                st = i
            i += 1

        if i - st > 2:
            res.append([st, i - 1])
        return res

if __name__ == '__main__':
    s = "abcdddeeeeaabbbcdddd"
    print Solution().largeGroupPositions(s)