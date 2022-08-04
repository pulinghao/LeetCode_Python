//
//  main.cpp
//  习题15.8
//
//  Created by pulinghao on 2022/7/19.
//

#include <iostream>
#include <string>
using namespace::std;

struct base {
    string name(){
        return basename;
    }
    virtual void print(ostream &os){
        os<<basename;
    }
    
private:
    string basename;
};

struct derived : public base{
    void print(ostream &os){
        os<<" "<< men;
    }
private:
    int men;
};

int main(int argc, const char * argv[]) {
    // insert code here...
    base bobj;
    base *bp1 = &bobj;
    base &br1 = bobj;
    derived dobj;
    base *bp2 = &dobj;
    base &br2 = dobj;
    
    bobj.print(cout);
    dobj.print(cout);
    bp1->name();
    bp2->name();
    br1.print(cout);
    br2.print(cout);
    return 0;
}
