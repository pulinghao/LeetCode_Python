#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/28 8:47 下午
 @Author  :pulinghao@baidu.com
 @File     :896. 单调数列.py
 @Description :
"""


class Solution(object):
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) == 1:
            return True

        res = True
        last = A[1] - A[0]
        for i in range(1, len(A)):
            if last == 0:
                last = A[i] - A[i - 1]
                continue
            delta = A[i] - A[i - 1]
            if delta == 0:
                continue
            elif delta * last > 0:
                last = delta
            else:
                res = False
                break

        return res

if __name__ == '__main__':
    A = [1,3,2]
    print Solution().isMonotonic(A)