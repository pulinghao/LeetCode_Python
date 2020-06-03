#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/4/25 10:04 下午
 @Author   :pulinghao@baidu.com
 @File     :全排列.py 
 @Description :
"""


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # length = len(nums)
        # res = []
        # if length == 0:
        #     return res
        # path = []  # 保存结果
        # used = [False] * length  # 数字是否被使用到了
        # self.dfs(nums,length,0,path,used,res)
        res = []
        self.help(nums,[],res)
        return res

    def dfs(self, nums, length, depth, path, used, res):
        if depth == length:  # 终止条件
            re_list = list(path)  #执行深拷贝
            res.append(re_list)
            return

        for i in range(length):
            if used[i]:  # 代表这个数字已经被用过了
                continue
            path.append(nums[i])
            used[i] = True
            # 进行下一个层的深度遍历
            self.dfs(nums, length, depth + 1, path, used, res)
            # 回溯
            path.pop()
            used[i] = False
        pass

    def help(self,nums,path,res):
        if len(nums) == 0:
            res.append(list(path))
            return

        for i in range(len(nums)):
            new_nums = nums[:] # 复制一份数字
            new_nums.pop(i) # 将第i个数字删掉
            path.append(nums[i])
            self.help(new_nums,path,res)
            path.pop()



if __name__ == '__main__':
    print Solution().permute(nums=[1, 2, 3])
