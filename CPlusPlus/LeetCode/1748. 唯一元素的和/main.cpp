//
//  main.cpp
//  1748. 唯一元素的和
//
//  Created by pulinghao on 2022/2/6.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    int sumOfUnique(vector<int>& nums) {
        vector<int> temp(101);
        for (int i = 0; i < nums.size(); i++) {
            temp[nums[i]] ++;
        }
        
        int res = 0;
        for (int i = 0; i < temp.size(); i++) {
            if (temp[i] > 1) {
                continue;
            } else if (temp[i] == 1) {
                res += i;
            }
        }
        return res;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[1,2,3,2]";
    vector<int> nums = stringToIntegerVector(input);
    std::cout << Solution().sumOfUnique(nums)<<endl;
    return 0;
}
