#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/30 8:49 下午
 @Author  :pulinghao@baidu.com
 @File     :557. 反转字符串中的单词 III.py
 @Description :
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s.split(' ')
        temp = []
        for word in arr:
            temp.append(word[::-1])

        res = ' '.join(temp)
        return res

if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print Solution().reverseWords(s)