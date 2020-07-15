#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/12 10:46 上午
 @Author   :pulinghao@baidu.com
 @File     :5460. 好数对的数目.py 
 @Description :
"""

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        def get_value(n):
            if n == 0:
                return 1
            if n == 1:
                return n
            else:
                return n * get_value(n - 1)
        def gen_last_value(n, m):
            first = get_value(n)
            second = get_value(m)
            third = get_value((n - m))
            return first / (second * third)
        dict = {}
        for i in range(len(nums)):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
        res = 0
        for k,v in dict.items():
            if v == 1:
                continue
            cnt = gen_last_value(v,2)
            res += cnt
        return res


if __name__ == '__main__':
    print Solution().numIdenticalPairs(nums= [1,1,1,1])
