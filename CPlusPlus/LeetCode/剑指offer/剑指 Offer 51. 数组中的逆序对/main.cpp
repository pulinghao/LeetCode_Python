//
//  main.cpp
//  剑指 Offer 51. 数组中的逆序对
//
//  Created by pulinghao on 2022/6/21.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int reversePairs(vector<int>& nums) {
        int n = nums.size();
        if (n < 2) {
            return 0;
        }
        vector<int> temp(n);
        return merge_count(nums, 0, n - 1, temp);
    }
    
    // 每一步的时候，先计算子数组内部的逆序对，计算完后，调整数组内部的顺序，即对nums进行操作负值
    // tmp数组，保存的是排序前的nums
    // 子数组内部有序以后，再处理子数组和子数组之间的逆序对
    int merge_count(vector<int>&nums, int left, int right, vector<int> &tmp){
        if (left >= right) {
            return 0;
        }
        int mid = (left + right) / 2;
        int leftArrayRes = merge_count(nums, left, mid, tmp);
        int rightArrayRes = merge_count(nums, mid + 1, right , tmp);
        
        // 剪枝
        // 左边数组的最大值 <= 右边数组的最小值
        if (nums[mid] <= nums[mid + 1]) {
            return leftArrayRes + rightArrayRes;
        }
        for(int i = left; i <= right; i++){
            tmp[i] = nums[i];
        }
        
        int i = left;
        int j = mid + 1;
        int count = 0;
        for (int k = left; k <= right; k++) {
            // 先处理两个case
            if (i == mid + 1) {
                nums[k] = tmp[j];
                j++;
            } else if (j == right + 1){
                nums[k] = tmp[i];
                i++;
            } else if (tmp[i] <= tmp[j]){
                nums[k] = tmp[i];
                i++;
            } else {
                // 逆序对的情况
                nums[k] = nums[j];
                j++;
                count += mid - i + 1;
            }
        }
        
        return count + leftArrayRes + rightArrayRes;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
