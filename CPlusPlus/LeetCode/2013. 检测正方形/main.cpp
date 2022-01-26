//
//  main.cpp
//  2013. 检测正方形
//
//  Created by pulinghao on 2022/1/26.
//

#include <iostream>
#include "common.h"

class DetectSquares {
public:
    unordered_map<int, unordered_map<int, int>> map;
    DetectSquares() {
        
    }
    
    void add(vector<int> point) {
        int x = point[0];
        int y = point[1];
        map[y][x] += 1;
    }
    
    int count(vector<int> point) {
        int x = point[0];
        int y = point[1];
        if (!map.count(y)) {
            return 0;
        }
        unordered_map<int, int> &yCnt = map[y];
        int res = 0;
        for(auto &[col, colCnt] : map){
            if (col != y) {
                int d = col - y;
                res += (colCnt.count(x) ? colCnt[x] : 0 ) * (yCnt.count(x + d) ? yCnt[x + d] : 0) * (colCnt.count(x + d) ? colCnt[x + d] : 0);
                res += (colCnt.count(x) ? colCnt[x] : 0 ) * (yCnt.count(x - d) ? yCnt[x - d] : 0) * (colCnt.count(x - d) ? colCnt[x - d] : 0);
            }
        }
        return res;
    }
};

/**
 * Your DetectSquares object will be instantiated and called as such:
 * DetectSquares* obj = new DetectSquares();
 * obj->add(point);
 * int param_2 = obj->count(point);
 */
*
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
