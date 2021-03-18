#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/1 11:38 下午
 @Author  :pulinghao@baidu.com
 @File     :888. 公平的糖果棒交换.py
 @Description :
"""


class Solution(object):
    def fairCandSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        delta = (sum(A) - sum(B)) // 2
        rec = set(A)
        for candy in B:
            x = candy + delta
            if x in rec:
                return [x,candy]


if __name__ == '__main__':
    A = [1,2,5]
    B = [2,4]
    print Solution().fairCandSwap(A,B)

