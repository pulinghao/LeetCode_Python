#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/11/4 8:26 下午
 @Author  :pulinghao@baidu.com
 @File     :57. 插入区间.py
 @Description :
"""


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        res = []
        i = 0
        # 1.先找到需要合并的位置
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # 2. 合并区间
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0],intervals[i][0])
            newInterval[1] = max(newInterval[1],intervals[i][1])
            i += 1
        res.append(newInterval)

        while i < len(intervals):
            res.append(intervals[i])
            i += 1

        return res

if __name__ == '__main__':
    intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
    newInterval = [4,8]
    print Solution().insert(intervals,newInterval)