#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/8/16 10:37 上午
 @Author   :pulinghao@baidu.com
 @File     :5185. 存在连续三个奇数的数组.py 
 @Description :
"""

class Solution(object):
    def threeConsecutiveOdds(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        i = 0
        ans = False
        while i < len(arr):
            if arr[i] % 2 == 1:
                if i + 1 < len(arr) and arr[i + 1] % 2 == 1 and i + 2 < len(arr) and arr[i + 2] % 2 == 1:
                    ans = True
                    break

            i += 1
        return ans

if __name__ == '__main__':
    arr = [1,2,34,3,4,5,7,23,12]
    print Solution().threeConsecutiveOdds(arr)