//
//  main.cpp
//  398. 随机数索引
//
//  Created by pulinghao on 2022/4/25.
//

#include <iostream>
#include "common.h"

class Solution {
    vector<int> &nums;
public:
    Solution(vector<int>& nums) : nums(nums) {}
    
    int pick(int target) {
        int ans = 0;
        for (int i = 0, cnt = 0; i < nums.size(); ++i) {
            if (nums[i] == target) {
                ++cnt; // 第 cnt 次遇到 target
                if (rand() % cnt == 0) {
                    ans = i;
                }
            }
        }
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
