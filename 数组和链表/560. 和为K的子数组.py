#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/15 11:19 下午
 @Author   :pulinghao@baidu.com
 @File     :560. 和为K的子数组.py 
 @Description :
"""

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 暴利解法，超时
        # res = 0
        # for i in range(len(nums)):
        #     summ = 0
        #     for j in range(i, len(nums)):
        #         summ += nums[j]
        #         if summ == k:
        #             res+= 1
        #
        # return res
    #   前缀和
        presum = 0
        map = {0:1} #必须初始化为{0:1}
        count = 0
        for i in range(len(nums)):
            presum += nums[i]

            if (presum - k) in map:
                count += map[presum - k]

            if presum in map:
                map[presum] += 1
            else:
                map[presum] = 1
        return count

if __name__ == '__main__':
    print Solution().subarraySum(nums = [1,1,1], k = 2)