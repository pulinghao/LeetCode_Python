#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/15 9:27 下午
 @Author   :pulinghao@baidu.com
 @File     :11. 盛最多水的容器.py 
 @Description :
"""

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        l = 0
        r = len(height) - 1
        res = 0
        while l < r:
            area = min(height[l],height[r]) * (r - l)

            # 当左边比右边小时，移动左边，因为移动右边会造成 r - l的值减小
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

            res = max(area,res)
        return res

if __name__ == '__main__':
    print Solution().maxArea(height=[1,8,6,2,5,4,8,3,7])