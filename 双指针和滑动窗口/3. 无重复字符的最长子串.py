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

    def lengthOfLongestSubstring2(self, s):
        """
        滑动窗口方法
        :param s:
        :return:
        """
        l = 0
        r = 0
        dict = {}
        moveLeft = False
        maxLength = 0

        while r < len(s):
            rightChar = s[r]
            if rightChar in dict:
                dict[rightChar] += 1
            else:
                dict[rightChar] = 1

            if dict[rightChar] > 1:
                moveLeft = True
            while moveLeft:
                if r - l > maxLength:
                    maxLength = r - l

                leftChar= s[l]

                if leftChar in dict:
                    dict[leftChar] -= 1
                l += 1
                moveLeft = False
                for k,v in dict.items():
                    if v > 1:
                        moveLeft = True
                        break
            r += 1

        maxLength = max(maxLength, r - l)
        return maxLength

        pass




if __name__ == '__main__':
    # print Solution().lengthOfLongestSubstring(s="dvdf")
    # print Solution().lengthOfLongestSubstring2("tmmzuxt")
    print Solution().lengthOfLongestSubstring2("abcabcbb")