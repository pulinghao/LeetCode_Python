#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/29 10:07 下午
 @Author   :pulinghao@baidu.com
 @File     :96. 不同的二叉搜索树.py 
 @Description :
"""

class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(2 , n + 1):
            # 以某个数值 i 为节点的情况下，
            for j in range(1, i + 1):
                # 内层循环， 左侧子树的数量（从0个节点数到j-1个） * 右侧子树的数量（从j + 1个数到 i 个）
                dp[i] += dp[j - 1] * dp[i - j]
                # 采用累加的方式，是因为只算了第i个节点作为根节点的数量

        return dp[n]





if __name__ == '__main__':
    print Solution().numTrees(3)