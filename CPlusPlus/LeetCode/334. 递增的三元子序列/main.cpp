//
//  main.cpp
//  334. 递增的三元子序列
//
//  Created by pulinghao on 2022/1/12.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool increasingTriplet(vector<int>& nums) {
        if (nums.size() < 3) {
            return false;
        }
        
        int n = nums.size();
        vector<int> leftMin(n);
        vector<int> rightMax(n);
        leftMin[0] = nums[0];
        rightMax[n - 1] = nums[n - 1];
        for (int i = 1; i < n; i++) {
            leftMin[i] = min(nums[i],leftMin[i - 1]);
        }
        
        for (int i = n - 2; i >= 0; i--) {
            rightMax[i] = max(nums[i],rightMax[i + 1]);
        }
        
        for (int i = 1; i < n - 1; i++) {
            if (nums[i] > leftMin[i - 1] && nums[i] < rightMax[i + 1]) {
                return true;
            }
        }
        return false;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
