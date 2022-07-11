//
//  main.cpp
//  剑指 Offer 56 - II. 数组中数字出现的次数 II
//
//  Created by pulinghao on 2022/6/27.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int singleNumber(vector<int>& nums) {
        vector<int> k(32);
        for (int i = 0; i < nums.size(); ++i)
        {
            int num = nums[i];
            int j = 31;
            while(num){
                k[j] += num % 2;
                num = num >> 1;
                j--;
            }
        }

        vector<int> res(32);
        for (int i = 0; i < 32; ++i)
        {
            if (k[i] % 3 == 1)
            {
                res[i] = 1;
            }
        }

        int resV = 0;
        for (int i = 31; i >= 0; i--)
        {
            if (res[i]) {
                resV += pow(2,31 - i);
            }
        }
        return resV;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> input = {3,4,3,3};
    std::cout << Solution().singleNumber(input);
    return 0;
}
