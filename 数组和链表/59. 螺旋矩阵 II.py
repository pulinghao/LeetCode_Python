#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/16 11:04 下午
 @Author  :pulinghao@baidu.com
 @File     :59. 螺旋矩阵 II.py
 @Description :
"""


class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        N = n * n
        res = [[0 for _ in range(n)] for _ in range(n)]

        top = 0
        right = n
        bottom = n
        left = 0
        i = 1
        while i <= N:
            for j in range(left, right):
                res[top][j] = i
                i += 1

            top += 1
            for j in range(top, bottom):
                res[j][right - 1] = i
                i += 1

            right -= 1
            for j in range(right - 1, left - 1, -1):
                res[bottom - 1][j] = i
                i += 1

            bottom -= 1
            for j in range(bottom - 1, top - 1, -1):
                res[j][left] = i
                i += 1
            left += 1
        return res

if __name__ == '__main__':
    print Solution().generateMatrix(n=4)