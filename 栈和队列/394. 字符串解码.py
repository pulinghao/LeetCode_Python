#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/28 8:01 下午
@Author:  pulinghao
@File: 394. 字符串解码.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        prenum = 0
        for c in s:
            if c == ']':
                h = stack.pop(-1)
                temp = ""
                while h != '[':
                    temp += h
                    h = stack.pop(-1)
                newstr = temp[::-1]
                num = int(stack.pop(-1))

                for i in range(num):
                    for newc in newstr:
                        stack.append(newc)
            else:
                if ord(c) >= 48 and ord(c) <= 57:
                    # 另外一种写法
                    # if c in '0123456789':
                    prenum = int(c) + prenum * 10
                elif c == '[':
                    if prenum != 0:
                        stack.append(prenum)
                        stack.append(c)
                        prenum = 0
                else:
                    stack.append(c)
        return ''.join(stack)



if __name__ == '__main__':
    line = "[]"
    out = Solution().decodeString(s = "100[leetcode]")

    print out 