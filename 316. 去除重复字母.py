#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/20 7:32 下午
 @Author  :pulinghao@baidu.com
 @File     :316. 去除重复字母.py
 @Description :
"""
import collections

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        remain_counter = collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and c < stack[-1] and remain_counter[stack[-1]] > 0:
                    stack.pop()
                stack.append(c)
            remain_counter[c] -= 1

        return ''.join(stack)

if __name__ == '__main__':
    print Solution().removeDuplicateLetters(s="cbacdcbc")