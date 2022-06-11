//
//  main.cpp
//  剑指 Offer 17. 打印从1到最大的n位数
//
//  Created by pulinghao on 2022/6/11.
//

#include <iostream>
#include "common.h"


class Solution {
private:
    vector<string> stringlist;
public:
    vector<int> printNumbers(int n) {
        string s(n,'0');
        
        for (int i = 0; i < 10; i++) {
            s[0] = i + '0';
            recursivePrint(s, n, 0);
        }
        vector<int> res;
        for (int i = 0; i < stringlist.size(); i++) {
            string s = stringlist[i];
            int ires = stoi(s);
            if (ires == 0) {
                continue;
            }
            res.push_back(ires);
        }
        return res;
    }
    
    void recursivePrint(string s, int length, int index){
        if (index == length - 1) {
            stringlist.push_back(s);
            return;
        }
        
        for (int i = 0; i < 10; i++) {
            char c = i + '0';
            s[index + 1] = c;
            recursivePrint(s, length, index + 1);
        }
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    Solution().printNumbers(10);
    return 0;
}
