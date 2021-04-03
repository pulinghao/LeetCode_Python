#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/20 10:33 下午
 @Author  :pulinghao@baidu.com
 @File     :150. 逆波兰表达式求值.py
 @Description :
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for idx, item in enumerate(tokens):
            if item.isdigit():
                stack.append(item)
            else:
                if item == '+':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(str(int(num1) + int(num2)))
                elif item == '-':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(str(int(num2) - int(num1)))
                elif item == '*':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(str(int(num2) * int(num1)))
                elif item == '/':
                    num1 = stack.pop()
                    num2 = stack.pop()
                    stack.append(str(int(num2)/int(num1)))
                else:
                    stack.append(int(item))
        return int(stack.pop())

if __name__ == '__main__':
    tokens = ["4","-2","/","2","-3","-","-"]
    print Solution().evalRPN(tokens)

