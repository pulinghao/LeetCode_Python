#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/9 10:50 下午
 @Author   :pulinghao@baidu.com
 @File     :435. 无重叠区间.py 
 @Description :
"""

class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        if len(intervals) == 0:
            return 0
        # 对第二个进行排序
        intervals.sort(key = lambda x:x[1])
        ans = 0
        end = intervals[0][1]

        for i in range(1,len(intervals)):
            it = intervals[i]
            if it[0] < end:
                ans += 1
            else:
                end = it[1]

        return ans

if __name__ == '__main__':
    print Solution().eraseOverlapIntervals([ [1,2], [2,3], [3,4], [1,3],[2,4]])