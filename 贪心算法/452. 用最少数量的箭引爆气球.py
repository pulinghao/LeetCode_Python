#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/9 10:28 下午
 @Author   :pulinghao@baidu.com
 @File     :452. 用最少数量的箭引爆气球.py 
 @Description :
"""


class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        if len(points) == 0:
            return 0
        # 1.对这些气球的end排序
        points.sort(key=lambda x: x[1])

        ans = 1
        end = points[0][1]

        for point in points:
            # 如果下个区间小于当前的最小end，那么需要新的箭
            if point[0] > end:
                ans += 1
                end = point[1]

        return ans


if __name__ == '__main__':
    print Solution().findMinArrowShots(points=[[10, 16], [2, 8], [1, 6], [7, 12]])
