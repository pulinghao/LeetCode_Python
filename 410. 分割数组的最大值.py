#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/25 9:28 下午
 @Author   :pulinghao@baidu.com
 @File     :410. 分割数组的最大值.py 
 @Description :
"""

class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """

        if len(nums) == m:
            return max(nums)

        left = max(nums)
        right = sum(nums)

        while left < right:
            mid = left + (right - left) / 2

            tempSum = 0
            cnt = 1 # 初始值为1，

            for num in nums:
                tempSum += num
                if tempSum > mid:
                    cnt += 1
                    tempSum = num

            # 比较子数组的数量，是否为m
            if cnt > m:
                # 数量大于m，说明设置的mid值偏小了，右移mid值
                left = mid + 1
            else:
                right = mid

        return left

if __name__ == '__main__':
    nums = [7, 2, 5, 10, 8]
    m = 2
    print Solution().splitArray(nums,m)