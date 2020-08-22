#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/19 10:04 下午
 @Author   :pulinghao@baidu.com
 @File     :647. 回文子串.py 
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.cnt = 0
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """

        # cnt = 0
        # for i in range(0,len(s)):
        #     for j in range(i + 1,len(s) + 1):
        #         if s[i:j] == s[i:j][::-1]:
        #             cnt += 1
        # return cnt

        def count(s, start, end):
            while start >= 0 and end < len(s) and s[start] == s[end]:
                self.cnt += 1
                start -= 1
                end += 1

        for i in range(len(s)):
            count(s, i, i)
            count(s, i, i + 1)

        return self.cnt

if __name__ == '__main__':
    print Solution().countSubstrings("aaa")