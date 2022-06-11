#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time:  14:50
# @Author:pulinghao
# @File：剑指 Offer 05. 替换空格.py
# @Software: PyCharm


class Solution(object):
    def replaceSpace(self, s):
        """
        :type s: str
        :rtype: str
        这题用Python写不方便，用C++写好
        """
        stringlist = list(s)
        oldSize = len(stringlist)
        count = 0
        for c in s:
            if c == ' ':
                count += 1

        stringlist += ' ' * count * 2
        p2 = len(stringlist) - 1
        p1 = oldSize - 1
        while p1 > -1:
            if stringlist[p1] == ' ':
                stringlist[p2] = '0'
                p2 -= 1
                stringlist[p2] = '2'
                p2 -= 1
                stringlist[p2] = '%'
            else:
                stringlist[p2] = stringlist[p1]
            p1-=1
            p2-=1

        return ''.join(stringlist)


if __name__ == '__main__':
    print Solution().replaceSpace(s='We are Happy')

