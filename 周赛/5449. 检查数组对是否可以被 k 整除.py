#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/28 11:12 上午
 @Author   :pulinghao@baidu.com
 @File     :5449. 检查数组对是否可以被 k 整除.py 
 @Description :
"""

class Solution(object):
    def canArrange(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: bool
        统计余数的个数
        """
        div = [0] * k
        for num in arr:
            # 统计各个余数的个数
            div[num % k] += 1

        if div[0] % 2 != 0:
            return False

        for i in range(1, k / 2 + 1):
            if div[i] != div[k - i]:
                return False
        return True





if __name__ == '__main__':
    print Solution().canArrange(arr = [5,3,10,1,-7,0,33,-1,10,8,-3,0,-10,47,-9,-6,38,8,5,38,-4,4,-5,-8,-4,0,-8,5,7,3,-3,0,6,8,47,39,35,39,4,9], k = 43)