#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/27 10:43 上午
 @Author   :pulinghao@baidu.com
 @File     :1109. 航班预订统计.py 
 @Description :
"""

class Solution(object):
    def corpFlightBookings(self, bookings, n):
        """
        :type bookings: List[List[int]]
        :type n: int
        :rtype: List[int]
        """

        ans = [0] * n
        for i in range(len(bookings)):
            book = bookings[i]
            ans[book[0] - 1] += book[2]
            if book[1] < n:
                ans[book[1]] -= book[2]

        for i in range(1,len(ans)):
            ans[i] += ans[i - 1]

        return ans


if __name__ == '__main__':
    print Solution().corpFlightBookings(bookings = [[1,1,10]], n = 1)