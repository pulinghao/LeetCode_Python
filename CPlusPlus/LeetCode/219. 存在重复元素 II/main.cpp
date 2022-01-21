//
//  main.cpp
//  219. 存在重复元素 II
//
//  Created by pulinghao on 2022/1/19.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool containsNearbyDuplicate(vector<int>& nums, int k) {
        unordered_map<int, int> map;
        for (int i = 0; i < nums.size(); i++) {
            int key = nums[i];
            if (map.count(key) && i - map[key] <= k) {
                return true;
            }
            map[key] = i;
        }
        return false;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
