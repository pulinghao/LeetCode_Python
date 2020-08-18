#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/16 11:12 上午
 @Author   :pulinghao@baidu.com
 @File     :5489. 两球之间的磁力.py 
 @Description :
"""

import sys


class Solution(object):
    def maxDistance(self, position, m):
        """
        :type position: List[int]
        :type m: int
        :rtype: int
        """

        position.sort()
        if m == 2:
            return abs(position[0] - position[-1])

        # 篮子间的最大间隔
        maxDist = position[-1] - position[0]
        # 篮子间的最小间隔
        minDist = maxDist
        for i in range(1, len(position)):
            minDist = min(minDist, position[i] - position[i - 1])
            pass

        # 二分查找
        left = minDist
        right = maxDist / (m - 1)  # 每两个之间的平均间隔是 最大间隔除以篮子数
        while left <= right:
            mid = left + (right - left) / 2
            if self.check(mid,position,m):
                left = mid + 1
            else:
                right = mid - 1

        return left - 1

    def check(self, mid, array, m):
        cnt = 0
        target = array[0] + mid
        for i in range(len(array) - 1):
            if array[i] < target and array[i + 1] >= target:
                cnt += 1
                target = array[i + 1] + mid

        if cnt >= m - 1:
            return True # 说明mid值偏小了
        else:
            return False





if __name__ == '__main__':
    position = [1,2,3,4,7]
    m = 3
    print Solution().maxDistance(position, m)
