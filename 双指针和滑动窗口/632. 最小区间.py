#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/1 11:28 下午
 @Author   :pulinghao@baidu.com
 @File     :632. 最小区间.py 
 @Description :
"""
import sys
import collections


class Solution(object):
    def smallestRange(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: List[int]
        """
        N = len(nums)
        dic = collections.defaultdict(list)
        xMin = sys.maxint
        xMax = -sys.maxint
        for i, array in enumerate(nums):
            for x in array:
                dic[x].append(i)
                xMin = min(xMin, x)
                xMax = max(xMax, x)

        window = [0] * N
        inside = 0
        left = xMin
        right = xMin - 1
        bestLeft = xMin
        bestRight = xMax
        while right < xMax:
            right += 1
            if right in dic:
                for x in dic[right]:
                    window[x] += 1
                    if window[x] == 1:
                        inside += 1

                while inside == N:
                    # 移动左侧指针
                    if right - left < bestRight - bestLeft:
                        bestLeft,bestRight = left, right

                    if left in dic:
                        for i in dic[left]:
                            window[i] -= 1
                            if window[i] == 0:
                                inside -= 1

                    left += 1
        return [bestLeft,bestRight]


if __name__ == '__main__':
    print Solution().smallestRange([[4,10,15,24,26], [0,9,12,20], [5,18,22,30]])