//
//  main.cpp
//  1725. 可以形成最大正方形的矩形数目
//
//  Created by pulinghao on 2022/2/4.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int countGoodRectangles(vector<vector<int>>& rectangles) {
        vector<int> squares;
        for (int i = 0; i < rectangles.size(); i++) {
            vector<int> rect = rectangles[i];
            int a = rect[0];
            int b = rect[1];
            int c = min(a, b);
            squares.push_back(c);
        }
        
        sort(squares.begin(), squares.end());
        int n = squares.size();
        int maxLength = squares[n - 1];
        int res = 0;
        for (int i = n - 1; i >= 0; i--) {
            if (squares[i] == maxLength) {
                res ++;
            }
        }
        return res;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    vector<vector<int>> rec = {{5,8},{3,9},{5,12},{16,5}};
    Solution().countGoodRectangles(rec);
    return 0;
}
