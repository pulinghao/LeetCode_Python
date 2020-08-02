#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/30 11:02 上午
 @Author   :pulinghao@baidu.com
 @File     :a到b间隔k.py 
 @Description :
"""


class Solution(object):
    def sum2(self, a, b, k):
        if a + k > b:
            return b
        else:
            return a + self.sum2(a + k, b, k)

    def recusiveSum(self, a, k, b):
        pass


if __name__ == '__main__':
    print Solution().sum2(1, 10, 3)
