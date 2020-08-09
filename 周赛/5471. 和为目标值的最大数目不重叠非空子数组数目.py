#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/9 11:04 上午
 @Author   :pulinghao@baidu.com
 @File     :5471. 和为目标值的最大数目不重叠非空子数组数目.py 
 @Description :
"""

class Solution(object):
    def maxNonOverlapping(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        N = len(nums)
        preSum = {}
        ans = 0
        sum_i = 0
        preSum[0] = 1
        for i in range(0, N):
            sum_i = sum_i + nums[i]
            sum_j = sum_i - target
            # 将数据重置
            if sum_j in preSum:
                ans += 1
                preSum = {}
                preSum[0] = 1
                sum_i = 0
                continue
            # 这里必须在设置新的前缀和之前
            if sum_i in preSum:
                preSum[sum_i] += 1
            else:
                preSum[sum_i] = 1

        return ans

if __name__ == '__main__':
    #nums= [2, 3, 3, -3, 3, 2, 0, -1, 3, -2], target = 2
    print Solution().maxNonOverlapping(nums = [1,1,1,1,1], target = 2)