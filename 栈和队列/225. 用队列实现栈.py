#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/6 3:19 下午
 @Author   :pulinghao@baidu.com
 @File     :225. 用队列实现栈.py 
 @Description :
"""

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.queue.append(x)


    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        cnt = len(self.queue)
        while cnt > 1:
            self.queue.append(self.queue.pop(0))
            cnt -= 1
        return self.queue.pop(0)


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        cnt = len(self.queue)
        while cnt > 1:
            self.queue.append(self.queue.pop(0))
            cnt -= 1
        top = self.queue[0]
        self.queue.append(self.queue.pop(0)) #恢复栈的结够
        return top



    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return True if len(self.queue) == 0 else False

if __name__ == '__main__':
    obj = MyStack()
    obj.push(1)
    obj.push(2)
    param_2 = obj.top()
    param_3 = obj.pop()
    param_4 = obj.empty()
    print param_2
    print param_3
    print param_4