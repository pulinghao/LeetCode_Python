#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/19 10:54 下午
 @Author   :pulinghao@baidu.com
 @File     :125. 验证回文串.py 
 @Description :
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip().lower()

        s1 = ""
        for c in s:
            if 97 <= ord(c) <= 122 or 48<= ord(c) <= 57:
                s1 += str(c)

        if len(s1) == 0:
            return True
        left = 0
        right = len(s1) - 1

        res = True
        while left < right:
            if s1[left] != s1[right]:
                res = False
                break
            left += 1
            right -= 1

        return res



if __name__ == '__main__':
    print Solution().isPalindrome(s = "abba")