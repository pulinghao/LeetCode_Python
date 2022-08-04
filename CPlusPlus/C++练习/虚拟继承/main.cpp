//
//  main.cpp
//  虚拟继承
//
//  Created by pulinghao on 2022/7/19.
//

#include <iostream>
using namespace std;
class A {
    int a;
public:
    A(){ cout<<"Constructing A"<<endl; }
    virtual void test(){cout<<"test A"<<endl;}
};

class B {
public:
    B(){ cout<<"Constructing B"<<endl;}
    virtual void test(){cout<<"test B"<<endl;}
};

class B1:virtual public B ,virtual public A{
public:
    B1(){cout<<"Contruction B1 no args"<<endl;}
    B1(int i){ cout<<"Constructing B1"<<endl; }
    virtual void test(){cout<<"test B1"<<endl;}
};

class B2:public A,public B {
public:
    B2(int j){ cout<<"Constructing B2"<<endl; }
};
class D: public B1, public B2 {
public:
    D(int m,int n): B1(m),B2(n){ cout<<"Constructing D"<<endl; }
    void test(){cout<<"test D"<<endl;}
    A a;
};
    
int main(){
    D d(1,2);
    B1 b1;
    A *pa;
    pa = &b1;
    pa->test();
//    Constructing B
//    Constructing A
//    Constructing B1
//    Constructing A
//    Constructing B
//    Constructing B2
//    Constructing A
//    Constructing D
    return 0;
}
