#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/25 10:22 下午
 @Author   :pulinghao@baidu.com
 @File     :49. 字母异位词分组.py 
 @Description :
"""

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        dict = {}
        for s in strs:
            key = ''.join(sorted(s))
            if key in dict.keys():
                dict[key].append(s)
            else:
                dict[key] = [s]

        res = []
        for k,v in dict.items():
            res.append(v)
        return res

if __name__ == '__main__':
    print Solution().groupAnagrams(strs=["eat", "tea", "tan", "ate", "nat", "bat"])