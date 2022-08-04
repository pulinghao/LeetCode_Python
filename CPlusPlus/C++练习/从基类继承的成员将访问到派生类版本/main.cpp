//
//  main.cpp
//  从基类继承的成员将访问到派生类版本
//
//  Created by pulinghao on 2022/8/3.
//

#include <iostream>
using namespace std;
class B{
public:
    void f(){ g(); }
    virtual void g(){ cout << "B::g"; }
};
class D : public B{
public:
    void g(){ cout << "D::g\n"; }
};
int main(){
    D d;
    d.f();
//    system("pause");
    return 0;
}
