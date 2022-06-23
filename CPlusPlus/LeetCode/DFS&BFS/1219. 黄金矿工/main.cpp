//
//  main.cpp
//  1219. 黄金矿工
//
//  Created by pulinghao on 2022/2/5.
//

#include <iostream>

#include "common.h"

vector<vector<int>> dirs = {{0,1},{0,-1},{1,0},{-1,0}};
class Solution {
private:
    int ans = 0;
    vector<vector<int>> visited;
    int _m = 0;
    int _n = 0;
public:
    bool isValid(int a, int b){
        return a >= 0 && b >= 0 && a < _m && b < _n;
    }
    int dfs(int x, int y, vector<vector<int>> &grid){
        int gold = grid[x][y];
        
        for(auto &dir : dirs){
            int a = x + dir[0];
            int b = y + dir[1];
            if (isValid(a, b) && !visited[a][b] && grid[x][y]) {
                visited[a][b] = 1;
                gold = max(gold,grid[x][y] + dfs(a, b, grid));
                visited[a][b] = 0;
            }
        }
        return gold;
    }
    int getMaximumGold(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        
        _m = m;
        _n = n;
        int ret = 0;
        for (int i = 0; i < m ; i++) {
            vector<int> temp;
            for (int j = 0; j < n; j++) {
                temp.push_back(0);
            }
            this->visited.push_back(temp);
        }
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j]) {
                    visited[i][j] = 1;
                    ret = max(ret,dfs(i, j, grid));
                    visited[i][j] = 0;
                }
            }
        }
        return ret;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[[0,6,0],[5,8,7],[0,9,0]]";
    vector<vector<int>> grid = stringToIntegerVectors(input);
    int ret = Solution().getMaximumGold(grid);
    cout<<ret<<endl;
    return 0;
}
