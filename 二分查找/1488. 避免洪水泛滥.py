#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/21 11:19 下午
 @Author   :pulinghao@baidu.com
 @File     :1488. 避免洪水泛滥.py 
 @Description : 贪心算法
"""
import bisect
class Solution(object):
    def avoidFlood(self, rains):
        """
        :type rains: List[int]
        :rtype: List[int]
        """
        n = len(rains)
        rainLakes = {}
        dryDays = []
        ans = [-1] * n

        def find_left(array,value):
            left = 0
            right = len(array) - 1
            while left <= right:
                mid = left + (right - left) / 2
                if array[mid] < value:
                    left = mid + 1
                elif array[mid] > value:
                    right = mid - 1
                else:
                    right = mid - 1

            if left >= len(array):
                return -1
            return left


        for i in range(len(rains)):
            if rains[i] > 0:
                if rains[i] in rainLakes:
                    rainLake = rains[i]
                    index = find_left(dryDays,rainLakes[rainLake])
                    # index = bisect.bisect_left(dryDays,rainLakes[rainLake])
                    if index == -1:
                        return []
                    ans[dryDays[index]] = rains[i]
                    rainLakes[rains[i]] = i
                    dryDays.remove(dryDays[index])
                else:
                    rainLakes[rains[i]] = i
                pass
            else:
                dryDays.append(i)
                ans[i] = 1
        return ans

if __name__ == '__main__':
    print Solution().avoidFlood(rains=[1,2,0,0,2,1])