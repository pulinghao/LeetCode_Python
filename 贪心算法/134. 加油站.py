#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/16 11:13 下午
 @Author   :pulinghao@baidu.com
 @File     :134. 加油站.py 
 @Description :
"""

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        cur = 0
        total = 0
        p = 0

        for i in range(len(gas)):
            cur += gas[i] - cost[i]
            total += gas[i] - cost[i]
            if cur < 0:
                cur = 0
                p = i + 1

        return p if total >= 0 else -1

if __name__ == '__main__':
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    print Solution().canCompleteCircuit(gas , cost)

