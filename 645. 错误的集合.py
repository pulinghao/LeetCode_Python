#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/2 7:09 下午
@Author:  pulinghao
@File: 645. 错误的集合.py
@Software: PyCharm
"""

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        array = []
        repeat = 0
        loss = 0
        for i in range(10000):
            array.append(0)

        for i in range(len(nums)):
            num = nums[i]
            if array[num - 1] == 0:
                array[num - 1] = 1
            else:
                repeat = num

        for i in range(len(array)):
            if array[i] == 0:
                loss = i
                break

        return [repeat,loss + 1]


if __name__ == '__main__':
    nums = [6,1,2,2,4,5]

    print set(nums)
    print set(range(1,len(nums) + 1)) - set(nums)
    # print Solution().findErrorNums(nums)