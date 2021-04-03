#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/27 10:04 下午
 @Author   :pulinghao@baidu.com
 @File     :33. 搜索旋转排序数组.py 
 @Description :
"""


class Solution(object):
    def __init__(self):
        self.nums = []

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 分治的思想
        self.nums = nums
        left = 0
        right = len(nums) - 1
        if len(nums) == 0:
            return -1

        return self.partion(left, right, target)

    def partion(self, left, right, target):
        if left == right:
            if self.nums[left] == target:
                return left
            else:
                return -1
        else:
            mid = (left + right) / 2
            mid_num = self.nums[mid]

            if target == mid_num:
                return mid

            left_num = self.nums[left]
            right_num = self.nums[right]

            if mid_num >= left_num:
                # 说明左侧是递增序列：
                if left_num <= target < mid_num:
                    # 在左侧找
                    return self.partion(left, mid - 1, target)
                else:
                    # 在右侧找
                    return self.partion(mid + 1, right, target)

            else:
                # 说明右侧是递增序列
                if mid_num < target <= right_num:
                    return self.partion(mid + 1, right, target)
                else:
                    return self.partion(left, mid - 1, target)


if __name__ == '__main__':
    print Solution().search(nums=[3,1], target=1)
