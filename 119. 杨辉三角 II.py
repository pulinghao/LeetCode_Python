#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/12 11:10 下午
 @Author  :pulinghao@baidu.com
 @File     :119. 杨辉三角 II.py
 @Description :
"""


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        res = [1] * (rowIndex + 1)
        for i in range(2, rowIndex + 1):
            for j in range(i - 1,0 ,-1): # 倒着来，否则的话，res的值会变化
                res[j] += res[j - 1]

        return res


if __name__ == '__main__':
    print Solution().getRow(3)
