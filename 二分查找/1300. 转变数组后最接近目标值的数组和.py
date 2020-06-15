#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/6/14 5:17 下午
 @Author   :pulinghao@baidu.com
 @File     :1300. 转变数组后最接近目标值的数组和.py 
 @Description :
"""
import bisect
class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        # 排序
        arr.sort()
        n = len(arr)
        prefix = [0]
        for num in arr:
            # 前缀和
            prefix.append(prefix[-1] + num)

        right = max(arr)
        ans = 0
        diff = target
        for i in range(1 , right + 1):
            it = bisect.bisect_left(arr,i)
            current = prefix[it] + (n - it) * i
            if abs(current - target) < diff:
                ans = i
                diff = abs(current - target)

        return ans


        return res[0][1]


if __name__ == '__main__':
    print Solution().findBestValue(arr = [2,3,5], target = 10)