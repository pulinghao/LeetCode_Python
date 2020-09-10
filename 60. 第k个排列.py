#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/5 10:50 下午
 @Author  :pulinghao@baidu.com
 @File     :60. 第k个排列.py
 @Description :
"""


class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        def dfs(n, k, index, path):
            if index == n:
                return
            cnt = factorial[n - 1 - index]
            for i in range(1 , n + 1):
                if used[i]:
                    continue
                if cnt < k:
                    k -= cnt
                    continue
                path.append(i)
                used[i] = True
                dfs(n,k,index + 1,path)
                return

        if n == 0:
            return ""

        used = [False] * (n + 1)
        path = []
        factorial = [1] * (n + 1)
        for i in range(2,n + 1):
            factorial[i] = factorial[i - 1] * i
        dfs(n,k,0,path)
        return ''.join([str(num) for num in path])

if __name__ == '__main__':

    print Solution().getPermutation(n = 3, k = 3)