#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/2 10:20 下午
 @Author  :pulinghao@baidu.com
 @File     :424. 替换后的最长重复字符.py
 @Description :
"""
import collections


class Solution(object):
    def characterReplacement(self, s, k):
        left = 0
        right = 0
        res = 0
        dic = collections.defaultdict(int)
        while right < len(s):
            char = s[right]
            dic[char] += 1
            res = max(res, dic[char])
            if right - left + 1 > res + k:
                dic[s[left]] -= 1
                left += 1
            right +=1

        return right - left

        pass


if __name__ == "__main__":
    s = "AABABBA"
    k = 1
    print Solution().characterReplacement(s, k)
