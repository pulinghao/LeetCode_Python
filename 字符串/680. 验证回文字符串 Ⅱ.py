#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/19 11:10 下午
 @Author   :pulinghao@baidu.com
 @File     :680. 验证回文字符串 Ⅱ.py 
 @Description :
"""

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        def search(s, times):
            begin = 0
            end = len(s) - 1

            while begin < end:
                if s[begin] != s[end]:
                    if times == 0:
                        return False
                    else:
                        # 去掉左边或者右边，有一个是回文串即可
                        return search(s[begin:end], times - 1) or search(s[begin + 1:end + 1], times - 1)
                begin += 1
                end -= 1
            return True

        return search(s,1)

if __name__ == '__main__':
    print Solution().validPalindrome(s="cbbaa")