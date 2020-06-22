#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/17 11:47 下午
 @Author   :pulinghao@baidu.com
 @File     :42. 接雨水.py 
 @Description :
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        stack = []
        res = 0
        i = 0
        while i < len(height):
            while len(stack) != 0 and height[i] > height[stack[-1]]:
                idx = stack.pop()
                h = height[idx]
                if len(stack) == 0:
                    break

                delta = min(height[stack[-1]], height[i]) - h
                width = i - stack[-1] - 1
                water = delta * width
                res += water

            stack.append(i)
            i += 1

        return res


if __name__ == '__main__':
    print Solution().trap(height=[2,0,2])
