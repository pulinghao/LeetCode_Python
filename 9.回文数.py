#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/1 9:20 下午
 @Author   :pulinghao@baidu.com
 @File     :9.回文数.py 
 @Description :
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        z = x
        y = 0
        # 1. x转为数组
        while(x/10 != 0):
            y = x % 10 + y * 10
            x = x/10
        y = x % 10 + y * 10

        if y == z:
            return True
        else:
            return False



    pass


if __name__ == '__main__':
    x = 123321
    print Solution().isPalindrome(x)