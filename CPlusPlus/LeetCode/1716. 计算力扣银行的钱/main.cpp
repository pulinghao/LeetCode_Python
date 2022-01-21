//
//  main.cpp
//  1716. 计算力扣银行的钱
//
//  Created by pulinghao on 2022/1/15.
//

#include <iostream>

class Solution {
public:
    int totalMoney(int n) {
        int week = n / 7;
        int rest = n % 7;
        int start = 1;
        int ans = 0;
        for (int i = 0; i < week ; i++) {
            for (int j = 0; j < 7; j++) {
                ans += start + j;
            }
            start += 1;
        }
        
        start = 1 + week;
        for (int i = 0; i < rest; i++) {
            ans +=  start + i;
        }
        return ans;
    }
};


int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
