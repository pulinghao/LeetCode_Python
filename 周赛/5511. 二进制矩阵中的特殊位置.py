#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/13 10:34 上午
 @Author  :pulinghao@baidu.com
 @File     :5511. 二进制矩阵中的特殊位置.py
 @Description :
"""


class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        res = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    col_0 = True
                    row_0 = True
                    for k in range(len(mat)):
                        if mat[k][j] != 0 and k != i:
                            row_0 = False
                            break

                    for k in range(len(mat[0])):
                        if mat[i][k] != 0 and k != j:
                            col_0 = False
                            break

                    if col_0 and row_0:
                        res += 1

        return res

if __name__ == '__main__':
    mat = [[0, 0, 0, 0, 0],
           [1, 0, 0, 0, 0],
           [0, 1, 0, 0, 0],
           [0, 0, 1, 0, 0],
           [0, 0, 0, 1, 1]]
    print Solution().numSpecial(mat)