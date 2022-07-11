//
//  main.cpp
//  剑指 Offer 60. n个骰子的点数
//
//  Created by pulinghao on 2022/6/29.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    vector<double> dicesProbability(int n) {
        int dp[15][70];  // n <= 11,和最大为66
        memset(dp, 0, sizeof(dp));
        for (int i = 1; i <= 6; i++) {
            dp[1][i] = 1;
        }
        
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j <= 6 * i; j++) {
//                for (int l = 1; l <= 6; l++) {
//                    if (j - l >= 1) {
//                        dp[i][j] += dp[i - 1][j - l];
//                        
//                    }
//                }
                for (int l = i - 1; l <= j - 1; l++) {
                    if(j - 1 - l >= 6) continue;
                    dp[i][j] += dp[i - 1][l];
                }
            }
        }
        
        int all = pow(6,n);
        vector<double> ret;
        for (int i = n; i <= 6 * n; i ++) {
            ret.push_back(dp[n][i] * 1.0 / all);
        }
        return ret;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    Solution().dicesProbability(2);
    return 0;
}
