//
//  main.cpp
//  747. 至少是其他数字两倍的最大数
//
//  Created by pulinghao on 2022/1/13.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int dominantIndex(vector<int>& nums) {
        
        vector<int> array = nums;
        sort(nums.begin(),nums.end());
        int n = nums.size();
        if (n == 1) {
            return 0;
        }
        if (nums[n - 1] < 2 * nums[n - 2]) {
            return -1;
        } else {
            for (int i = 0; i < array.size(); i++) {
                if (array[i] == nums[n - 1]) {
                    return i;
                }
            }
            return - 1;
        }
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> nums = {1,2,3,4};
    std::cout << Solution().dominantIndex(nums);
    return 0;
}
