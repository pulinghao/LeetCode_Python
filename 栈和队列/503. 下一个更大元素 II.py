#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/6 9:34 下午
 @Author  :pulinghao@baidu.com
 @File     :503. 下一个更大元素 II.py
 @Description :
"""

class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [-1] * N
        stack = []
        for i in range(N * 2):
            while stack and nums[stack[-1]] < nums[i % N]:
                # 栈顶元素 小于 入栈的元素时，弹出
                res[stack.pop()] = nums[i % N]
            stack.append(i % N)

        return res


if __name__ == '__main__':
    print Solution().nextGreaterElements([6,5,4,3,8])