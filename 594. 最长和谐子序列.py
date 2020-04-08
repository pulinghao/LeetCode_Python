#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/5 4:11 下午
 @Author   :pulinghao@baidu.com
 @File     :594. 最长和谐子序列.py 
 @Description :
"""


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict = {}
        for i in range(len(nums)):
            if dict.has_key(nums[i]):
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        listmax = 0
        for key in dict.keys():
            num_1 = 0
            if dict.has_key(key + 1):
                num_1 = dict[key + 1]
                number = num_1 + dict[key]
            else:
                number = 0
            listmax = max(listmax, number)
        return listmax


if __name__ == '__main__':
    nums = [1,1,1,1]
    print Solution().findLHS(nums)
