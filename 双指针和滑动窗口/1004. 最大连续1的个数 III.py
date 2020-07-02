#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/6/30 8:47 下午
@Author:  pulinghao
@File: 1004. 最大连续1的个数 III.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        if len(A) < 1:
            return 0

        left = 0
        right = 0
        res = 0
        change = 0
        while right < len(A):
            if A[right] == 0:
                change += 1
            while change > K: # 这里用if也可以，其实是两个指针一起移动，right - left + 1的值不会变化
                if A[left] == 0:
                    # 当左指针为0时，向右滑动后，change - 1，就不需要变一个0了
                    change -= 1
                left += 1

            res = max(right - left + 1,res)
            right += 1
        return res

if __name__ == '__main__':
    out = Solution().longestOnes(A = [1,1,1,0,0,0,1,1,1,1,0], K = 2)

    print out 