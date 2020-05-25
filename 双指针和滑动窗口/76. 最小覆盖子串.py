#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/23 10:02 下午
 @Author   :pulinghao@baidu.com
 @File     :76. 最小覆盖子串.py 
 @Description :
"""
import sys

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        left = 0
        right = 0
        res = [sys.maxint, 0, 0] # len ,left ,right

        # need记录 t中相应的字符数
        need = {}
        for c in t:
            if need.has_key(c):
                need[c] += 1
            else:
                need[c] = 1

        # 1.先移动right，找到第一个可行解
        window = {}

        match = 0  # 记录need和window match的次数
        while right < len(s):
            c1 = s[right]
            if need.has_key(c1):
                if window.has_key(c1):
                    window[c1] += 1
                else:
                    window[c1] = 1

                if window[c1] == need[c1]:
                    match += 1

            right += 1

            # 2.如果当前达到了一个可行解,左移左侧指针，直到第一次不满足条件位置
            while match == len(need):
                # 3. 获取符合条件的一个最小值
                if right - left < res[0]:
                    res[0] = right - left
                    res[1] = left
                    res[2] = right
                c2 = s[left]

                if need.has_key(c2):
                    if window.has_key(c2):
                        window[c2] -= 1
                    else:
                        window[c2] = 0

                    if window[c2] < need[c2]:
                        match -= 1

                left += 1

        res_left = res[1]
        res_right = res[2]
        if res_right >= res_left:
            return s[res_left:res_right]
        else:
            return ""

if __name__ == '__main__':
    print Solution().minWindow(s="aaaaaaaaaaaabbbbbcdd", t="abcdd")
