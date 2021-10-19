#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2021/4/2 9:28 上午
@Author:  pulinghao
@File: 面试题 17.21. 直方图的水量.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        ans = 0
        for i in range(len(height)):
            while stack and height[i] > height[stack[-1]]:
                # 计算雨水高度
                top = stack.pop()
                if not stack:
                    break

                # 获取出栈元素左侧的高度

                left = stack[-1]
                curWidth = i - left - 1
                curHeight = min(height[left],height[i]) - height[top]
                ans += curWidth * curHeight
            stack.append(i)
        return ans



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().func(root)

    print out
