#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/25 5:22 下午
 @Author   :pulinghao@baidu.com
 @File     :1111. 有效括号的嵌套深度.py 
 @Description :
"""

class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        谁的深度浅，就给谁涨深度
        """

        ans = []
        a = b = 0  # 这是深度，初始都是0
        for s in seq:
            if s == '(':
                if a <= b:
                    a += 1
                    ans.append(0)
                else:
                    b += 1
                    ans.append(1)
            elif s == ')':
                if a > b:
                    a -= 1
                    ans.append(0)
                else:
                    b -= 1
                    ans.append(1)
        return ans

