#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/2 10:00 下午
 @Author   :pulinghao@baidu.com
 @File     :面试题64. 求1+2+…+n.py 
 @Description :
"""

class Solution(object):
    def quickMulti(self,A,B):
        ans = 0
        while B:
            if B & 1: # B为奇数，保留相加；偶数的话去掉
                ans += A
            A <<= 1
            B >>= 1
        return ans

    def __init__(self):
        self.res = 0
    def sumNums(self, n):
        """
        :type n: int
        :rtype: int
        """
        # 俄罗斯农民乘法,见官方解

        # 利用短路 && 和 ||
        # 这里制造短路，如果n>1，那么会执行后面的部分，如果n=1，那么程序就会继续往下走

        n > 1 and self.sumNums(n - 1)
        self.res += n
        return self.res





if __name__ == '__main__':
    Solution().sumNums(n = 3)