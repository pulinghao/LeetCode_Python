#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/9 10:32 上午
 @Author   :pulinghao@baidu.com
 @File     :5483. 整理字符串.py 
 @Description :
"""

class Solution(object):
    def makeGood(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        for i in range(len(s)):
            if stack:
                top = stack[-1]
                if ord(s[i]) == ord(top) + 32 or ord(s[i]) == ord(top) - 32:
                    stack.pop(-1)
                    continue

            stack.append(s[i])

        return ''.join(stack)

if __name__ == '__main__':
    print Solution().makeGood(s = "s")