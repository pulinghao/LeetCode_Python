//
//  main.cpp
//  1984. 学生分数的最小差值
//
//  Created by pulinghao on 2022/2/11.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    int minimumDifference(vector<int>& nums, int k) {
        if (nums.size() == 1) {
            return 0;
        }
        vector<int> temp(100000);
        for (int i = 0; i < nums.size(); i++) {
            temp[nums[i]]++;
        }
        
        vector<int> temp2;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] != 0) {
                temp2.push_back(i);
            }
        }
        
        int max = INT_MAX;
        for (int i = 0; i < temp2.size() + 1 - k; i++) {
//            if (temp2[i + k - 1] - temp2[i] < max) {
                max = min(max,temp2[i + k - 1] - temp2[i]);
//            }
        }
        return max;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[87063,61094,44530,21297,95857,93551,9918]";
    vector<int> nums = stringToIntegerVector(input);
    int k = 6;
    std::cout << Solution().minimumDifference(nums, k);
    return 0;
}
