#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/16 10:42 上午
 @Author   :pulinghao@baidu.com
 @File     :5488. 使数组中所有元素相等的最小操作数.py 
 @Description :
"""

class Solution(object):
    def minOperations(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr = []
        for i in range(n):
            arr.append(2 * i + 1)

        if n == 1:
            return 0
        mid = (arr[0] + arr[-1]) / 2
        ans = 0
        i = 0
        while arr[i] <= mid:
            ans += mid - arr[i]
            i += 1
        return ans

if __name__ == '__main__':
    n = 2
    print Solution().minOperations(n)