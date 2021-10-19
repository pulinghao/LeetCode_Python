//
//  main.cpp
//  447. 回旋镖的数量
//
//  Created by pulinghao on 2021/9/13.
//

#include <iostream>
#include <unordered_map>
#include <string>
#include <vector>

using namespace::std;


class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int ans = 0;
        for (auto &p : points) {
            unordered_map<int, int> cnt;
            for (auto &q : points) {
                int dis = (p[0] - q[0]) * (p[0] - q[0]) + (p[1] - q[1]) * (p[1] - q[1]);
                ++cnt[dis];
            }
            for (auto &[_, m] : cnt) {  //这种写法是C++ 17的写法
                // 如果cnt = 1的话，ans = 0
                // 如果cnt > 1的话，说明，距离相等的点存在，假设 m = 2,就有两个组合
                ans += m * (m - 1);
            }
        }
        return ans;


    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
   
    Solution so;
    vector<vector<int>> points = {{0,0},{1,0},{2,0}};
    cout<<so.numberOfBoomerangs(points);
    
    
    return 0;
}
