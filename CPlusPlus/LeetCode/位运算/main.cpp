//
//  main.cpp
//  位运算
//
//  Created by pulinghao on 2022/6/11.
//

#include <iostream>

int main(int argc, const char * argv[]) {
    // insert code here...
    char a = 'A' | ' ';
    char B = 'b' & '_';
    char c = 'C' ^ ' ';
    char D = 'd' ^ ' ';
    
    int n = 3;
    int number = 1;
    int i = 0;
    while (++i < n) {
        number *= 10;
    }
    std::cout << number;
    return 0;
}
