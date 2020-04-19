#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/17 11:49 下午
 @Author   :pulinghao@baidu.com
 @File     :213. 打家劫舍 II.py 
 @Description :
"""
import leetcode_utils

class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        res = self.rob1(nums[:-1])
        res2 = self.rob1(nums[1:])
        return max(res,res2)



    def rob1(self,nums):
        if len(nums) == 0:
            return 0

        if len(nums) == 1:
            return nums[0]

        if len(nums) == 2:
            return max(nums[0],nums[1])

        preMax = 0
        curMax = 0
        for i in range(len(nums)):
            temp = curMax
            curMax = max(preMax + nums[i],curMax)
            preMax = temp
        return curMax


if __name__ == '__main__':
    line = "[1,2,3,1]"
    nums = leetcode_utils.stringToIntegerList(line)

    ret = Solution().rob(nums)

    out = leetcode_utils.intToString(ret)
    print out