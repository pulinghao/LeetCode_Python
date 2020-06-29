#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/28 10:59 上午
 @Author   :pulinghao@baidu.com
 @File     :209. 长度最小的子数组.py 
 @Description :
"""


class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 0
        j = 0
        ans = len(nums) + 1  # 这个长度是不存在的，如果等于这个长度，那么返回0
        sum = 0
        while i < len(nums):
            sum += nums[i]
            while sum >= s:
                ans = min(i - j + 1,ans)
                sum -= nums[j]
                if j + 1 < len(nums):
                    j += 1

            i += 1

        return 0 if ans == len(nums) + 1 else ans

if __name__ == '__main__':
    print Solution().minSubArrayLen(s = 3, nums = [1,1])


