#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/14 7:30 下午
 @Author   :pulinghao@baidu.com
 @File     :136. 只出现一次的数字.py 
 @Description :
 你的算法应该具有线性时间复杂度。 你可以不使用额外空间来实现吗？

"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1:
            return nums[0]
        a = nums[0]

        for i in range(1, len(nums)):
            a = a ^ nums[i]
        return a


if __name__ == '__main__':
    print Solution().singleNumber(nums=[4,1,2,1,2])
