#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/12/4 2:50 下午
@Author:  pulinghao
@File: 659. 分割数组为连续子序列.py
@Software: PyCharm
"""

import leetcode_utils
import collections

class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def isPossible(self, nums):
        nc = collections.defaultdict(int)
        tail = collections.defaultdict(int)
        for num in nums:
            nc[num] += 1
            tail[num] = 0

        for k in nums:
            if nc[k] == 0:
                continue
            elif nc[k] > 0 and tail[k - 1] > 0:
                nc[k] -= 1
                tail[k - 1] -= 1
                tail[k] += 1
            elif nc[k] > 0 and nc[k + 1] > 0 and nc[k + 2] > 0:
                # 初始情况
                nc[k] -= 1
                nc[k + 1] -= 1
                nc[k + 2] -= 1
                tail[k + 2] += 1
            else:
                return False
        return True
        pass


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4, 5]
    out = Solution().isPossible(nums)

    print out
