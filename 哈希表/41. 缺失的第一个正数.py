#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/27 10:16 上午
 @Author   :pulinghao@baidu.com
 @File     :41. 缺失的第一个正数.py 
 @Description :
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        把1 映射到 0，2映射到1……，找到第一个映射关系不是f(n) = n - 1的数
        缺失的正整数范围肯定在[1,len(nums)]内
        """

        for i in range(len(nums)):
            while nums[i] >= 1 and nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # 缺失的正整数范围肯定在[1,len(nums)]内，所以用nums[i] <= len(nums)筛选
                # nums[i] != nums[nums[i] - 1这个避免重复计算
                temp = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = temp

        for i in range(len(nums)):
            # 第一个不满足索引 - 1关系的数
            if nums[i] - 1!= i:
                return i + 1

        # 如果本来的顺序就是1，2，3...N，返回N + 1
        return len(nums) + 1


if __name__ == '__main__':
    print Solution().firstMissingPositive([1,2,0])
