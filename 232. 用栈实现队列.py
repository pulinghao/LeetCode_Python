#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/6 2:53 下午
 @Author   :pulinghao@baidu.com
 @File     :232. 用栈实现队列.py 
 @Description :
"""


class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.list1 = []
        self.list2 = []

    def push(self, x):
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        while len(self.list2):
            self.list1.append(self.list2.pop())

        self.list1.append(x)
        while len(self.list1):
            self.list2.append(self.list1.pop())

    def pop(self):
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        return self.list2.pop()

    def peek(self):
        """
        Get the front element.
        :rtype: int
        """
        return self.list2[-1]

    def empty(self):
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        return True if len(self.list2) == 0 else False


if __name__ == '__main__':
    obj = MyQueue()
    obj.push(1)
    obj.push(2)
    obj.push(3)
    param_2 = obj.pop()
    param_2 = obj.pop()
    param_3 = obj.peek()
    param_4 = obj.empty()
    print param_2
    print param_3
    print param_4
# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
