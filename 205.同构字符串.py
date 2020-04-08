#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/1 9:39 下午
 @Author   :pulinghao@baidu.com
 @File     :205.同构字符串.py 
 @Description :
"""


class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        # 利用map,保存这两个键值对
        map = {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            if map.has_key(s[i]):
                if map[s[i]] == t[i]:
                    continue
                else:
                    return False
            else:
                if t[i] in map.values():
                    return False
                else:
                    map[s[i]] = t[i]

        return True


if __name__ == '__main__':
    s = "ab"
    t = "aa"
    print Solution().isIsomorphic(s, t)
