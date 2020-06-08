#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/3/30 9:26 下午
 @Author   :pulinghao@baidu.com
 @File     :main.py 
 @Description :
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)):
        #     left = nums[i]
        #     for j in range(len(nums)):
        #         right = nums[j]
        #         if i == j:
        #             continue
        #         if left + right == target:
        #             return (i,j)
        #
        #     pass
        map = {}
        for index, num in enumerate(nums):
            another_num = target - num
            if another_num in map:
                return [map[another_num], index]
            map[num] = index

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        # 1. 排序
        nums.sort()
        for i in range(len(nums) - 2):
            if nums[i] > 0: #后面的数都大于0,跳过循环
                break
            if i == 0 or nums[i] > nums[i-1]:
                left = i + 1
                right = len(nums) - 1
                if nums[i] + nums[left] + nums[left + 1] > 0 or nums[i] + nums[right] + nums[right - 1] < 0:
                    continue

                while left < right:
                    ident = nums[i] + nums[left] + nums[right]
                    if ident == 0:
                        result.append([nums[i],nums[left],nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                    elif ident < 0:
                        left += 1
                    else:
                        right -=1
        return result

        pass

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """



if __name__ == '__main__':
    solv = Solution()

    # print solv.twoSum([2,7,11, 15], 9)
    print solv.threeSum([-1,0,1,2,-1,-4])
