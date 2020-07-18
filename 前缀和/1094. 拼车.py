#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/27 1:36 下午
 @Author   :pulinghao@baidu.com
 @File     :1094. 拼车.py 
 @Description :
"""


class Solution(object):
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        N = 1000
        res = [0] * N
        for i in range(len(trips)):
            trip = trips[i]
            people = trip[0]
            start = trip[1]
            end = trip[2]
            res[start - 1] += people
            res[end - 1] -= people

        for i in range(1, N):
            res[i] += res[i - 1]
            if res[i] > capacity:
                return False

        return True


if __name__ == '__main__':
    print Solution().carPooling(trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11)
