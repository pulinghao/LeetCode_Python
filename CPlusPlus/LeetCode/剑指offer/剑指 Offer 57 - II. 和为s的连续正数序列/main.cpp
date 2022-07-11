//
//  main.cpp
//  剑指 Offer 57 - II. 和为s的连续正数序列
//
//  Created by pulinghao on 2022/6/27.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    vector<vector<int>> findContinuousSequence(int target) {
        vector<vector<int>> res;
        int small = 1;
        int big = 2;
        int mid = (1 + target) / 2;
        int curSum = small + big;
        while(small < mid){
            if(curSum == target){
                // 添加到数组中
                vector<int> temp;
                for(int i = small; i<= big;i++){
                    temp.push_back(i);
                }
                res.push_back(temp);
                big++;
                curSum+=big;
            } else if(curSum > target){
                curSum-=small;
                small++;
            } else {
                big++;
                curSum+=big;
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    Solution().findContinuousSequence(9);
    return 0;
}
