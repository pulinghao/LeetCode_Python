//
//  main.cpp
//  剑指 Offer 62. 圆圈中最后剩下的数字
//
//  Created by pulinghao on 2022/7/15.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int lastRemaining(int n, int m) {
        vector<int> nums;
        for (int i = 0; i < n; i++) {
            nums.push_back(i);
        }
        
        int index = 0;
        while (nums.size() != 1) {
            int count = m - 1;
            while(count > 0){
                index++;
                if (index >= nums.size()) {
                    index = index - nums.size();
                }
                count--;
            }
            nums.erase(nums.begin() + index);
        }
        return nums[0];
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    int n =10,m = 17;
    cout<<Solution().lastRemaining(n, m);
    return 0;
}
