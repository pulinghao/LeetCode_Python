#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/11 10:26 上午
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

        pass
    def lengthOfSub(self,s):
        if len(s) == 0:
            return 0

        subLength = self.lengthOfSub(s[:-1])

        if s in subLength:
            return subLength
        else:
            return subLength + s



if __name__ == '__main__':
    s = "abcabcbb"
    print Solution().lengthOfLongestSubstring(s)