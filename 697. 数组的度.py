#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/2 10:22 下午
 @Author   :pulinghao@baidu.com
 @File     :697. 数组的度.py 
 @Description :
"""

class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = {}
        for i in range(len(nums)):
            num = nums[i]
            if dic.has_key(str(num)):
                arr = dic[str(num)]
                arr.append(i)
            else:
                arr = []
                arr.append(i)
                dic[str(num)] = arr

        max_length = 0
        max_count = 0
        for item in dic.values():
            if len(item) > max_length:
                max_length = len(item)
                first = item[0]
                last = item[-1]
                max_count = last - first + 1
            elif len(item) == max_length:
                first = item[0]
                last = item[-1]
                if max_count >= last- first:
                    max_count = last - first + 1
            pass
        return max_count
    pass

if __name__ == '__main__':
    nums = [1, 2, 2, 3, 1]
    print Solution().findShortestSubArray(nums)