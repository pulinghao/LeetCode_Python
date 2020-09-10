#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/29 11:40 下午
 @Author  :pulinghao@baidu.com
 @File     :KMP算法.py.py
 @Description :
"""


class Solution:
    def getNext(self, T):
        """
        构造next数组
        :param T:
        :return:
        """
        i = 0
        j = -1
        next_val = [-1] * len(T)
        while i < len(T) - 1:
            if j == -1 or T[i] == T[j]:
                i += 1
                j += 1
                # next_val[i] = j
                if i < len(T) and T[i] != T[j]:
                    next_val[i] = j
                else:
                    next_val[i] = next_val[j]
            else:
                j = next_val[j]
        return next_val


    def KMP(self, S , T):
        """

        :param s: 待匹配的串
        :param p: 模式串
        :return:
        """
        i = 0
        j = 0
        next = self.getNext(T)
        while i < len(S) and j < len(T):
            if j == -1 or S[i] == T[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        if j == len(T):
            return i - j
        else:
            return -1


if __name__ == '__main__':
    S = 'BXBABBABABAAABABAAA'
    T = 'ABABAAABABAA'
    print Solution().KMP(S,T)