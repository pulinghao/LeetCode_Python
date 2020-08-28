#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/26 12:03 上午
 @Author  :pulinghao@baidu.com
 @File     :17. 电话号码的字母组合.py
 @Description :
"""

dict = {'1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'qprs', '8': 'tuv',
                '9': 'wxyz'}

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        res = []
        if len(digits) == 0:
            return res
        path = []
        self.dfs(digits,path,res,0)
        return res

    def dfs(self, digits, path, res, idx):

        if idx == len(digits):
            ans = path[:]
            res.append(''.join(ans))
            return

        key = digits[idx]
        value = dict[str(key)]
        for digit in value:
            path.append(digit)
            self.dfs(digits,path,res,idx + 1)
            path.pop(-1)




if __name__ == '__main__':
    s = "23"
    print Solution().letterCombinations(s)