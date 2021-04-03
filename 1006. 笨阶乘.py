#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/4/1 11:24 下午
 @Author  :pulinghao@baidu.com
 @File     :1006. 笨阶乘.py
 @Description :
"""


class Solution(object):
    def clumsy(self, N):
        """
        :type N: int
        :rtype: int
        """
        op = 0
        stack = [N]
        for i in range(N - 1, 0, -1):
            if op == 0:
                stack.append(stack.pop() * i)
            elif op == 1:
                stack.append(int(stack.pop() / float(i)))
            elif op == 2:
                stack.append(i)
            elif op == 3:
                stack.append(-i)
            op = (op + 1) % 4
        return sum(stack)


if __name__ == '__main__':
    N = 7
    print Solution().clumsy(N)

