#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/22 7:25 上午
 @Author   :pulinghao@baidu.com
 @File     :剑指 Offer 11. 旋转数组的最小数字.py 
 @Description :
"""

class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers) - 1

        while left < right:
            mid = left + (right - left) / 2
            if numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] > numbers[right]:
                left = mid + 1
            else:
                right = right - 1
        return numbers[left]


if __name__ == '__main__':
    print Solution().minArray([3,1,3])