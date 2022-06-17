//
//  main.cpp
//  498. 对角线遍历
//
//  Created by pulinghao on 2022/6/14.
//

#include <iostream>
#include "common.h"
class Solution {
public:
    vector<int> findDiagonalOrder(vector<vector<int>>& mat) {
        int i = 0;
        int j = 0;
        bool left = true;
        int m = mat.size();
        int n = mat[0].size();
        vector<int> res;
        while((i!= m - 1)||(j!= n - 1)){
            res.push_back(mat[i][j]);
            if(left){
                i--;
                j++;
                if (i < 0) {
                    left = false;
                    i = 0;
                    if (j == n) {
                        i = 1;
                        j = n - 1;
                    }
                } else {
                    
                    if (j == n) {
                        left = false;
                        i = i + 2;
                        j = n - 1;
                    }
                }
            } else {
                i++;
                j--;
                if (j < 0) {
                    left = true;
                    j = 0;
                    if (i == m) {
                        j = 1;
                        i = m - 1;
                    }
                } else {
                    if (i == m) {
                        left = true;
                        j = j + 2;
                        i = m - 1;
                    }
                }
            }
        }
        //最后一个元素单独处理
        res.push_back(mat[m - 1][n - 1]);
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[[1,2,3],[4,5,6],[7,8,9]]";
//    string input = "[[2,3]]";
    vector<vector<int>> mat = stringToIntegerVectors(input);
    vector<int> res = Solution().findDiagonalOrder(mat);
    return 0;
}
