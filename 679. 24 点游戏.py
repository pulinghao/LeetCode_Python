#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time :2020/8/22 11:08 下午
 @Author   :pulinghao@baidu.com
 @File     :679. 24 点游戏.py 
 @Description :
"""

target = 24
ex = 1e-6

class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        curnums = []
        for num in nums:
            curnums.append(float(num))

        return self.dfs(curnums)


    def dfs(self,nums):
        if len(nums) == 0:
            return False

        if len(nums) == 1:
            return abs(target - nums[0]) < ex

        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    curnums = []
                    for k in range(len(nums)):
                        if k != i and k != j:
                            curnums.append(nums[k])

                    # 尝试每一种运算
                    # a + b
                    curnums.append(nums[i] + nums[j])
                    isOk = self.dfs(curnums)
                    curnums.pop(-1)
                    if isOk:
                        return True
                    # a - b
                    curnums.append(nums[i] - nums[j])
                    isOk = self.dfs(curnums)
                    curnums.pop(-1)
                    if isOk:
                        return True

                    # a * b
                    curnums.append(nums[i] * nums[j])
                    isOk = self.dfs(curnums)
                    curnums.pop(-1)
                    if isOk:
                        return True

                    # a / b
                    if nums[j] != 0:
                        curnums.append(nums[i] / nums[j])
                        isOk = self.dfs(curnums)
                        curnums.pop(-1)
                        if isOk:
                            return True

        return False


if __name__ == '__main__':
    nums = [4, 1, 8, 7]
    print Solution().judgePoint24(nums)