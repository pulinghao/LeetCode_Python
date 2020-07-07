#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/15 9:39 下午
 @Author   :pulinghao@baidu.com
 @File     :1209. 删除字符串中的所有相邻重复项 II.py 
 @Description :
"""


class Solution(object):
    def removeDuplicates(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """

        if len(s) == 0:
            return ""

        if k == 0:
            return s
        stack = []
        i = 0
        while i < len(s):
            if len(stack) == 0:
                cnt = 1
                stack.append([s[i], cnt])
                i += 1
                continue

            top = stack[-1]
            top_value = top[0]
            top_cnt = top[1]
            cnt = 0
            if top_value == s[i]:
                top_cnt += 1
                stack.append([s[i], top_cnt])
                cnt = top_cnt
            else:
                stack.append([s[i], 1])
                cnt = 1

            if cnt == k:
                while cnt > 0:
                    stack.pop()
                    cnt -= 1

            i += 1

        res = []
        for value in stack:
            res.append(value[0])
        return ''.join(res)


if __name__ == '__main__':
    print Solution().removeDuplicates(s="pbbcggttciiippooaais", k=2)
