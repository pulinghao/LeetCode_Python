#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/21 10:32 上午
 @Author   :pulinghao@baidu.com
 @File     :5440. 数组异或操作.py 
 @Description : 194周赛
"""

class Solution(object):
    def xorOperation(self, n, start):
        """
        :type n: int
        :type start: int
        :rtype: int
        """

        i = 0
        ans = start
        while i < n:
            if i == 0:
                i += 1
                continue
            ans ^= start + 2 * i
            i += 1
        return ans

if __name__ == '__main__':
    print Solution().xorOperation(n = 5, start = 0)