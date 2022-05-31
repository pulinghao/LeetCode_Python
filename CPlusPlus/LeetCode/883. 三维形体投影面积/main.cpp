//
//  main.cpp
//  883. 三维形体投影面积
//
//  Created by pulinghao on 2022/4/26.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int projectionArea(vector<vector<int>>& grid) {
        int res = 0;
        // 每一行的最大值相加
        int over = 0;
        int rowSum = 0;
        vector<int> rows;
        vector<int> cols;
        for (int i = 0; i < grid.size(); i++) {
            int temp = 0;
            vector<int> row = grid[i];
            for (int j = 0; j < row.size(); j++) {
                temp = max(temp,row[j]);
            }
            rows.push_back(temp);
        }
        // 每一列的最大值相加
        vector<int> oneRow = grid[0];
        int colSize = oneRow.size();
        for (int i = 0; i < colSize; i++) {
            int temp = 0;
            for (int j = 0; j < grid.size(); j++) {
                temp = max(temp,grid[j][i]);
            }
            cols.push_back(temp);
        }
        
        for (int i = 0; i < grid.size(); i++) {
            vector<int> row = grid[i];
            for (int j = 0; j < row.size(); j++) {
                if (row[j] != 0) {
                    over ++;
                }
            }
        }
        
        res = accumulate(rows.begin(), rows.end(), 0) + accumulate(cols.begin(), cols.end(), 0) + over;
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string inputStr = "[[1,2],[3,4]]";
    vector<vector<int>> input = stringToIntegerVectors(inputStr);
    std::cout << Solution().projectionArea(input);
    return 0;
}
