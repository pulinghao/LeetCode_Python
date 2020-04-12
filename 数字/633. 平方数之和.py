#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/10 10:26 下午
 @Author   :pulinghao@baidu.com
 @File     :633. 平方数之和.py 
 @Description :
"""
import math
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        left = 0
        right = int(math.sqrt(c))
        while left <= right:
            if left ** 2 + right ** 2 == c:
                return True
            elif left ** 2 + right ** 2 > c:
                right -= 1
            else:
                left += 1
        return False
        pass

if __name__ == '__main__':
    c = 3
    print Solution().judgeSquareSum(c)