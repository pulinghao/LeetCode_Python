//
//  main.cpp
//  重载
//
//  Created by pulinghao on 2022/7/14.
//

#include <iostream>

using namespace std;
class Time{
private:
    int hh,mm,ss;
public:
    Time(int h=0,int m=0,int s=0):hh(h),mm(m),ss(s){}
    void operator()(int h,int m,int s) {
        hh=h;
        mm=m;
        ss=s;
    }
    
    Time operator++();
    Time operator++(int);
    void ShowTime(){
        cout<<hh<<":"<<mm<<":"<<ss<<endl;
    }
};

Time Time::operator++(int n){
    Time tmp = *this;
    ++(*this);
    return tmp;
}

Time Time::operator++(){
    ++ss;
    if(ss == 60){
        ss = 0;
        ++mm;
        if (mm == 60) {
            mm = 0;
            hh++;
            if (hh == 24) {
                hh = 0;
            }
        }
    }
    return *this;
}
int main(){
    Time t1(12,10,11);
    t1.ShowTime();
    t1.operator()(23,20,34);  // 显示调用()
//    t1.ShowTime();
    t1(10,10,10);             //重载()
    t1.ShowTime();
    
    Time t(23,59,59);
    ++t;
    t.ShowTime();
    (t++).ShowTime();
    t.ShowTime();
//    system("pause");
}
