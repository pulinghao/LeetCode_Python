#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/5/31 10:13 下午
 @Author   :pulinghao@baidu.com
 @File     :784. 字母大小写全排列.py 
 @Description :
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        res = []
        track = []
        def backtrack(s,track,index):
            if len(track) == len(s):
                trackStr = ''.join(track)
                res.append(trackStr)
                return

            if index == len(s):
                return

            choice = []
            c = s[index]
            if c.isalpha():
                # 1.是字母的话，就有两个选项
                choice.append(c.upper())
                choice.append(c.lower())
            else:
                # 2.是数字的话
                choice.append(c)

            # 3.从选择中选
            for i in range(len(choice)):
                track.append(choice[i])
                backtrack(s,track,index + 1)
                track.pop(-1)

        backtrack(S,track,0)
        return res

if __name__ == '__main__':
    print Solution().letterCasePermutation(S='a1b2')
