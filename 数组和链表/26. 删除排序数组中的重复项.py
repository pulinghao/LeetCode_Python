#!/usr/bin/env python
# _*_coding:utf-8 _*_
# coding=utf8
"""
 @Time     :2020/6/29 11:22 下午
 @Author   :pulinghao@baidu.com
 @File     :26. 删除排序数组中的重复项.py 
 @Description :
 快慢指针
"""


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        i = 0  # 保存不重复的
        for j in range(1, len(nums)):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]

        return i + 1


if __name__ == '__main__':
    print Solution().removeDuplicates(nums=[0, 0, 1, 1, 1, 2, 2, 3, 3, 4])
