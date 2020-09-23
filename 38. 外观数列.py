#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/9/12 11:11 下午
 @Author  :pulinghao@baidu.com
 @File     :38. 外观数列.py
 @Description :
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"

        last = self.countAndSay(n - 1)
        count = 1

        res = ''
        for i in range(len(last)):
            if i + 1 < len(last) and last[i] == last[i + 1] :
                count += 1
            else:
                res += str(count) + last[i]
                count = 1


        return res

if __name__ == '__main__':
    print Solution().countAndSay(n = 5)