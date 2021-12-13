//
//  main.cpp
//  807. 保持城市天际线
//
//  Created by pulinghao on 2021/12/13.
//

#include <iostream>

#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace::std;
class Solution {
public:
    int maxIncreaseKeepingSkyline(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<int> colMax(n);
        vector<int> rowMax(n);
        
        for (int i = 0; i < grid.size()(); i++) {
            for (int j = 0; j < grid[0].size(); j++) {
                rowMax[i] = max(rowMax[i], grid[i][j]);
                colMax[j] = max(colMax[j], grid[i][j]);
            }
        }
        
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                ans += min(rowMax[i],colMax[j]) - grid[i][j];
            }
        }
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
