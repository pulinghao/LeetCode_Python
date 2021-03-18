#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/21 10:25 下午
 @Author  :pulinghao@baidu.com
 @File     :1438. 绝对差不超过限制的最长连续子数组.py
 @Description :
"""


from sortedcontainers import SortedList
class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        res = 0
        left = 0
        right = 0
        curMax = nums[left]
        curMin = nums[left]
        while left < len(nums):
            while abs(curMax - curMin) <= limit and right < len(nums):
                right += 1
                if right < len(nums):
                    if curMax < nums[right]:
                        curMax = nums[right]
                    if curMin > nums[right]:
                        curMin = nums[right]

            # 记录当前的长度
            res = max(right - left, res)
            left += 1
            if left < len(nums):
                right = left
                curMax = nums[left]
                curMin = nums[left]
        return res

    def copyAnswer(self,nums,limit):

        s = SortedList()
        left, right = 0, 0
        res = 0
        while right < len(nums):
            s.add(nums[right])
            while s[-1] - s[0] > limit:
                s.remove(nums[left])
                left += 1
            res = max(res, right - left + 1)
            right += 1
        return res

if __name__ == '__main__':
    nums = [8,2,4,7]
    limit = 4
    s = SortedList()
    s.add(1)
    s.add(4)
    s.add(5)
    s.add(2)
    s.remove(1)
    print s
    print Solution().longestSubarray(nums,limit)
