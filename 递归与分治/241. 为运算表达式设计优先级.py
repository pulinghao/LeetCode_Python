#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/27 4:42 下午
 @Author   :pulinghao@baidu.com
 @File     :241. 为运算表达式设计优先级.py 
 @Description :
"""


class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in {'+', '-', '*'}:
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i + 1:])
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        if char == '-':
                            res.append(l - r)
                        if char == '*':
                            res.append(l * r)

        return res

if __name__ == '__main__':
    print Solution().diffWaysToCompute("2-1-1")