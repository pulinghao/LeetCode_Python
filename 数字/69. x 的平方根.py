#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/9 12:03 上午
 @Author   :pulinghao@baidu.com
 @File     :69. x 的平方根.py 
 @Description :
"""

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        # if x == 0:
        #     return 0
        # if x < 4:
        #     return 1
        #
        # half = x / 2
        #
        # i = 0
        # num = 0
        # while i <= x:
        #     num = i ** 2
        #     if num > x:
        #         return i - 1
        #     elif num == x:
        #         return i
        #     i += 1
        #
        # return i
        # 牛顿平方根
        if x <= 0:
            return 0
        cur = 1.0
        while True:
            pre = cur
            cur = (cur + x / cur)/2
            if abs(pre - cur) < 1e-6:
                return int(cur)





if __name__ == '__main__':
    print Solution().mySqrt(x = 8)