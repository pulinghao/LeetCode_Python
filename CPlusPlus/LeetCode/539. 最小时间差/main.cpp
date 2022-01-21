//
//  main.cpp
//  539. 最小时间差
//
//  Created by pulinghao on 2022/1/18.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int findMinDifference(vector<string>& timePoints) {
        vector<int> mins;
        for (int i = 0; i < timePoints.size(); i++) {
            string time = timePoints[i];
            string hh = time.substr(0,2);
            string mm = time.substr(3,5);
            int h = stoi(hh);
            int m = stoi(mm);
            int mi = 0;
            mi = h * 60 + m;
            mins.push_back(mi);
        }
        
        sort(mins.begin(), mins.end());
        int res = INT_MAX;
        for (int i = 1; i < mins.size(); i++) {
            res = min(res, mins[i] - mins[i - 1]);
        }
        int size = mins.size();
        return min(res , 24 * 60 + mins[0] - mins[size - 1]);
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
