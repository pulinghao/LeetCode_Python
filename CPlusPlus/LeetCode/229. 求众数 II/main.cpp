//
//  main.cpp
//  229. 求众数 II
//
//  Created by pulinghao on 2021/10/22.
//

#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;


class Solution {
public:
    vector<int> majorityElement(vector<int>& nums) {
        int count = nums.size() / 3;
        unordered_map<int, int> map;
        vector<int> ans;
        for (int i = 0; i < nums.size(); i++) {
            int num = nums[i];
            if (map[num]) {
                map[num] = map[num] + 1;
            } else {
                map[num] = 1;
            }
        }
        
        for (auto &v : map){
            if (v.second > count) {
                ans.push_back(v.first);
            }
        }
        return ans;
    }
};


