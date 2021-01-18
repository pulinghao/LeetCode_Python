#!/usr/bin/env python
# _*_coding:utf-8_*_

"""
@Time :    2020/12/8 7:13 下午
@Author:  pulinghao
@File: 842. 将数组拆分成斐波那契序列.py
@Software: PyCharm
"""

import leetcode_utils


class Solution(object):
    def __init__(self):
        pass

    def func(self, root):
        pass

    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        ans = []
        def backtrack(index):
            if index == len(S):
                return len(ans) >= 3

            cur = 0
            for i in range(index,len(S)):
                if i > index and S[index] == '0':
                    break

                cur = cur * 10 + ord(S[i]) - ord('0')
                if cur > 2 ** 31 - 1:
                    break

                if len(ans) < 2 or cur == ans[-2] + ans[-1]:
                    ans.append(cur)
                    if backtrack(i + 1):
                        return True
                    ans.pop(-1)
                elif len(ans) > 2 and cur > ans[-2] + ans[-1]:
                    break

            return False


        backtrack(0)
        return ans

if __name__ == '__main__':
    S = "123456579"
    out = Solution().splitIntoFibonacci(S)
    print out
