//
//  main.cpp
//  构造函数&析构函数
//
//  Created by pulinghao on 2022/7/14.
//

#include <iostream>


using namespace std;
class A {
public:
    A(){ cout<<"Constructing A"<<endl; }
    void printA(){
//        x = 3;
        cout<<"this is A"<<endl;
    }
    ~A(){ cout<<"Destructing A"<<endl; }
private:
    int x;
};
class B:public A {
public:
   ~B(){ cout<<"Destructing B"<<endl; }
};

class Base{
private:
    int x;
public:
    Base(int a){
        x=a;
        cout<<"Base constructor x="<<x<<endl;
    }
    ~Base(){ cout<<"Base destructor..."<<endl; }
};
class Derived:public  Base{
private:
    int y;
public:
    Derived(int a,int b):Base(a){       //派生类构造函数的初始化列表
        y=b;
        cout<<"Derived constructor y="<<y<<endl;
    }
    ~Derived(){ cout<<"Derived destructor..."<<endl; }
};

void test(){
//    B b;
    Derived d(1,2);
    A *pA = new A();
    delete pA;
//    pA->printA();
    pA = nullptr;
    pA->printA();
//    Base *pB = new Base(1);
//    delete pB;
    Base *pB = (Base *)malloc(sizeof(Base));
    free(pB);

}
int main(){
    test();
//    system("pause");
}
