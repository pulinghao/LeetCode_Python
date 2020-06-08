#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/6 1:38 下午
 @Author   :pulinghao@baidu.com
 @File     :22. 括号生成.py 
 @Description :
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        res = []
        track = []
        def backtrack(left,right,track):
            # left:剩余左括号数
            # right:剩余右括号数
            if right < left:
                return # 不合法，右括号数必须>=左括号数

            if left < 0 or right < 0:
                return # 不合法
            if left == 0 and right == 0:
                str = ''.join(track)
                res.append(str)
                return

            track.append('(')
            backtrack(left - 1, right, track)
            track.pop(-1)

            track.append(')')
            backtrack(left, right - 1, track)
            track.pop(-1)

        backtrack(n,n,track)
        return res

if __name__ == '__main__':
    print Solution().generateParenthesis(n = 3)