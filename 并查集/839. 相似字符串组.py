#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/1/31 8:41 下午
 @Author  :pulinghao@baidu.com
 @File     :839. 相似字符串组.py
 @Description :
"""

class Solution(object):
    def numSimilarGroups(self, strs):
        """
        :type strs: List[str]
        :rtype: int
        """
        n = len(strs)
        f = list(range(n))

        def find(x):
            if f[x] == x:
                return x
            f[x] = find(f[x])
            return f[x]

        def check(a, b):
            num = 0
            for ac, bc in zip(a, b):
                if ac != bc:
                    num += 1
                    if num > 2:
                        return False
            return True

        for i in range(n):
            for j in range(i + 1, n):
                fi, fj = find(i), find(j)
                if fi == fj:
                    continue
                if check(strs[i], strs[j]):
                    f[fi] = fj

        ret = sum(1 for i in range(n) if f[i] == i)
        return ret

if __name__ == '__main__':
    strs = ["tars", "rats", "arts", "star"]
    print Solution().numSimilarGroups(strs)