#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/23 11:19 上午
 @Author  :pulinghao@baidu.com
 @File     :5495. 圆形赛道上经过次数最多的扇区.py
 @Description :
"""

class Solution(object):
    def mostVisited(self, n, rounds):
        """
        :type n: int
        :type rounds: List[int]
        :rtype: List[int]
        """
        res = [0] * (n + 1)
        for i in range(1, len(rounds)):
            start = rounds[i - 1]
            end = rounds[i]
            if i == 1:
                if end > start:
                    for j in range(start, end + 1):
                        res[j] += 1
                else:
                    for j in range(start, n + 1):
                        res[j] += 1
                    for j in range(1, end + 1):
                        res[j] += 1
            else:
                if end > start:
                    for j in range(start + 1, end + 1):
                        res[j] += 1
                else:
                    for j in range(start + 1, n + 1):
                        res[j] += 1
                    for j in range(1, end + 1):
                        res[j] += 1

        max = 0
        ans = []
        for i,num in enumerate(res):
            if num > max:
                ans = []
                max = num
                ans.append(i)
            elif num == max:
                ans.append(i)

        return ans



if __name__ == '__main__':
    print Solution().mostVisited(n = 4, rounds = [1,3,1,2])