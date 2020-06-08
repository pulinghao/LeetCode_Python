#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/6 1:49 下午
 @Author   :pulinghao@baidu.com
 @File     :17. 电话号码的字母组合.py 
 @Description :
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """


        res = []
        track = []

        if len(digits) == 0:
            return res
        dict = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}

        def backtrack(depth,track):
            if len(track) == len(digits):
                res.append(''.join(track))
                return

            num = digits[depth]
            chars = dict[num]
            for c in chars:
                track.append(c)
                backtrack(depth + 1,track)
                track.pop(-1)

        backtrack(0,track)
        return res



if __name__ == '__main__':
    print Solution().letterCombinations(digits="23")