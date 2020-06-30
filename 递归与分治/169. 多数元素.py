#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/27 4:56 下午
 @Author   :pulinghao@baidu.com
 @File     :169. 多数元素.py 
 @Description :
方法一： 分治 一个数如果是众数，那么肯定也是左半部分或者右半部分的众数
方法二：排序 再取 n/2 位置处的数

"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def partion(l, r):
            if l == r:
                return nums[l]

            mid = l + (r - l) / 2

            # 分治，分别统计两边的次数
            left_num = partion(l, mid)
            right_num = partion(mid + 1, r)

            if left_num == right_num:
                return left_num

            left_count = 0
            right_count = 0
            for i in range(l, r + 1):
                if nums[i] == left_num:
                    left_count += 1

            for i in range(l, r + 1):
                if nums[i] == right_num:
                    right_count += 1

            return left_num if left_count > right_count else right_num

        return partion(0, len(nums) - 1)


if __name__ == '__main__':
    print Solution().majorityElement(nums=[1, 1, 2])
