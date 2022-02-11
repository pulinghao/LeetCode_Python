//
//  main.cpp
//  1765. 地图中的最高点
//
//  Created by pulinghao on 2022/1/29.
//

#include <iostream>

#include "common.h"
int dirs[4][2] = {{-1,0},{1,0},{0,-1},{0,1}};
class Solution {
public:
    vector<vector<int>> highestPeak(vector<vector<int>>& isWater) {
        
        int m = isWater.size();
        int n = isWater[0].size();
        int a = abs(m - n);
        vector<vector<int>> res(m, vector<int>(n,-1));
        queue<pair<int, int>> q;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (isWater[i][j] == 1) {
                    res[i][j] = 0;
                    q.emplace(i,j);
                }
            }
        }
        
        while (!q.empty()) {
            auto &p = q.front();
            for(auto &dir : dirs){
                int x = p.first + dir[0], y = p.second + dir[1];
                if (0 <= x && x < m && 0 <= y && y < n && res[x][y] == -1) {
                    res[x][y] = res[p.first][p.second] + 1;
                    q.emplace(x,y);
                }
            }
            q.pop();
        }
        
        return res;
    }
    
};


int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
