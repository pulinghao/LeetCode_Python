#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/19 3:03 下午
 @Author   :pulinghao@baidu.com
 @File     :27. 移除元素.py 
 @Description :
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1

        return i




if __name__ == '__main__':
    val = 1
    nums = [1,2,3,4,5]
    ret = Solution().removeElement(nums, val)
    print ret