//
//  main.cpp
//  453. 最小操作次数使数组元素相等
//
//  Created by pulinghao on 2021/10/20.
//

#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
        int minNum = *min_element(nums.begin(),nums.end());
        int res = 0;
        for (int num : nums) {
            res += num - minNum;
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    Solution so;
    vector<int> nums = vector<int>({1,2,3});
    std::cout<<so.minMoves(nums);
    return 0;
}
