#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/7 7:40 下午
 @Author  :pulinghao@baidu.com
 @File     :131. 分割回文串.py
 @Description :
"""


class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        res = []
        path = []
        self.backtrack(s,res,path)
        return res

        pass

    def isPalindrome(self, s):
        return True if s == s[::-1] else False

    def backtrack(self, s, res, path):
        if not s:
            res.append(path)
            return

        for i in range(1,len(s) + 1):
            if self.isPalindrome(s[:i]):
                self.backtrack(s[i:],res,path + [s[:i]])


if __name__ == '__main__':
    print Solution().partition(s = "aab" )