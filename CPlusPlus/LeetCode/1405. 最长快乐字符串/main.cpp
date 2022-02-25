//
//  main.cpp
//  1405. 最长快乐字符串
//
//  Created by pulinghao on 2022/2/7.
//

#include <iostream>

#include "common.h"
class Solution {
public:
    char getMaxChar(int a, int b ,int c){
        if (a >= b && b >= c) {
            return 'a';
        } else if (b >= a && b >= c){
            return 'b';
        } else if (c >= a && c >= b){
            return 'c';
        } else {
            return 'a';
        }
    }
    
    bool isEnd(string s, int a, int b, int c){
        if (s.size() < 2) {
            return true;
        } else {
            int n = s.size();
            if (s.substr(n - 3, n - 1) == "aa" && b == 0 && c == 0 && a > 0) {
                return false;
            } else if (s.substr(n - 3, n - 1) == "bb" && a == 0 && c == 0 && b > 0) {
                return false;
            } else if (s.substr(n - 3, n - 1) == "bb" && a == 0 && b == 0 && c > 0) {
                return false;
            } else {
                return true;
            }
        }
    }
    string longestDiverseString(int a, int b, int c) {
        string res = "";
        while (true) {
            if (getMaxChar(a, b, c) == 'a') {
                res.append("a");
                a--;
            } else if (getMaxChar(a, b, c) == 'b') {
                res.append("b");
                b--;
            } else if (getMaxChar(a, b, c) == 'c') {
                res.append("c");
                c--;
            }
            
            if (!isEnd(res,a,b,c)) {
                break;
            }
        }
        return res;
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    int a = 1;
    int b = 1;
    int c = 7;
    std::cout << Solution().longestDiverseString(a, b, c)<<endl;
    return 0;
}
