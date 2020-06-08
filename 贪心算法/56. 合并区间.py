#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/6 4:51 下午
 @Author   :pulinghao@baidu.com
 @File     :56. 合并区间.py 
 @Description :
"""


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda intv: intv[0])
        res = []
        res.append(intervals[0])

        for i in range(1, len(intervals)):
            last_interval = res[-1]  # 当前的区间
            cur_interval = intervals[i]
            if cur_interval[0] <= last_interval[-1]:
                # 可能这区间就被包含在内，所以要去max
                last_interval[-1] = max(cur_interval[1],last_interval[-1])
            else:
                res.append(intervals[i])
        return res

if __name__ == '__main__':
    print Solution().merge(intervals=[[1,4],[2,3]])
