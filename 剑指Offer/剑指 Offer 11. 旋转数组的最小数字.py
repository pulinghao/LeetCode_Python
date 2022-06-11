#!/usr/bin/env python
# _*_coding:utf-8_*_
# @Time:  16:48
# @Author:pulinghao
# @File：剑指 Offer 11. 旋转数组的最小数字.py
# @Software: PyCharm

import leetcode_utils
class Solution(object):
    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        left = 0
        right = len(numbers) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            elif numbers[mid] == numbers[right]:
                # 顺序查找
                min = numbers[left]
                for i in range(left,right):
                    if numbers[i] < min:
                        min = numbers[i]
                return min

    def minArray2(self,numbers):
        index1 = 0
        index2 = len(numbers) - 1
        mid = 0
        while numbers[index1] >= numbers[index2]:
            if index2 - index1 == 1:
                mid = index2
                break
            mid = (index1 + index2) // 2
            if numbers[mid] == numbers[index1] and numbers[mid] == numbers[index2]:
                temp = numbers[mid]
                for i in range(index1,index2 + 1):
                    if numbers[i] < temp:
                        temp = numbers[i]
                        mid = i
                break
            if numbers[mid] >= numbers[index1]:
                index1 = mid
            elif numbers[mid] <= numbers[index2]:
                index2 = mid

        return numbers[mid]





if __name__ == '__main__':
    numbers = [3, 4, 5, 1, 2]
    numbers2 =[2,2,2,0,1]
    print Solution().minArray2(numbers2)