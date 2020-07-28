#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/26 10:46 上午
 @Author   :pulinghao@baidu.com
 @File     :5473. 灯泡开关 IV.py 
 @Description :
"""


class Solution(object):
    def minFlips(self, target):
        """
        :type target: str
        :rtype: int
        """
        cnt = 0
        if len(target) == 0:
            return 0

        if target[0] == '1':
            cnt += 1

        for i in range(1,len(target)):
            if target[i] == '1' and target[i - 1] == '0':
                cnt += 1
            if target[i] == '0' and target[i - 1] == '1':
                cnt += 1

        return cnt



if __name__ == '__main__':
    print Solution().minFlips(target = "11000")