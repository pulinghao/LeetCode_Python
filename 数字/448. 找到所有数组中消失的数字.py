#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/13 9:42 下午
 @Author  :pulinghao@baidu.com
 @File     :448. 找到所有数组中消失的数字.py
 @Description :
"""

class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # 利用不存在的数字，其对应下表位置的数不可能被修改
        for i , num in enumerate(nums):
            if nums[abs(num) - 1] > 0:
                nums[abs(num) - 1] *= -1

        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i + 1)
        return res