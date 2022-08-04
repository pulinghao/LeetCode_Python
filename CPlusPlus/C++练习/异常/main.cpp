//
//  main.cpp
//  异常
//
//  Created by pulinghao on 2022/8/4.
//

#include<iostream>
using namespace std;
int main(){
    cout<<"1--before try block..."<<endl;
    try{
        cout<<"2--Inside try block..."<<endl;
        throw "abc";
        cout<<"3--After throw ...."<<endl;
    }
    catch(int i) {
        cout<<"4--In catch block1 ... exception..errcode  is.."<<i<<endl;
    }
    catch(char const * s) {
        cout<<"5--In catch block2 ... exception..errcode is.."<<s<<endl;
    }
    cout<<"6--After Catch...";
//    system("pause");
}


