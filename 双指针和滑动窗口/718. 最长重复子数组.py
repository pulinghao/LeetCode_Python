#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/1 10:34 上午
@Author:  pulinghao
@File: 718. 最长重复子数组.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def findLength(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        return self.slideWindow(A,B)

    def slideWindow(self,A,B):
        # 滑动窗口方式

        # 方法一，滑动A
        # A始终从0开始取
        # B从i开始一直到len(B)
        res = 0
        if len(A) > len(B):
            A,B = B,A # 让A始终是较短的那个

        for i in range(len(B)):
            length = min(len(B) - i ,len(A))
            res = max(res,self.maxLength(A,B,0,i,length))

        # 滑动B
        for i in range(len(A)):
            length = min(len(A) - i , len(B))
            res = max(res,self.maxLength(A,B,i,0,length))

        return res
        pass

    def maxLength(self,A,B,startA,startB,length):
        """
        :param A: 数组A
        :param B: 数组B
        :param startA: 对齐后，A的开始位置
        :param startB: 对齐后，B的开始位置
        :param length: 结束位置
        :return:
        """
        res = 0
        k = 0
        for i in range(length):
            if A[startA + i] == B[startB + i]:
                k += 1
            else:
                res = max(k,res)
                k = 0
        res = max(k,res)
        return res

if __name__ == '__main__':

    out = Solution().findLength([1,2,3,2,1],[3,2,1,4,7])

    print out 