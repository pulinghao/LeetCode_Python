#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/13 1:16 下午
@Author:  pulinghao
@File: 198. 打家劫舍.py
@Software: PyCharm
"""
import leetcode_utils

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        preMax = 0
        curMax = 0

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        res = self.forceRecurse(nums)

        for i in range(len(nums)):
            temp = curMax
            curMax = max(preMax + nums[i],preMax)
            preMax = temp
            pass

        return res

    # 1. 暴力递归
    def forceRecurse(self,nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        return max(self.forceRecurse(nums[:-1]),self.forceRecurse(nums[:-2]) + nums[-1])
        pass

    # 2.备忘录
    def dpRecurse(self,nums):
        preMax = 0
        curMax = 0

        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0], nums[1])


        for i in range(len(nums)):
            temp = curMax
            curMax = max(preMax + nums[i], curMax)
            preMax = temp
            pass
        return curMax



def rob(nums):
    if len(nums) == 0:
        return 0

    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0],nums[1])

    dp = [0 for i in range(len(nums) + 1)]

    dp[0] = 0
    dp[1] = nums[0]
    for i in range(2,len(nums) + 1):
        dp[i] = max(dp[i - 1],nums[i - 1] + dp[i - 2])

    return dp[-1]

    pass
if __name__ == '__main__':
    line = "[2,7,9,3,1]"
    nums = leetcode_utils.stringToIntegerList(line)

    # ret = Solution().rob(nums)
    ret = rob( [1,3,1])
    out = leetcode_utils.intToString(ret)
    print out
