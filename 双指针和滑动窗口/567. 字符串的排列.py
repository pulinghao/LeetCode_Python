#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2021/2/10 10:52 下午
 @Author  :pulinghao@baidu.com
 @File     :567. 字符串的排列.py
 @Description :
"""
import collections
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        # 1. 建立s1的字典
        # 统计 s1 中每个字符出现的次数
        counter1 = collections.Counter(s1)
        N = len(s2)
        # 定义滑动窗口的范围是 [left, right]，闭区间，长度与s1相等
        left = 0
        right = len(s1) - 1
        # 统计窗口s2[left, right - 1]内的元素出现的次数
        counter2 = collections.Counter(s2[0:right])
        while right < N:
            # 把 right 位置的元素放到 counter2 中
            counter2[s2[right]] += 1
            # 如果滑动窗口内各个元素出现的次数跟 s1 的元素出现次数完全一致，返回 True
            if counter1 == counter2:
                return True
            # 窗口向右移动前，把当前 left 位置的元素出现次数 - 1
            counter2[s2[left]] -= 1
            # 如果当前 left 位置的元素出现次数为 0， 需要从字典中删除，否则这个出现次数为 0 的元素会影响两 counter 之间的比较
            if counter2[s2[left]] == 0:
                del counter2[s2[left]]
            # 窗口向右移动
            left += 1
            right += 1
        return False

if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidboaoo"
    print Solution().checkInclusion(s1,s2)