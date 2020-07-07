#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time     :2020/7/3 2:39 下午
 @Author   :pulinghao@baidu.com
 @File     :974. 和可被 K 整除的子数组.py 
 @Description :
"""

class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        # ans = 0
        # sum = [0] * (len(A) + 1)
        # sum[0] = 0
        # for i in range(0,len(A)):
        #     sum[i + 1] = sum[i] + A[i]
        #
        # for i in range(1,len(sum)):
        #     for j in range(0,i):
        #         sub = sum[i] - sum[j]
        #         if sub % K == 0:
        #             ans += 1
        #
        # return ans
        return self.prefixSum(A,K)

    def prefixSum(self,nums,K):
        prefix = {}
        prefix[0] = 1
        sum_i = 0
        ans = 0
        for i in range(len(nums)):
            # pre[j] mod K = pre[i - 1] mod K
            # 前缀和只关心 mod K以后的值，出现的次数
            sum_i = (sum_i + nums[i]) % K
            if sum_i < 0:
                sum_i += K

            if sum_i in prefix:
                ans += prefix[sum_i]

            if sum_i in prefix:
                prefix[sum_i] += 1
            else:
                prefix[sum_i] = 1

        return ans


if __name__ == '__main__':
    # A = [1,2,3]
    # K = 3
    print Solution().subarraysDivByK(A = [4,5,0,-2,-3,1], K = 5)