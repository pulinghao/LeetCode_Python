#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/26 10:03 下午
 @Author   :pulinghao@baidu.com
 @File     :416. 分割等和子集.py 
 @Description :
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        # 动态规划
        # if sum(nums) % 2 == 1:
        #     return False
        #
        # sums = sum(nums) / 2
        # length = len(nums)
        #
        # dp = [[False] * (sums + 1)] * (length + 1)
        # dp[0][0] = True
        # for i in range(length + 1):
        #     dp[i][0] = True
        #
        # for i in range(1,length + 1):
        #     for j in range(1, sums + 1):
        #         if j - nums[i - 1] < 0:
        #             dp[i][j] = False
        #
        #         else:
        #             dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]
        #
        # return dp[length][sums]
        # 优化版本

        if sum(nums) % 2 == 1:
            return False

        sums = sum(nums) / 2
        length = len(nums)

        dp = [False] * (sums + 1)
        dp[0] = True

        i = 0
        while i < length:
            j = sums
            while j >= 0:
                if j - nums[i] >= 0:
                    dp[j] = dp[j] or dp[j - nums[i]]

                j -= 1
            i += 1
        return dp[sums]
        pass


if __name__ == '__main__':
    print Solution().canPartition(nums=[1,5,11,5])


