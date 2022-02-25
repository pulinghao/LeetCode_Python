//
//  main.cpp
//  1791. 找出星型图的中心节点
//
//  Created by pulinghao on 2022/2/18.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int findCenter(vector<vector<int>>& edges) {
        unordered_map<int, int> map;
        for (int i = 0; i < edges.size(); i++) {
            vector<int> v = edges[i];
            for (int j = 0; j < v.size(); j++) {
                int i = v[j];
                map[i]++;
            }
        }
        for (auto it = map.begin(); it !=map.end(); it++) {
            if (it->second > 1) {
                return it->first;
            }
        }
        return 0;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string input = "[[1,2],[2,3],[4,2]]";
    vector<vector<int>> vec = stringToIntegerVectors(input);
    std::cout << Solution().findCenter(vec)<<endl;
    return 0;
}
