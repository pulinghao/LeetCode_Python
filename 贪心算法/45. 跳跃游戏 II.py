#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/12 10:54 下午
 @Author  :pulinghao@baidu.com
 @File     :45. 跳跃游戏 II.py
 @Description :
"""


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxPos = 0 # 当前到达的最大边界
        end = 0
        step = 0
        for i in range(len(nums) - 1):
            if i <= maxPos:
                maxPos = max(maxPos, nums[i] + i) #取跳得最远的那个
                if i == end:
                    end = maxPos # 更新边界
                    step += 1

        return step

if __name__ == '__main__':
    print Solution().jump([2,3,1,1,4])