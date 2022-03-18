//
//  main.cpp
//  258. 各位相加
//
//  Created by pulinghao on 2022/3/3.
//

#include <iostream>

class Solution {
public:
    int addDigits(int num) {
        if(num / 10 == 0) {
            return num;
        }
        int temp = 0;
        while(num / 10){
            temp += num%10;
            num = num/10;
        }
        temp +=  num;
        return addDigits(temp);
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << Solution().addDigits(38);
    return 0;
}
