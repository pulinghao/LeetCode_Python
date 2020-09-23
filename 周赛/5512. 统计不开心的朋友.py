#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/13 11:02 上午
 @Author  :pulinghao@baidu.com
 @File     :5512. 统计不开心的朋友.py
 @Description :
"""

import collections
class Solution(object):
    def unhappyFriends(self, n, preferences, pairs):
        """
        :type n: int
        :type preferences: List[List[int]]
        :type pairs: List[List[int]]
        :rtype: int
        """

        cnt = 0
        pairDict = {}
        relateDict = {}
        for i in range(len(pairs)):
            pair = pairs[i]
            x = pair[0]
            y = pair[1]
            pairDict[x] = y
            pairDict[y] = x

        for i in range(len(preferences)):
            preference = preferences[i]
            relateDict[i] = preference

        for i in range(n):
            friend = pairDict[i]
            relatex = relateDict[i]
            if relatex[0] == friend:
                continue
            else:
                cnt += 1

        return cnt

if __name__ == '__main__':
    n = 4
    preferences = [[1,3,2],[2,3,0],[1,0,3],[1,0,2]]
    pairs = [[2,1],[3,0]]
    # pairs = [[0, 1], [2, 3]]
    print Solution().unhappyFriends(n,preferences,pairs)


