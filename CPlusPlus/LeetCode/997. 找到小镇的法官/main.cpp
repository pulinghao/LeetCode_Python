//
//  main.cpp
//  997. 找到小镇的法官
//
//  Created by pulinghao on 2021/12/19.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    int findJudge(int n, vector<vector<int>>& trust) {
        vector<int> inDegrees(n + 1);
        vector<int> outDegrees(n + 1);
        for (auto& edge : trust) {
            int x = edge[0], y = edge[1];
            ++inDegrees[y];
            ++outDegrees[x];
        }
        for (int i = 1; i <= n; ++i) {
            if (inDegrees[i] == n - 1 && outDegrees[i] == 0) {
                return i;
            }
        }
        return -1;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    int n = 2;
    vector<vector<int>> trust = {{1,2}};
    std::cout << Solution().findJudge(n, trust);
    return 0;
}
