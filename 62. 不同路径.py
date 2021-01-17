#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/12/9 10:00 下午
 @Author  :pulinghao@baidu.com
 @File     :62. 不同路径.py
 @Description :
"""
import math
class Solution(object):
    def __init__(self):
        self.res = 0
    def uniquePaths(self, m, n):
        """
            :type m: int
            :type n: int
            :rtype: int
            """

        # def backtrack(x, y, res):
        #     if x == m - 1 and y == n - 1:
        #         self.res += 1
        #
        #     if x > m - 1 or y > n - 1 or x < 0 or y < 0:
        #         return
        #
        #     for i in range(2):
        #         if i == 0:
        #             x = x + 1
        #             backtrack(x, y, res)
        #             x = x - 1
        #         if i == 1:
        #             y = y + 1
        #             backtrack(x, y, res)
        #             y = y - 1
        # res = 0
        # backtrack(0,0,res)
        # return self.res

        # DP方法
        f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        print(f)
        for i in range(1, m):
            for j in range(1, n):
                f[i][j] = f[i - 1][j] + f[i][j - 1]
        return f[m - 1][n - 1]



if __name__ == '__main__':
    print Solution().uniquePaths(m = 3, n = 7)