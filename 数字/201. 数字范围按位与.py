#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/23 9:17 上午
 @Author  :pulinghao@baidu.com
 @File     :201. 数字范围按位与.py
 @Description :
"""

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        res = 0
        # 将m与n不断右移，知道两者相等，取相等的前缀
        while m != n:
            m = m >> 1
            n = n >> 1
            res += 1
        return m << res

if __name__ == '__main__':
    m = 0
    n = 2147483647
    print Solution().rangeBitwiseAnd(m,n)