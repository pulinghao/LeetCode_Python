#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/6 3:53 下午
 @Author   :pulinghao@baidu.com
 @File     :155. 最小栈.py 
 @Description :
"""
import sys
class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.subStack = []
        self.min = sys.maxint

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x < self.min:
            self.min = x
        self.stack.append(x)

    def pop(self):
        """
        :rtype: None
        """
        value = self.stack.pop()
        if value == self.min:
            self.min = sys.maxint
            while len(self.stack):
                pop = self.stack.pop()
                if pop < self.min:
                    self.min = pop
                self.subStack.append(pop)
            while len(self.subStack):
                self.stack.append(self.subStack.pop())

        return value



    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min



if __name__ == '__main__':
    obj = MinStack()
    obj.push(-2)
    obj.push(0)
    obj.push(-3)
    param_2 = obj.getMin()
    param_3 = obj.pop()
    param_4 = obj.top()
    param_5 = obj.getMin()
    print param_2
    print param_3
    print param_4
    print param_5