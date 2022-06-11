//
//  main.cpp
//  剑指 Offer 04. 二维数组中的查找
//
//  Created by pulinghao on 2022/6/1.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool findNumberIn2DArray(vector<vector<int>>& matrix, int target) {
        if(matrix.empty()){
            return false;
        }
        bool res = false;
        int row = 0;
        int col = matrix[0].size() - 1;
        while(row < matrix.size() && col >= 0){
            if (matrix[row][col] == target) {
                return true;
            } else if (matrix[row][col] > target) {
                col --;
            } else {
                row ++;
            }
        }
        return false;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<vector<int>> matrix = {{1,1}};
    int target = 2;
    Solution().findNumberIn2DArray(matrix, 2);
    return 0;
}
