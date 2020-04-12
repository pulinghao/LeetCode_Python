#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/9 9:09 下午
 @Author   :pulinghao@baidu.com
 @File     :28. 实现 strStr().py 
 @Description :
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1

        if len(needle) == 0:
            return 0

        count = len(haystack) - len(needle) + 1

        equal = True
        for i in range(count):
            equalIndex = i
            for j in range(len(needle)):
                if haystack[i + j] == needle[j]:
                    equal = True
                    continue
                else:
                    equal = False
                    equalIndex = -1
                    break

            if equal:
                break
            else:
                continue

        return equalIndex




if __name__ == '__main__':
    str1 = "hello"
    str2 = "ll"
    print Solution().strStr(str1,str2)