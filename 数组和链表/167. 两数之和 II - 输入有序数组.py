#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/10 10:15 下午
 @Author   :pulinghao@baidu.com
 @File     :167. 两数之和 II - 输入有序数组.py 
 @Description :
"""

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left <= right:
            if numbers[left] + numbers[right] > target:
                right -= 1
            elif numbers[left] + numbers[right] < target:
                left += 1
            else:
                return left + 1,right + 1

        pass

if __name__ == '__main__':
    numbers = [2]
    target = 2
    print Solution().twoSum(numbers,target)