#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/7 8:58 下午
 @Author   :pulinghao@baidu.com
 @File     :20. 有效的括号.py 
 @Description :
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        for c in s:
            if c == '{' or c == '(' or c == '[':
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                if c == ')':
                    if stack[-1] == '(':
                        stack.pop()
                    else:
                        return False
                if c == ']':
                    if stack[-1] == '[':
                        stack.pop()
                    else:
                        return False
                if c == '}':
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        return False

        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = "]"
    print Solution().isValid(s)