#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/28 8:02 上午
 @Author   :pulinghao@baidu.com
 @File     :682. 棒球比赛.py 
 @Description :
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        遇到D就出栈一个数字
        """
        ans = 0
        stack = []
        def is_number(s):
            if s.isdigit():
                return True
            elif s.count('-') == 1 and s.startswith('-'):
                ss = s.split('-')[-1]
                if ss.isdigit():
                    return True
            return False
        for op in ops:
            if is_number(op):
                num = int(op)
                stack.append(num)
                ans += num

            if op == 'C':
                num = stack.pop()
                ans -= num

            if op == 'D':
                num = 2 * stack[-1]
                stack.append(num)
                ans += num

            if op == '+':
                num = stack[-1] + stack[-2]
                stack.append(num)
                ans += num

        return ans

if __name__ == '__main__':
    print Solution().calPoints(["5","-2","4","C","D","9","+","+"])