//
//  main.cpp
//  1447. 最简分数
//
//  Created by pulinghao on 2022/2/10.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    vector<string> simplifiedFractions(int n) {
        vector<string> res;
        
        for (int k = 1; k <= n; k++) {
            for (int i = 1; i < k; i++) {
                bool canMod = false;
                for (int j = 2; j <= i; j++) {
                    if (i % j == 0 && k % j == 0) {
                        canMod = true;
                        break;
                    }
                }
                if (!canMod) {
                    res.push_back(to_string(i) + "/" + to_string(k));
                }
            }
        }
        
        
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    int n = 3;
    vector<string> res = Solution().simplifiedFractions(n);
//    string resStr = stringToIntegerVector(<#string input#>)
    return 0;
}
