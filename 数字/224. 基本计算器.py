#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/3/10 6:57 下午
@Author:  pulinghao
@File: 224. 基本计算器.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 1. 先转成数字和运算符
        temp = ''
        group = []
        for c in s:
            if c == '+' or c == '-' or c == '(' or c == ')':
                if len(temp):
                    group.append(temp)
                group.append(c)
                temp = ''
            elif c.isdigit():
                temp += c
        if temp.isdigit():
            group.append(temp)

        # 2. 使用栈
        # 1) 存括号
        stack1 = []
        # 2) 存括号里面的运算
        stack2 = []
        total = 0
        for i in range(len(group)):
            if group[i] != ')':
                stack1.append(group[i])
            else:
                while stack1[-1] != '(':
                    stack2.append(stack1.pop())
                stack1.pop() # 把(去掉
                stack2 = stack2[::-1]
                if stack2[0].isdigit():
                    res = int(stack2[0])
                else:
                    res = 0
                    stack2.insert(0,0)
                for j in range(1,len(stack2)):
                    if stack2[j] == '+':
                        res += int(stack2[j + 1])
                        j += 1
                    elif stack2[j] == '-':
                        res -= int(stack2[j + 1])
                        j += 1
                stack2 = []
                stack1.append(res)

        # 3. 去掉了所有的括号
        if stack1[0] != '-' and stack1[0] != '+':
            res = int(stack1[0])
        else:
            res = 0
            stack1.insert(0,0)
        for j in range(1, len(stack1)):
            if stack1[j] == '+':
                res += int(stack1[j + 1])
                j += 1
            elif stack1[j] == '-':
                res -= int(stack1[j + 1])
                j += 1

        return res





if __name__ == '__main__':
    out = Solution().calculate(s = "(1+(4+5+2)-3)+(6+8)")

    print out
