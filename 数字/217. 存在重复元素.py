#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/5 4:34 下午
 @Author   :pulinghao@baidu.com
 @File     :217. 存在重复元素.py 
 @Description :
"""

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        dict = {}
        for num in nums:
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1

        for value in dict.values():
            if value > 1:
                return True

        return False


if __name__ == '__main__':
    nums = [1,1,1,3,3,4,3,2,4,2]
    print Solution().containsDuplicate(nums)