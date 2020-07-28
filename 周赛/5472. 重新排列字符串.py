#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/26 10:31 上午
 @Author   :pulinghao@baidu.com
 @File     :5472. 重新排列字符串.py 
 @Description :
"""

class Solution(object):
    def restoreString(self, s, indices):
        """
        :type s: str
        :type indices: List[int]
        :rtype: str
        """
        res = ''
        for i in range(len(indices)):
            loc = indices.index(i)
            res += s[loc]

        return res

if __name__ == '__main__':
    print Solution().restoreString(s = "abc", indices = [0,1,2])