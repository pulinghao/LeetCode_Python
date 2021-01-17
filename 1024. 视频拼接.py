#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/10/24 6:38 下午
 @Author  :pulinghao@baidu.com
 @File     :1024. 视频拼接.py
 @Description :
"""


class Solution(object):
    def videoStitching(self, clips, T):
        """
        :type clips: List[List[int]]
        :type T: int
        :rtype: int
        """
        last = pre = ret = 0
        maxn = [0] * T
        for a, b in clips:
            if a < T:
                maxn[a] = max(maxn[a], b)  # 以a为左侧区间，b尽可能大

        for i in range(T):
            last = max(maxn[i], last)
            if i == last:
                return -1
            if pre == i:
                pre = last
                ret += 1
        return ret
