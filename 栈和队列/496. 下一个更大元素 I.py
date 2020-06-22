#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/20 10:36 上午
 @Author   :pulinghao@baidu.com
 @File     :496. 下一个更大元素 I.py 
 @Description :
"""

class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        stack = []
        dict = {}
        res = []
        for i in range(len(nums2)):
            while len(stack) != 0 and nums2[i] > stack[-1]:
                top = stack.pop()
                dict[top] = nums2[i]

            stack.append(nums2[i])

        while len(stack) > 0:
            top = stack.pop()
            dict[top] = -1

        for i in range(len(nums1)):
            value = dict[nums1[i]]
            res.append(value)

        return res


if __name__ == '__main__':
    print Solution().nextGreaterElement(nums1 = [2,4], nums2 = [1,2,3,4])