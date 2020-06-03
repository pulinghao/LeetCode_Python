#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/2 11:13 下午
 @Author   :pulinghao@baidu.com
 @File     :3. 无重复字符的最长子串.py 
 @Description :
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = set()
        maxLength = 0
        length = 0
        left = 0

        for i in range(len(s)):
            length += 1
            while s[i] in dict:
                dict.remove(s[left])
                left += 1
                length -= 1
            maxLength = max(maxLength,length)
            dict.add(s[i])
        return maxLength





if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring(s="dvdf")
