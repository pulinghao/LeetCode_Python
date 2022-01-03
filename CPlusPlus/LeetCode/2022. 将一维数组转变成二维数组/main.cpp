//
//  main.cpp
//  2022. 将一维数组转变成二维数组
//
//  Created by pulinghao on 2022/1/1.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    vector<vector<int>> construct2DArray(vector<int>& original, int m, int n) {
        vector<vector<int>> res;
        if (original.size() != m * n) {
            return res;
        }
        
        for (int i = 0; i < m; i++) {
            vector<int> temp;
            for (int j = 0; j < n; j++) {
                int num = i * m + j;
                temp.push_back(original[num]);
            }
            res.push_back(temp);
        }
        
        return res;
        vector<vector<int>> ans;
        if (original.size() != m * n) {
            return ans;
        }
        for (auto it = original.begin(); it != original.end(); it += n) {
            ans.emplace_back(it, it + n);
        }
        return ans;


    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<int> array({1,1,1,1});
    int m = 4;
    int n = 1;
    vector<vector<int>> res = Solution().construct2DArray(array, m, n);
//    std::cout << Solution().construct2DArray(array, m, n)<<endle;
    return 0;
}
