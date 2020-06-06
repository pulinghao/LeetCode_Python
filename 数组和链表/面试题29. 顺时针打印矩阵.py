#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/5 8:59 下午
 @Author   :pulinghao@baidu.com
 @File     :面试题29. 顺时针打印矩阵.py 
 @Description :
"""

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        res = []
        top = 0
        bottom = len(matrix) - 1
        left = 0
        right = len(matrix[0]) - 1
        while True:
            for i in range(left,right + 1):
                res.append(matrix[top][i])

            top += 1

            if top > bottom:
                break

            for i in range(top,bottom + 1):
                res.append(matrix[i][right])

            right -= 1
            if right < left:
                break

            for i in range(right,left - 1,-1):
                res.append(matrix[bottom][i])

            bottom -= 1

            if bottom < top:
                break

            for i in range(bottom,top - 1, -1):
                res.append(matrix[i][left])

            left += 1
            if left > right:
                break
        return res

if __name__ == '__main__':
    print Solution().spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])