#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/17 7:25 下午
 @Author  :pulinghao@baidu.com
 @File     :566. 重塑矩阵.py
 @Description :
"""

class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """

        N = len(nums)
        M = len(nums[0])
        if r * c != M * N:
            return nums

        temp = []
        for i in range(N):
            for j in range(M):
                temp.append(nums[i][j])
        res = [[0 for i in range(c)] for j in range(r)]
        for i in range(r):
            for j in range(c):
                res[i][j] = temp[i * c + j]

        return res


if __name__ == '__main__':
    nums = [[1,2],[3,4]]
    r = 1
    c = 4
    print Solution().matrixReshape(nums,r,c)
