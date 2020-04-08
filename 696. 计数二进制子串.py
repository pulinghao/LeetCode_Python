#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/4/2 2:31 下午
@Author:  pulinghao
@File: 696. 计数二进制子串.py
@Software: PyCharm
"""


class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 以 000011110000为例
        last = 0  # 记录前半部分的数字长度
        cur = 1   # 记录后半部分（不同数字)的长度
        res = 0
        i = 1
        while i < len(s):
            if str(s[i]) != str(s[i - 1]):
                last = cur
                cur = 1
            else:
                cur += 1

            if cur <= last:
                res += 1
            i += 1
        return res


if __name__ == '__main__':
    s = "00110011"
    print Solution().countBinarySubstrings(s)