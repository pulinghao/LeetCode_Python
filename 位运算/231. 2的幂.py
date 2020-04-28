#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/28 9:46 下午
 @Author   :pulinghao@baidu.com
 @File     :231. 2的幂.py 
 @Description :
"""

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        # 位运算 x & (x - 1) 清除最低位的1

        if n < 0:
            return False

        if n & (n - 1) == 0:
            return True
        return False

        # 方法二 x & (-x) 返回最右侧的1
        # return n > 0 && ( n & -n) == n

if __name__ == '__main__':
    print Solution().isPowerOfTwo(n = 2)