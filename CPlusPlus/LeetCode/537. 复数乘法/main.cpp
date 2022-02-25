//
//  main.cpp
//  537. 复数乘法
//
//  Created by pulinghao on 2022/2/25.
//

#include <iostream>

#include "common.h"

class Solution {
public:
    vector<int> getAI(string num1){
        int num1_a = 0;
        int num1_i = 0;
        bool hasAdd1 = false;
        bool jian1a = false;
        bool jian1i = false;
        for (int i = 0; i < num1.size(); i++) {
            char c = num1[i];
            if (isdigit(c)) {
                if (hasAdd1 == false) {
                    num1_a = num1_a * 10 + c - '0';
                } else {
                    num1_i = num1_i * 10 + c - '0';
                }
                
            } else if (c == '+') {
                hasAdd1 = true;
            } else if (c == '-') {
                if (hasAdd1) {
                    jian1i = true;
                } else {
                    jian1a = true;
                }
            }
        }
        
        if (jian1a) {
            num1_a = -num1_a;
        }
        
        if (jian1i) {
            num1_i = -num1_i;
        }
        
        vector<int> res;
        res.push_back(num1_a);
        res.push_back(num1_i);
        return res;
        
    }
    string complexNumberMultiply(string num1, string num2) {
        vector<int> numA1 = getAI(num1);
        vector<int> numA2 = getAI(num2);
        int numa = 0;
        int numi = 0;
        numa = numA1[0] * numA2[0] + numA1[1] * numA2[1] * (-1);
        numi = numA1[0] * numA2[1] + numA1[1] * numA2[0];
        string res;
        res.append(to_string(numa));
        res += "+";
        res.append(to_string(numi));
        res += "i";
        
        return res;
        
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
//    "78+-76i"
//    "-86+72i"
    string num1 = "78+-76i";
    string num2 = "-86+72i";
    std::cout << Solution().complexNumberMultiply(num1, num2);
    return 0;
}
