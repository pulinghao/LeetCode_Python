#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/1 12:02 上午
 @Author  :pulinghao@baidu.com
 @File     :486. 预测赢家.py
 @Description :
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        one = []
        two = []
        while len(nums) > 0:
            if nums[0] > nums[-1]:
                one.append(nums[0])
                nums.pop(0)
            else:
                one.append(nums[-1])
                nums.pop(-1)

            if len(nums) > 0:
                if nums[0] > nums[-1]:
                    two.append(nums[0])
                    nums.pop(0)
                else:
                    two.append(nums[-1])
                    nums.pop(-1)

        oneres = sum(one)
        twores = sum(two)
        if oneres > twores:
            return True
        else:
            return False

if __name__ == '__main__':
    print Solution().PredictTheWinner([1, 5, 233, 7])