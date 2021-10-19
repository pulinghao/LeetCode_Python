//
//  main.cpp
//  1104. 二叉树寻路
//
//  Created by pulinghao on 2021/7/29.
//

#include <iostream>
#include <vector>
using namespace std;
class Solution {
public:
    int getReverse(int label, int row) {
            return (1 << row - 1) + (1 << row) - 1 - label;
        }

    vector<int> pathInZigZagTree(int label) {
        int row = 1, rowStart = 1;
        while (rowStart * 2 <= label) {
            row++;
            rowStart *= 2;
        }
        if (row % 2 == 0) {
            label = getReverse(label, row);
        }
        vector<int> path;
        while (row > 0) {
            if (row % 2 == 0) {
                path.push_back(getReverse(label, row));
            } else {
                path.push_back(label);
            }
            row--;
            label >>= 1;
        }
        reverse(path.begin(), path.end());
        return path;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
