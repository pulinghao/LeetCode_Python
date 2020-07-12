#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/12 9:56 上午
 @Author   :pulinghao@baidu.com
 @File     :174. 地下城游戏.py 
 @Description :
"""
import sys


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        N = len(dungeon)
        M = len(dungeon[0])
        #dp[i][j],代表当前格子走到右下角需要的最低血量，依赖后面的路径，与前面的路径无关
        dp = [[sys.maxint for _ in range(M)] for _ in range(N)]

        # 假设只有1 * 1的格子
        if dungeon[-1][-1] < 1:
            # 0或者负数
            dp[-1][-1] = 1 - dungeon[-1][-1]
        else:
            # 大于1的话，只需要1就可以通过了
            dp[-1][-1] = 1

        for i in range(N - 1, -1, -1):
            for j in range(M - 1, -1, -1):
                if i == N - 1 and j == M - 1:
                    # 保证右下角已知
                    dp[i][j] = max(1 - dungeon[-1][-1], 1)
                elif i == N - 1:
                    # 保证最下行已知
                    dp[i][j] = max(1, dp[i][j + 1] - dungeon[i][j])
                elif j == M - 1:
                    # 保证最右列已知
                    dp[i][j] = max(1, dp[i + 1][j] - dungeon[i][j])
                else:
                    dp[i][j] = max(1, min(dp[i + 1][j],dp[i][j + 1]) - dungeon[i][j])

        return dp[0][0]

if __name__ == '__main__':
    print Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]])