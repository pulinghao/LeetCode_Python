#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/11 8:45 下午
 @Author  :pulinghao@baidu.com
 @File     :1202. 交换字符串中的元素.py
 @Description :
"""

import collections
class DisjointSetUnion:
    def __init__(self, n):
        self.n = n
        self.rank = [1] * n
        self.f = list(range(n))

    def find(self, x):
        if self.f[x] == x:
            return x
        self.f[x] = self.find(self.f[x])
        return self.f[x]

    def unionSet(self, x, y):
        fx, fy = self.find(x), self.find(y)
        if fx == fy:
            return

        if self.rank[fx] < self.rank[fy]:
            fx, fy = fy, fx

        self.rank[fx] += self.rank[fy]
        self.f[fy] = fx


class Solution(object):
    def smallestStringWithSwaps(self, s, pairs):
        """
        :type s: str
        :type pairs: List[List[int]]
        :rtype: str
        """
        dsu = DisjointSetUnion(len(s))
        for x, y in pairs:
            dsu.unionSet(x, y)

        mp = collections.defaultdict(list)
        for i,ch in enumerate(s):
            mp[dsu.find(i)].append(ch)

        for vec in mp.values():
            vec.sort(reverse=True)

        ans = list()
        for  i in range(len(s)):
            x = dsu.find(i)
            ans.append(mp[x][-1])
            mp[x].pop()
        return "".join(ans)

if __name__ == '__main__':
    s = "dcab"
    pairs = [[0, 3], [1, 2]]
    print Solution().smallestStringWithSwaps(s,pairs)

