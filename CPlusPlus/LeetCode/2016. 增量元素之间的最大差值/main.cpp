//
//  main.cpp
//  2016. 增量元素之间的最大差值
//
//  Created by pulinghao on 2022/2/26.
//

#include <iostream>

#import "common.h"
class Solution {
public:
    int maximumDifference(vector<int>& nums) {
//        int n = nums.size();
//        int res = -1;
//        for (int i = n - 1; i >= 0; i--) {
//            for (int j = i - 1; j >= 0; j--) {
//                if (nums[i] - nums[j] > 0) {
//                    res = max(res, nums[i] - nums[j]);
//                }
//            }
//        }
//        return res;
        int n = nums.size();
        int ans = -1, premin = nums[0];
        for (int i = 1; i < n; ++i) {
            if (nums[i] > premin) {
                ans = max(ans, nums[i] - premin);
            } else {
                premin = nums[i];
            }
        }
        return ans;


        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[7,1,5,4]";
    vector<int> nums = stringToIntegerVector(input);
    std::cout << Solution().maximumDifference(nums);
    return 0;
}
