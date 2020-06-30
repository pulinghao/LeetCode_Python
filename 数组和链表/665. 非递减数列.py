#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/15 5:47 下午
@Author:  pulinghao
@File: 665. 非递减数列.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        ans = True
        cnt = 0
        if len(nums) <= 2:
            return True

        if nums[0] > nums[1]:
            nums[0] = nums[1]
            cnt += 1

        for i in range(1, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                cnt += 1
                if cnt > 1:
                    ans = False
                    break

                if nums[i - 1] > nums[i + 1]:
                    # 左边的数大于右边的数，让右边的数和当前的数相等，说明右边的数最小
                    nums[i + 1] = nums[i]
                else:
                    # 左边的数小于右边的数，右边的数小于中间的数，说明中间的数最大。让中间的数 等于 左边的数
                    nums[i] = nums[i - 1]
        return ans



if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().checkPossibility(nums = [4,2,1])

    print out 