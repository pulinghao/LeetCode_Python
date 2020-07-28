#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/24 7:58 上午
 @Author   :pulinghao@baidu.com
 @File     :1025. 除数博弈.py 
 @Description :
"""


class Solution(object):
    def divisorGame(self, N):
        """
        :type N: int
        :rtype: bool
        """
        return N % 2 == 0