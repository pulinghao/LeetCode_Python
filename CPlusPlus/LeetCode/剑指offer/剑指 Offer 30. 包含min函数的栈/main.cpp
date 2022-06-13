//
//  main.cpp
//  剑指 Offer 30. 包含min函数的栈
//
//  Created by pulinghao on 2022/6/12.
//

#include <iostream>
#include "common.h"

class MinStack {
stack<int> dataSt;
stack<int> minSt;
public:
    /** initialize your data structure here. */
    MinStack() {
        minSt.push(INT_MAX);
    }
    
    void push(int x) {
        dataSt.push(x);
        int min = minSt.top();
        if(x < min){
            minSt.push(x);
        } else {
            minSt.push(min);
        }
    }
    
    void pop() {
        dataSt.pop();
        minSt.pop();
    }
    
    int top() {
        return dataSt.top();
    }
    
    int min() {
        return minSt.top();
    }
};
int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
