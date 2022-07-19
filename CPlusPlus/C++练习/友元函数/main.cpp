//
//  main.cpp
//  友元函数
//
//  Created by pulinghao on 2022/7/14.
//

//使用友元函数计算两点间距离
#include <iostream>
#include <cmath>
using namespace std;
class Point{
  public:
    Point(int x=0,int y=0):X(x),Y(y){}
    int GetX(){
      return X;
    }
    int GetY(){
      return Y;
    }
//    friend float Distance(Point &a,Point &b);
    float Distance(Point &a, Point &b);
    friend float Distance(Point &a, Point &b);
  private:
    int X,Y;//私有数据成员
};


//通过将一个模块声明为另一个模块的友元，一个模块能够引用到另一个模块中本是被隐藏的信息。
float Point::Distance(Point &a, Point &b){
  double dx = a.X-b.X;
  double dy = a.Y-b.Y;
  return sqrt(dx*dx+dy*dy);
}


float Distance(Point &a, Point &b){
  double dx = a.X-b.X;
  double dy = a.Y-b.Y;
  return sqrt(dx*dx+dy*dy);
}

/*
若一个类为另一个类的友元，则此类的所有成员都能访问对方类的私有成员。
声明语法：将友元类名在另一个类中使用friend修饰说明。
*/

/*
如果声明B类是A类的友元，B类的成员函数就可以访问A类的私有和保护数据，
但A类的成员函数却不能访问B类的私有、保护数据。
*/
class A{
  friend class B;
  public:
    void Display(){
      cout<<x<<endl;
    }
    private:
      int x;
};

class B
{   public:
      void Set(int i);
      void Display();
    private:
      A a;
};
void B::Set(int i)
{
   a.x=i;
}
void B::Display()
{
   a.Display();
}

int main()
{
    Point p1(3.0,5.0),p2(4.0,6.0);
    cout<<"两点距离为："<<p1.Distance(p1,p2)<<endl;
    cout<<"两点距离为(友元）："<<Distance(p1,p2)<<endl;
//    system("pause");
    return 0;
}
