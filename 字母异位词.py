#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/3/31 9:19 下午
 @Author   :pulinghao@baidu.com
 @File     :字母异位词.py 
 @Description :
"""


class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        #
        # list_s = list(s)
        # list_t = list(t)
        #
        # list_s.sort()
        # list_t.sort()
        #
        # for i in range(len(list_s)):
        #     if list_s[i] != list_t[i]:
        #         return False
        # return True

        # chars_x = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # chars_y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
        # for char in s:
        #     index = int(ord(char) - ord('a'))
        #     chars_x[index] += 1
        #
        # for char in t:
        #     index = int(ord(char) - ord('a'))
        #     chars_y[index] += 1
        #
        #
        # for i in range(len(chars_x)):
        #     if chars_x[i] != chars_y[i]:
        #         return False
        #
        # return True
        chars_x = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(len(s)):
            index_s = ord(s[i]) - ord('a')
            index_t = ord(t[i]) - ord('a')
            chars_x[index_s] += 1
            chars_x[index_t] -= 1

        for x in chars_x:
            if x != 0:
                return False
        return True


    pass


def stringToString(input):
    return input[1:-1].decode('string_escape')


def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = lines.next()
            s = stringToString(line)
            line = lines.next()
            t = stringToString(line)

            ret = Solution().isAnagram(s, t)

            out = (ret)
            print out
        except StopIteration:
            break


if __name__ == '__main__':
    s = "anagram"
    t = "nagaram"
    ret = Solution().isAnagram(s, t)
    print ret
