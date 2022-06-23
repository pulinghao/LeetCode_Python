//
//  main.cpp
//  剑指 Offer 56 - I. 数组中数字出现的次数
//
//  Created by pulinghao on 2022/6/22.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    vector<int> singleNumbers(vector<int>& nums) {
        vector<int> res;
        int one = 0;
        for (auto num : nums) {
            one = num ^ one;
        }
        
        int digit = 1;
        while((one & digit) == 0){
            digit = digit<<1;
        }
        
        int a = 0;
        int b = 0;
        for (auto num : nums) {
            if (num & digit) {
                b ^= num;
            } else {
                a ^= num;
            }
        }
        
        return {a,b};
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> v = {1,2,5,2};
    Solution().singleNumbers(v);
    return 0;
}
