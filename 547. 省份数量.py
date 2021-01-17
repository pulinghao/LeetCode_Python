#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/7 3:44 下午
 @Author  :pulinghao@baidu.com
 @File     :547. 省份数量.py
 @Description :
"""


class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def find(index):
            if parent[index] != index:
                parent[index] = find(parent[index])
            return parent[index]

        def union(index1,index2):
            parent[find(index1)] = find(index2)

        provinces = len(isConnected)
        parent = list(range(provinces))

        for i in range(provinces):
            for j in range(i + 1, provinces):
                if isConnected[i][j] == 1:
                    union(i, j)

        circles = sum(parent[i] == i for i in range(provinces))
        return circles




if __name__ == '__main__':
    isConnected = [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
    print Solution().findCircleNum(isConnected)
