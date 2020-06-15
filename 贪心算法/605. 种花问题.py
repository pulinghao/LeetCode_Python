#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/13 2:42 下午
 @Author   :pulinghao@baidu.com
 @File     :605. 种花问题.py 
 @Description :
"""

class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        i = 0
        cnt = 0
        while i < len(flowerbed):
            if flowerbed[i] == 1:
                i += 1
                continue

            if i == 0:
                pre = 0
            else:
                pre = flowerbed[i - 1]

            if i == len(flowerbed) - 1:
                next = 0
            else:
                next = flowerbed[i + 1]

            if pre == 0 and next == 0:
                flowerbed[i] = 1
                cnt += 1
            i += 1

        return True if cnt >= n else False



if __name__ == '__main__':
    print Solution().canPlaceFlowers(flowerbed = [1,0,0,0,1], n = 1)