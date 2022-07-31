//
//  main.cpp
//  565. 数组嵌套
//
//  Created by pulinghao on 2022/7/17.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int arrayNesting(vector<int>& nums) {
        int n = nums.size();
        vector<int> cnt(n,1);
        int res = 1;
        for (int i = 0; i < nums.size(); i++) {
            int temp = 0;
            int idx = i;
            while (cnt[idx] != 0) {
                cnt[idx]--;
                int nextIdx = nums[idx];
                idx = nextIdx;
                temp++;
            }
            res = max(res, temp);
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    vector<int> A = {5,4,0,3,1,6,2};
    // insert code here...
    std::cout << Solution().arrayNesting(A);
    return 0;
}
