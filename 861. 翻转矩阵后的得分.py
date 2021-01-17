#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/7 10:11 下午
 @Author  :pulinghao@baidu.com
 @File     :861. 翻转矩阵后的得分.py
 @Description :
"""

class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        # 1. 先遍历每一行，让每一行的最高位为1
        N = len(A)
        M = len(A[0])
        for i in range(N):
            row = A[i]
            if row[0] == 0:
                # 翻转
                row[0] = 1
                for j in range(1,len(row)):
                    if row[j] == 0:
                        row[j] = 1
                    else:
                        row[j] = 0

        for j in range(M):
            col = []
            cnt0 = 0
            cnt1 = 0
            for i in range(N):
                col.append(A[i][j])
                if A[i][j] == 0:
                    cnt0 += 1
                else:
                    cnt1 += 1
            # 对col中0 和 1 计数，如果0比较多，把0的位置改成1，如果1比较多，就不要改了
            if cnt0 > cnt1:
                for i in range(N):
                    if A[i][j] == 0:
                        A[i][j] = 1
                    else:
                        A[i][j] = 0

        # 3. 将每一行的数据相加
        res = 0
        for j in range(M):
            temp = 0
            for i in range(N):
                temp += A[i][M - j - 1] * (2 ** j)
            res += temp
        return res


if __name__ == '__main__':
    A = [[0,0,1,1],[1,1,0,0]]
    print Solution().matrixScore(A)

