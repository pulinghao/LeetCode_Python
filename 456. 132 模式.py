#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/26 11:49 下午
 @Author  :pulinghao@baidu.com
 @File     :456. 132 模式.py
 @Description :
"""

class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False

        N = len(nums)
        leftMin = [float("inf")] * N
        for i in range(1, N):
            # 把左侧最小的数先找出来
            leftMin[i] = min(leftMin[i - 1], nums[i - 1])
        stack = []
        for j in range(N - 1, -1, -1):
            numsk = float("-inf")
            while stack and stack[-1] < nums[j]:
                # 维持一个单调递减栈，弹出小于nums[j]的数
                numsk = stack.pop()
            if leftMin[j] < numsk:
                return True
            stack.append(nums[j])
        return False


if __name__ == '__main__':
    print Solution().find132pattern(nums = [3,1,4,2])