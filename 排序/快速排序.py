#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/5/29 3:25 下午
@Author:  pulinghao
@File: 快速排序.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def quickSort(self,nums,left,right):
        if left < right:
            index = nums[left]

            self.quickSort(nums,left,)


        pass


    def quick(self,nums,begin,end):
        if begin >= end:
            return

        index = nums[begin]  # 基准数
        left = begin + 1
        right = end
        while left <= right:
            while left < len(nums) and nums[left] <= index:
                left += 1

            while right > -1 and nums[right] >= index:
                right -= 1

            if left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1

        nums[left - 1],nums[begin] = nums[begin],nums[left - 1]  # 这儿是跟基准数的位置交换
        px = left - 1

        self.quick(nums,begin,px - 1)
        self.quick(nums,px + 1,end)

        return nums



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)
    nums = [7,6,5,4,4,3,2,1]
    nums2 = [3, 7, 5, 4, 6, 2, 1]
    nums3 = [1,2,3,4,5,6,7]
    nums4 = [2,1]
    out = Solution().quick(nums4,0,len(nums4) - 1)

    print out 