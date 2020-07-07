#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/3 1:55 下午
 @Author   :pulinghao@baidu.com
 @File     :前缀和的基本框架.py 
 @Description :
"""


class PrefixSum(object):
    def fuc1(self, nums):
        N = len(nums)
        preSum = [0] * (N + 1)
        preSum[0] = 0
        for i in range(len(nums)):
            preSum[i + 1] = preSum[i] + nums[i]

        return preSum

    def subArray(self, nums, k):
        N = len(nums)
        sum = [0] * (N + 1)
        for i in range(len(nums)):
            sum[i + 1] = nums[i] + sum[i]

        ans = 0
        for i in range(1, N + 1):
            for j in range(0, i):
                if sum[i] - sum[j] == k:
                    ans += 1

        return ans

    def goodPrefixSum(self,nums,k):
        N = len(nums)
        preSum = {}
        ans = 0
        sum_i = 0
        preSum[0] = 1

        for i in range(0, N):
            sum_i = sum_i + nums[i]
            sum_j = sum_i - k
            # 这里必须在设置新的前缀和之前
            if sum_j in preSum:
                ans += preSum[sum_j]

            if sum_i in preSum:
                preSum[sum_i] += 1
            else:
                preSum[sum_i] = 1



        return ans


if __name__ == '__main__':
    print PrefixSum().goodPrefixSum(nums=[1],k = 0)
