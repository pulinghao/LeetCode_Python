//
//  main.cpp
//  661. 图片平滑器
//
//  Created by pulinghao on 2022/3/24.
//

#include <iostream>
#include "common.h"
class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& img) {
        vector<vector<int>> res;
        int m = img.size();
        int n = img[0].size();
        for (int i = 0; i < m; i++) {
            vector<int> line;
            for (int j = 0; j < n; j++) {
                int temp = avg(i, j, img);
                line.push_back(temp);
//                res.push_back(temp);
            }
            res.push_back(line);
        }
        return res;
    }
    
    int avg(int x,int y, vector<vector<int>>& img){
        int res = 0;
        int count = 0;
        int sum = 0;
        for (int i = x - 1; i < x + 2; i++) {
            for (int j = y - 1; j < y + 2; j++) {
                if (i < 0 || i > img.size() - 1 || j < 0 || j > img[0].size() - 1) {
                    continue;
                } else {
                    count ++;
                    sum += img[i][j];
                }
            }
        }
        res = sum / count;
        return res;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    vector<vector<int>> img = {{100,200,100},{200,50,200},{100,200,100}};
    Solution().imageSmoother(img);
    return 0;
}
