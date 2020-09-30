#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/9/27 10:51 上午
@Author:  pulinghao
@File: 5524. 经营摩天轮的最大利润.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def minOperationsMaxProfit(self, customers, boardingCost, runningCost):
        """
        :type customers: List[int]
        :type boardingCost: int
        :type runningCost: int
        :rtype: int
        """

        profits = []
        waiters = customers[0]
        roundCnt = 0
        totalUps = 0
        comeCnt = 0
        while waiters > 0 or comeCnt < len(customers):
            if waiters > 4:
                up = 4
                roundCnt += 1
                waiters -= 4
            else:
                roundCnt += 1
                up = waiters
                waiters = 0
            totalUps += up
            profit = totalUps * boardingCost - roundCnt * runningCost
            profits.append(profit)
            comeCnt += 1
            if comeCnt < len(customers):
                waiters += customers[comeCnt]

        ans = max(profits)
        maxIndex = -1
        maxProfit = 0
        if ans < 0:
            return -1
        else:
            for i in range(len(profits)):
                if profits[i] > maxProfit:
                    maxProfit = profits[i]
                    maxIndex = i

        return maxIndex + 1




if __name__ == '__main__':
    customers = [0,43,37,9,23,35,18,7,45,3,8,24,1,6,37,2,38,15,1,14,39,27,4,25,27,33,43,8,44,30,38,40,20,5,17,27,43,11,6,2,30,49,30,25,32,3,18,23,45,43,30,14,41,17,42,42,44,38,18,26,32,48,37,5,37,21,2,9,48,48,40,45,25,30,49,41,4,48,40,29,23,17,7,5,44,23,43,9,35,26,44,3,26,16,31,11,9,4,28,49,43,39,9,39,37,7,6,7,16,1,30,2,4,43,23,16,39,5,30,23,39,29,31,26,35,15,5,11,45,44,45,43,4,24,40,7,36,10,10,18,6,20,13,11,20,3,32,49,34,41,13,11,3,13,0,13,44,48,43,23,12,23,2]

    boardingCost = 43
    runningCost = 54

    out = Solution().minOperationsMaxProfit(customers,boardingCost,runningCost)

    print out
