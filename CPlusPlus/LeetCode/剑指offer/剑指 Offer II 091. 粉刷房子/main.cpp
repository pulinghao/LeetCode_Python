//
//  main.cpp
//  剑指 Offer II 091. 粉刷房子
//
//  Created by pulinghao on 2022/6/25.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int minCost(vector<vector<int>>& costs) {
        int nums = costs.size();
        vector<int> dp(nums + 1);
        vector<int> color(nums);
        vector<int> res;
    
        dp[1] = costs[0][0];
        color[0] = 0;
        for(int i = 2; i < nums + 1;i++){
            if(color[i - 2] == 0){
                if(costs[i - 1][1] <= costs[i - 1][2]){
                    dp[i] = dp[i - 1] + costs[i - 1][1];
                    color[i - 1] = 1;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][2];
                    color[i - 1] = 2;
                }
            } else if (color[i - 2] == 1){
                if(costs[i - 1][0] <= costs[i - 1][2]){
                    dp[i] = dp[i - 1] + costs[i - 1][0];
                    color[i - 1] = 0;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][2];
                    color[i - 1] = 2;
                }
            } else {
                if(costs[i - 1][0] <= costs[i - 1][1]){
                    dp[i] = dp[i - 1] + costs[i - 1][0];
                    color[i - 1] = 0;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][1];
                    color[i - 1] = 1;
                }
            }
        }
        res.push_back(dp[nums]);
        
        dp.clear();
        dp[1] = costs[0][1];
        color[0] = 1;
        for(int i = 2; i < nums + 1;i++){
            if(color[i - 2] == 0){
                if(costs[i - 1][1] <= costs[i - 1][2]){
                    dp[i] = dp[i - 1] + costs[i - 1][1];
                    color[i - 1] = 1;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][2];
                    color[i - 1] = 2;
                }
            } else if (color[i - 2] == 1){
                if(costs[i - 1][0] <= costs[i - 1][2]){
                    dp[i] = dp[i - 1] + costs[i - 1][0];
                    color[i - 1] = 0;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][2];
                    color[i - 1] = 2;
                }
            } else {
                if(costs[i - 1][0] <= costs[i - 1][1]){
                    dp[i] = dp[i - 1] + costs[i - 1][0];
                    color[i - 1] = 0;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][1];
                    color[i - 1] = 1;
                }
            }
        }
        res.push_back(dp[nums]);

        dp.clear();
        dp[1] = costs[0][2];
        color[0] = 2;
        for(int i = 2; i < nums + 1;i++){
            if(color[i - 2] == 0){
                if(costs[i - 1][1] <= costs[i - 1][2]){
                    dp[i] = dp[i - 1] + costs[i - 1][1];
                    color[i - 1] = 1;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][2];
                    color[i - 1] = 2;
                }
            } else if (color[i - 2] == 1){
                if(costs[i - 1][0] <= costs[i - 1][2]){
                    dp[i] = dp[i - 1] + costs[i - 1][0];
                    color[i - 1] = 0;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][2];
                    color[i - 1] = 2;
                }
            } else {
                if(costs[i - 1][0] <= costs[i - 1][1]){
                    dp[i] = dp[i - 1] + costs[i - 1][0];
                    color[i - 1] = 0;
                } else {
                    dp[i] = dp[i - 1] + costs[i - 1][1];
                    color[i - 1] = 1;
                }
            }
        }
        res.push_back(dp[nums]);

        int min = *min_element(res.begin(), res.end());//返回s中的最小值
        return min;
    }
    
    int minCost2(vector<vector<int>>& costs) {
            int n = costs.size();
            vector<int> dp(3);
            for (int j = 0; j < 3; j++) {
                dp[j] = costs[0][j];
            }
            for (int i = 1; i < n; i++) {
                vector<int> dpNew(3);
                for (int j = 0; j < 3; j++) {
                    dpNew[j] = min(dp[(j + 1) % 3], dp[(j + 2) % 3]) + costs[i][j];
                }
                dp = dpNew;
            }
            return *min_element(dp.begin(), dp.end());
        }
};





int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[[5,8,6],[19,14,13],[7,5,12],[14,15,17],[3,20,10]]";
    vector<vector<int>> inputV = stringToIntegerVectors(input);
    
    std::cout << Solution().minCost2(inputV);
    
    std::cout << Solution().minCost(inputV);
    
    return 0;
}
