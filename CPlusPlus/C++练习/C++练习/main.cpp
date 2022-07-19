//
//  main.cpp
//  C++练习
//
//  Created by pulinghao on 2022/7/12.
//

#include <iostream>

using namespace::std;

double power(double,int);

int main(int argc, const char * argv[]) {
    // insert code here...
    double res = power(3.0, 2);
    int seed = 6;
    srand(6);
    cout<<seed<<endl;
    
    return 0;
}

double power(double x, int n)
{
    double val = 1.0;
    while(n--)
    {
        val*=x;
    }
    return val;
}
