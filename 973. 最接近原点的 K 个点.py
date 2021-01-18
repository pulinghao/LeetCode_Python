#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/11/9 10:48 上午
@Author:  pulinghao
@File: 973. 最接近原点的 K 个点.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        for point in points:
            x = point[0]
            y = point[1]
            dist = (x ** 2 + y ** 2) ** 0.5
            point.append(dist)

        points.sort(key = lambda x : x[2])

        newPoint = points[0:K]
        res = []
        for point in newPoint:
            x = point[0]
            y = point[1]
            res.append([x,y])

        return res

if __name__ == '__main__':
    points =  [[3,3],[5,-1],[-2,4]]
    K = 2

    out = Solution().kClosest(points,K)

    print out
