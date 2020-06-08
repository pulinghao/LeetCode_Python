#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/6 12:54 下午
 @Author   :pulinghao@baidu.com
 @File     :128. 最长连续序列.py 
 @Description :
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        hashset = set(nums)
        ans = 0
        i = 0
        while i < len(nums):
            length = 0
            num = nums[i]
            left_num = num - 1
            right_num = num + 1
            if num in hashset:
                length += 1
                hashset.remove(num)

            while left_num in hashset:
                length += 1
                hashset.remove(left_num)
                left_num -= 1

            while right_num in hashset:
                length += 1
                hashset.remove(right_num)
                right_num += 1

            ans = max(ans, length)
            i += 1

        return ans

if __name__ == '__main__':
    print Solution().longestConsecutive(nums = [100,4,5,7,200,3,2])
