#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/9 10:43 上午
 @Author   :pulinghao@baidu.com
 @File     :5484. 找出第 N 个二进制字符串中的第 K 位.py 
 @Description :
"""

class Solution(object):
    def findKthBit(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        i = 0
        last = [0]
        def invert(s):
            ans = []
            for i in range(len(s)):
                if s[i] == 0:
                    ans.append(1)
                else:
                    ans.append(0)
            return ans

        while i < n - 1:
            res = last[:]
            res.append(1)
            invertLast = invert(last)
            reverseLast = invertLast[::-1]
            res.extend(reverseLast)
            last = res[:]
            i += 1

        return str(last[k - 1])

if __name__ == '__main__':
    print Solution().findKthBit(n = 2, k = 3)