//
//  main.cpp
//  71. 简化路径
//
//  Created by pulinghao on 2022/1/6.
//

#include <iostream>
#include "common.h"


class Solution {
public:
    string simplifyPath(string path) {
        auto split = [](const string &s, char delim) -> vector<string>{
            vector<string> ans;
            string cur;
            for(char ch : s){
                if (ch == delim) {
                    ans.push_back(move(cur));  // move 左值引用改为右值引用，这儿避免不必要的拷贝操作
                    cur.clear();
                } else {
                    cur += ch;
                }
            }
            ans.push_back(move(cur));
            return ans;
        };
        
        vector<string> names = split(path, '/');
        vector<string> stack;
        for(string &name : names){
            if (name == "..") {
                if (!stack.empty()) {
                    stack.pop_back();
                }
            }
            
            else if(!name.empty() && name != ".") {
                stack.push_back(move(name));
            }
        }
        string ans;
        if (stack.empty()) {
            ans = "/";
        } else {
            for (string& name : stack){
                ans+= "/" + move(name);
            }
        }
        return ans;
    }
};

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
