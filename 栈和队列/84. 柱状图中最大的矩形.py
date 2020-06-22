#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/20 9:34 上午
 @Author   :pulinghao@baidu.com
 @File     :84. 柱状图中最大的矩形.py 
 @Description : 单调栈
"""

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        stack = []
        i = 0
        res = 0
        while i < len(heights):
            while len(stack) != 0 and heights[stack[-1]] > heights[i]:
                top_idx = stack.pop()
                top_height = heights[top_idx]
                # 左侧的索引
                if len(stack) > 0:
                    left_idx = stack[-1]
                    width = i - left_idx - 1
                else:
                    width = i
                # 右侧的索引
                res = max(res, top_height * width)

            stack.append(i)
            i += 1

        # 栈不为空（例如，递增的一个栈）
        while len(stack) > 0:
            top_idx = stack.pop()
            top_height = heights[top_idx]

            # 对于相同的高度，直接弹出栈
            while len(stack) > 0 and heights[stack[-1]] == top_height:
                stack.pop()


            if len(stack) > 0:
                width = len(heights) - 1 - stack[-1]
            else:
                # stack为空的时候，说明弹出了最后一个元素，就是最低的
                width = len(heights)

            res = max(res, top_height * width)

        return res


if __name__ == '__main__':
    print Solution().largestRectangleArea([0,0])