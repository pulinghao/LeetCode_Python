#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/11 10:44 下午
 @Author   :pulinghao@baidu.com
 @File     :50. Pow(x, n).py 
 @Description :
"""


class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """


        def quickMul(N):
            if N == 0:
                return 1

            y = quickMul(N // 2)

            return y * y if N % 2 == 0 else y * y * x

        return quickMul(n) if n > 0 else 1.0/quickMul(-n)


if __name__ == '__main__':
    print Solution().myPow(x=2, n=-3)
