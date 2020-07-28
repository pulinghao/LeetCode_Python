#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/25 10:39 下午
 @Author   :pulinghao@baidu.com
 @File     :58. 最后一个单词的长度.py 
 @Description :
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        res = ''
        wordList = []
        for c in s:
            if c == ' ':
                if len(res) > 0:
                    wordList.append(res)
                res = ''
            else:
                res += c
        if len(res) > 0:
            wordList.append(res)
        if len(wordList) == 0:
            return 0
        return len(wordList[-1])

if __name__ == '__main__':
    print Solution().lengthOfLastWord(s = " ")