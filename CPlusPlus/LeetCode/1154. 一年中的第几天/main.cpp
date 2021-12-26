//
//  main.cpp
//  1154. 一年中的第几天
//
//  Created by pulinghao on 2021/12/21.
//

#include <iostream>
#include "common.h"

class Solution {
public:
    int dayOfYear(string date) {
        int year = 0,month = 0,day = 0;
        bool first = false;
        bool second = false;
        
        year = stoi(date.substr(0, 4));
        for (int i = 0; i < date.length(); i++) {
            char c = date[i];
            if (c != '-' && !first && !second) {
                year = year * 10 + (c - 48);
            } else if (c == '-' && !first && !second){
                first = true;
            } else if (c != '-' && first && !second) {
                month = month * 10 + c - 48;
            } else if (c == '-' && first && !second) {
                second = true;
            } else if (c != '-' && first && second) {
                day = day * 10 + c - 48;
            }
        }
        
        bool run = false;
        if (year % 4 == 0) {
            run = true;
        }
        int ret = 0;
        for (int i = 1; i < month ; i++) {
            if (i == 1 || i == 3 || i == 5 || i == 7 || i == 8 || i == 10 || i == 12) {
                ret += 31;
            }
            if (i == 2) {
                if (run) {
                    ret += 29;
                } else {
                    ret += 28;
                }
            }
            
            if (i == 4 || i == 6 || i == 9 || i == 11) {
                ret += 30;
            }
        }
        
        ret += day;
        return ret;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    string date = "2004-03-01";
    std::cout << Solution().dayOfYear(date)<<endl;
    return 0;
}
