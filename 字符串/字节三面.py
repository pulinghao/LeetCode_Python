#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/3/16 9:15 下午
 @Author  :pulinghao@baidu.com
 @File     :字节三面.py
 @Description : 在字符串s1中删除所有在s2中出现的字符
"""


class Solution:
    def removeS2InS2(self, s1, s2):
        s2dict = {}
        for c in s2:
            if c in s2dict.keys():
                continue
            else:
                s2dict[c] = 1
        # 1. 双指针
        s1array = list(s1)
        for i in range(len(s1array)):
            if s1array[i] in s2dict.keys():
                s

                    break
        return s1[:i]

        pass


if __name__ == '__main__':
    s1 = "Hello World"
    s2 = "aol"
    out = Solution().removeS2InS2(s1, s2)
    print out