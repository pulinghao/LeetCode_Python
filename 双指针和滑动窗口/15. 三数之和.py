#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/12 2:27 下午
 @Author   :pulinghao@baidu.com
 @File     :15. 三数之和.py 
 @Description :
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        ans = []

        if len(nums) == 0:
            return ans
        if nums[0] > 0 or nums[-1] < 0:
            # 同符号无解
            return ans

        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i - 1]:
                num = nums[i]
                left = i
                right = len(nums) - 1
                while left < right:
                    sum = nums[left] + num + nums[right]
                    if sum == 0:
                        ans.append([nums[left], num, nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            # 这里left - 1，是说当前的这个数字，是否跟前一个相同
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            # 这里right + 1,当前数字是否跟后面那个相同
                            right -= 1
                    elif sum < 0:
                        left += 1
                    else:
                        right -= 1
        return ans

if __name__ == '__main__':
    print Solution().threeSum(nums = [-2,0,1,1,2])