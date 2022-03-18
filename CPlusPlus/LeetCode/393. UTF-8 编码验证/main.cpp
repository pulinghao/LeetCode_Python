//
//  main.cpp
//  393. UTF-8 编码验证
//
//  Created by pulinghao on 2022/3/13.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    bool validUtf8(vector<int>& data) {
        int i = 0;
        bool res = true;
        while (i < data.size()) {
            int num = data[i];
            if ((num >> 7) == 0) {
                i++;
            } else if ((num >> 5) == 0b110) {
                i++;
                if (i < data.size() && (data[i] >> 6) == 0b10) {
                    i++;
                } else {
                    res = false;
                    break;
                }
            } else if ((num >> 4) == 0b1110) {
                i += 2;
                if (i < data.size() && (data[i] >> 6) == 0b10 && (data[i - 1] >> 6) == 0b10) {
                    i++;
                } else {
                    res = false;
                    break;
                }
            } else if ((num >> 3) == 0b11110){
                i += 3;
                if (i < data.size() && (data[i] >> 6) == 0b10&& (data[i - 1] >> 6) == 0b10 && (data[i - 2] >> 6) == 0b10) {
                    i++;
                } else {
                    res = false;
                    break;
                }
            } else {
                res = false;
                break;
            }
        }
        return res;
    }
};

int main(int argc, const char * argv[]) {
    string data = "[240,162,138,147]";
    vector<int> input = stringToIntegerVector(data);
    // insert code here...
    std::cout << Solution().validUtf8(input);
    return 0;
}
