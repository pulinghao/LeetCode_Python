//
//  main.cpp
//  测试C++性能
//
//  Created by pulinghao on 2022/3/11.
//

#include <iostream>
#include "common.h"

int main(int argc, const char * argv[]) {
    chrono::system_clock::time_point startTime = chrono::system_clock::now();
    long sum = 0;
    for (int i = 0; i < 10000000; i++) {
        sum += i;
    }
    chrono::system_clock::time_point endTime = chrono::system_clock::now();
    cout << "C++ sum: " << sum << endl;
    cout << "duration: " <<(endTime - startTime).count()*1.0/CLOCKS_PER_SEC << "s" << endl;
    return 0;
}
