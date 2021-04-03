#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/21 10:28 下午
 @Author  :pulinghao@baidu.com
 @File     :73. 矩阵置零.py
 @Description :
"""

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        if not matrix or not matrix[0]:
            return
        M = len(matrix)
        N = len(matrix[0])
        row = set()
        col = set()
        for i in range(M):
            for j in range(N):
                if matrix[i][j] == 0:
                    row.add(i)
                    col.add(j)

        for i in range(M):
            for j in range(N):
                if i in row or j in col:
                    matrix[i][j] = 0