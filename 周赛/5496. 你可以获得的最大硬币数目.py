#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/24 11:08 下午
 @Author  :pulinghao@baidu.com
 @File     :5496. 你可以获得的最大硬币数目.py
 @Description :
"""


class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        # 1.每次取出最大的两个，和最小的1个
        # 2.取中间的那个
        piles.sort(reverse = True)
        res = 0
        for i in range(len(piles) / 3):
            idx = i * 2 + 1
            res += piles[idx]
        return res

if __name__ == '__main__':
    piles = [2,4,5]
    print Solution().maxCoins(piles)