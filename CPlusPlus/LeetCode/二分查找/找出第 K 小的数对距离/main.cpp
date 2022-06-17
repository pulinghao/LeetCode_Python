//
//  main.cpp
//  找出第 K 小的数对距离
//
//  Created by pulinghao on 2022/6/15.
//

#include <iostream>
#include "common.h"
class Solution {
public:
    int smallestDistancePair(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        int n = nums.size(), left = 0, right = nums.back() - nums.front();
        while (left <= right) {
            int mid = (left + right) / 2;
            int cnt = 0;
            for (int i = 0, j = 0; j < n; j++) {
                while (nums[j] - nums[i] > mid) {
                    i++;
                }
                cnt += j - i;
            }
            if (cnt >= k) {
                right = mid - 1;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> v = {1,6,1};
    std::cout << Solution().smallestDistancePair(v, 1);
    return 0;
}
