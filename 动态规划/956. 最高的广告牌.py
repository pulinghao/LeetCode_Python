#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/7/27 12:59 下午
@Author:  pulinghao
@File: 956. 最高的广告牌.py
@Software: PyCharm
"""

import leetcode_utils
import copy
import functools


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def tallestBillboard(self, rods):
        """
        :type rods: List[int]
        :rtype: int
        """
        # dp[n][h]: n表示前n个管子，h表示高度差，dp值表示最大公共高度
        #
        # H = sum(rods)
        # dp = [-1 for _ in range(H + 1)]
        # dp[0] = 0
        # for h in rods:
        #     cur = []
        #     for item in dp:
        #         cur.append(item)
        #
        #     for i in range(0, H - h + 1):
        #         if dp[i] < 0:
        #             continue
        #         dp[i + h] = max(dp[i + h], cur[i])
        #         dp[abs(i - h)] = max(dp[abs(i - h)], cur[i] + min(i, h))
        #
        # return dp[0]

        H = sum(rods)
        dp = [[-1 for _ in range(H + 1)] for _ in range(len(rods) + 1)]

        dp[0][0] = 0

        for i in range(1, len(rods)):
            h = rods[i - 1]
            for j in range(0, H - h + 1):
                dp[i][j + rods[i - 1]] = max(dp[i][j + rods[i - 1]], dp[i - 1][j])
                dp[i][abs(j - rods[i - 1])] = max(dp[i][abs(j - rods[i - 1])], dp[i - 1][j] + min(rods[i - 1], j))

        """
        robs = [1,2,3,4,5]
        dp[0][0] = 0
        
        dp[1][0] = -1
        dp[1][1] = -1
        dp[1][2] = -1
        dp[1][3] = -1
        ...
        
        dp[2][0] = 
        """
        return dp[-1][0]
        # s = sum(rods)
        # dp = [-1] * (s + 1)
        # dp[0] = 0
        # for h in rods:
        #     cur = dp[:]  # 不能直接cur=dp，这样相当于引用而不是复制
        #     for i in range(s - h + 1):
        #         if dp[i] < 0:  # 说明当前这个高度差的还没有
        #             continue
        #         dp[i + h] = max(dp[i + h], cur[i])
        #         dp[abs(i - h)] = max(dp[abs(i - h)], cur[i] + min(i, h))
        # return dp[0]


if __name__ == '__main__':
    line = "[]"
    root = leetcode_utils.stringToTreeNode(line)

    out = Solution().tallestBillboard([1, 2, 3, 4, 5])

    print out
