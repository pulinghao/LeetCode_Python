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

    def minWindow2(self,s,t):
        if len(t) > len(s):
            return ""
        l = 0
        r = 0
        dict1 = {}  # 保存t中字符出现的次数
        resLength = sys.maxint
        baseleft = 0
        baseright = 0
        for c in t:
            if c in dict1:
                dict1[c] += 1
            else:
                dict1[c] = 1

        while r < len(s):
            rightChar = s[r]
            if rightChar in dict1:
                dict1[rightChar] -= 1

            allIn = True
            for k,v in dict1.items():
                if v > 0:
                    allIn = False
                    break


            while allIn:
                if resLength > r - l + 1:
                    resLength = r - l + 1
                    baseleft = l
                    baseright = r + 1

                # 移动左侧指针
                leftChar = s[l]
                if leftChar in dict1:
                    dict1[leftChar] += 1
                l += 1

                for k,v in dict1.items():
                    if v > 0:
                        allIn = False
                        break

            r += 1

        return s[baseleft:baseright]


if __name__ == '__main__':
    print Solution().minWindow2(s="ADOBECODEBANC", t="ABC")

    # print Solution().minWindow2(s="a", t="aa")