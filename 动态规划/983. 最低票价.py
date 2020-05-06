#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/6 10:28 下午
 @Author   :pulinghao@baidu.com
 @File     :983. 最低票价.py 
 @Description :
"""


class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        # 初始化dp数组
        dp = [0] * (days[-1] + 1)
        days_idx = 0
        for i in range(1, len(dp)):
            today = days[days_idx]
            if i != today:
                # 不在数组内
                dp[i] = dp[i - 1]
            else:
                dp[i] = min(dp[max(0, i - 1)] + costs[0], dp[max(0, i - 7)] + costs[1], dp[max(0, i - 30)] + costs[2])
                days_idx += 1

        return dp[-1]


if __name__ == '__main__':
    print  Solution().mincostTickets(days=[1, 4, 6, 7, 8, 20], costs=[2, 7, 15])
