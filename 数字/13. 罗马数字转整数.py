#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/19 10:46 下午
 @Author   :pulinghao@baidu.com
 @File     :13. 罗马数字转整数.py 
 @Description :
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        sum = 0
        for i in range(len(s) - 1):
            if s[i] == "I":
                if s[i + 1] == "V" or s[i + 1] == "X":
                    sum -= 1
                else:
                    sum += 1
            if s[i] == "V":
                sum += 5
            if s[i] == "X":
                if s[i + 1] == "L" or s[i + 1] == "C":
                    sum -= 10
                else:
                    sum += 10
            if s[i] == "L":
                sum += 50
            if s[i] == "C":
                if s[i + 1] == "D" or s[i + 1] == "M":
                    sum -= 100
                else:
                    sum += 100
            if s[i] == "D":
                sum += 500
            if s[i] == "M":
                sum += 1000

        if s[-1] == "I":
            sum += 1
        if s[-1] == "V":
            sum += 5
        if s[-1] == "X":
            sum += 10
        if s[-1] == "L":
            sum += 50
        if s[-1] == "C":
            sum += 100
        if s[-1] == "D":
            sum += 500
        if s[-1] == "M":
            sum += 1000


        return sum

    def goodAnswer(self,s):
        a = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        ans = 0
        for i in range(len(s)):
            # 这里巧妙的应用了 a字典对应值，有顺序。例如 I的值就小于V和X的值
            if i < len(s) - 1 and a[s[i]] < a[s[i + 1]]:
                ans -= a[s[i]]
            else:
                ans += a[s[i]]
        return ans



if __name__ == '__main__':
    s = "IX"
    print Solution().romanToInt(s)

