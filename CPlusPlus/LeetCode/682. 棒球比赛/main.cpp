//
//  main.cpp
//  682. 棒球比赛
//
//  Created by pulinghao on 2022/3/27.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    int calPoints(vector<string>& ops) {
        vector<int> temp;
        for (int i = 0; i < ops.size(); i++) {
            string s = ops[i];
            char c = s[0];
            if (s == "C") {
                temp.pop_back();
            } else if (s == "+") {
                int n = temp.size();
                int num1 = temp[n - 1];
                int num2 = temp[n - 2];
                int num3 = num1 + num2;
                temp.push_back(num3);
            } else if (s == "D") {
                int n = temp.size();
                int num1 = temp[n - 1];
                int num2 = 2 * num1;
                temp.push_back(num2);
            } else {
                int num = stoi(s);
                temp.push_back(num);
            }
        }
        int res = 0;
        for (int j = 0; j < temp.size(); j++) {
            res += temp[j];
        }
        return res;
     }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
