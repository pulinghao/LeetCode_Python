#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/6 3:56 下午
 @Author   :pulinghao@baidu.com
 @File     :455. 分发饼干.py 
 @Description :
"""

class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """

        if len(g) == 0 or len(s) == 0:
            return 0

        g.sort() # g = sorted(g)
        s.sort() # s = sorted(s)
        i = 0
        j = 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                i += 1
            j += 1

        return i

if __name__ == '__main__':
    print Solution().findContentChildren([10,9,8,7], [5,6,7,8])