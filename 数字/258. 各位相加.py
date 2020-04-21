#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/20 10:51 下午
 @Author   :pulinghao@baidu.com
 @File     :258. 各位相加.py 
 @Description :
"""

class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        # 方法1
        # a = num
        # b = 0
        # while a:
        #     b = a % 10 + b
        #     a = a/10
        #
        # a = b + a
        #
        # if a >= 10:
        #     return self.addDigits(a)
        # else:
        #     return a

        # 方法2
        # 找规律，能被9整除，返回9；不能的话，返回余数
        if num > 9:
            num = num % 9
            if num == 0:
                return 9

        return num




if __name__ == '__main__':
    print Solution().addDigits(19)