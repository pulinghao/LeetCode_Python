#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/14 9:32 下午
 @Author   :pulinghao@baidu.com
 @File     :392. 判断子序列.py 
 @Description :
"""

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        i = 0
        j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        if i == len(s):
            return True
        else:
            return False

        # 迭代器
        t = iter(t)
        res = []
        for c in s:
            if c in t:
                res.append(c)
            else:
                res.append(None)

        res = iter(res)
        return all(res)
        # c in t for c in s

if __name__ == '__main__':
    print Solution().isSubsequence(s = "abc", t = "ahbgdc")