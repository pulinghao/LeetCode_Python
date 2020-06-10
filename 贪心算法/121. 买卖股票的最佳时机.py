#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/10 10:42 下午
 @Author   :pulinghao@baidu.com
 @File     :121. 买卖股票的最佳时机.py 
 @Description :
"""
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        minPrice = sys.maxint
        maxPofit = 0

        for i in range(len(prices)):
            if prices[i] < minPrice:
                # 记录当前日期下，价格的最小值
                minPrice = prices[i]
            else:
                # 保存最大利润
                maxPofit = max(maxPofit,prices[i] - minPrice)
        return maxPofit

if __name__ == '__main__':
    print Solution().maxProfit([7,1,5,3,6,4])