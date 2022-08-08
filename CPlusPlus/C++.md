# 数据

## char 转 int

```c++
char a = '0';
int ia = a - '0';

int iia = atoi(a); //stdlib.h
```

## string 转int

```c++
int stoi(string str);
```

## 判断是否是int



## int  转 string

```c++
int a = 10;
string str_a = to_string(a);
```



# 字符串

## 搜索字符串

`find`接口，没查找到，返回`string::npos`

```c++
str.find(goal) != string::npos;
```

## 字符串扩容

```c++
// 将原来的字符串扩容到n的大小
string.resize(n)
```

## 子字符串

取从pos开始，长度为length的子字符串

```c++
str.substr(pos,length); 
```



# 队列 deque

STL提供了双向队列，能够从头部和尾部取出元素

- 访问队头元素

```c++
item = deque.front()
```

- 弹出队头元素

```c++
deque.pop_front()
```

- 添加元素

```c++
deque.push_back(item)
```

# 栈

```c++
stack<int> q;	//以int型为例
int x;
q.push(x);		//将x压入栈顶
int top = q.top();		//返回栈顶的元素
q.pop();		//删除栈顶的元素
int size = q.size();		//返回栈中元素的个数
bool isEmtpq.empty();		//检查栈是否为空,若为空返回true,否则返回false
```



# 字典 unordered_map

### 遍历

- 迭代器

```C++
unordered_map<string, string> umap;
for (auto iter = umap.begin(); iter != umap.end(); ++iter) {
    cout << "<" << iter->first << ", " << iter->second << ">" << endl;
}
```

- 判断某个key是否存在

```c++
unordered_map<char, vector<char>> edges;
// 判断 某个key是否存在，不存在的话，创建一个vector数组作为value
if (!edges.count(key)) {
    edges[key] = vector<char>();
}

edges.find(key) != edges.end()//查
```



# 数组 vector

## 判断是否为空

```c++
vector<int>& arr;
if(arr.empty()){
	
}
```

## 反转

```c++
vector<int>& arr;
reverse(arr.begin(), arr.begin() + n);
```

## 排序

- 按照字符串长度和字母序排序

```c++
vector<string>& words;
sort(words.begin(), words.end(), [](const string &a, const string &b) {
  // 如果两个字符串长度不相等，返回 更长的字符串；
  // 如果两个字符串长度相等，返回 字母序靠前的字符串
	return a.size() != b.size() ? a.size() < b.size() : a > b;
});
```


- 按照某个算法排序，例如按照两者组合后的结果顺序排序

```c++
 vector<string> strs;
 sort(strs.begin(),strs.end(),compare);
 static bool compare(const string &a,const string &b)
{
    return a+b<b+a;
}
```



## 求和`accumulate`

```c++
#include<numeric>

vector<int> account;
accumulate(account.begin(), account.end(), 0)
```

## 复制

从一个数组复制到另外一个数组

```c++
vector<int> A
vector<int> B = vector<int>(A.begin(),A.begin() + offset);
vector<int> C = vector<int>(A.begin(),A.end());
```

## 最大最小值

```c++
#include <vector>
#include <algorithm>

vector<double> s;
double min = *min_element(s.begin(), s.end());//返回s中的最小值
double max= *max_element(s.begin(), s.end());//返回最大值
```



# struct

- struct内部使用vector

```c++
struct TrieTreeNode
{
    bool end;
    vector<TrieTreeNode *> children = vector<TrieTreeNode *>(26,nullptr); //ok
  	vector<TrieTreeNode *> children2(23,nullptr);   // bad
    vector<int> son(12);  // bad
    vector<TrieTreeNode *> chidlren3; //ok
};

```



# 随机数

- 随机数种子`srand()`

  不选择种子，默认调用`srand(1)`，每次产生的随机数都是一样的

- 随机数`rand()`

```c++
rand() % 6; //产生 0 - 5 的随机数，但是每次结果都是一样的，如果srand一样
```



# 数学

- `__builtin_popcount(x)`

精确计算二进制中1的个数

<<<<<<< Updated upstream
## 随机数

从`[start,end]`的随机数

```c++
rand() % (end - start + 1 ) + start 
```

从`[start,end)`的随机数

```c++
rand() % (end - start) + start 
```


# 函数

## 内联函数

普通函数的调用方式，跳到另外一个地址（函数地址），并在执行结束后，返回

1. 在函数调用时，存储该指令的内存地址；
2. 将函数参数，复制到栈区
3. 跳到标记函起点的内存单元，执行代码
4. 跳回到地址被保存的指令处

内联函数

- 将函数代码，替换为函数调用，无需跳到另一处执行代码

- 运行速度快，但内存开销多



## 类的前向声明

与OC类似，可以声明指针，但是不能声明对象，也不能直接调用方法

```c++
class Fred;	//前向引用声明

class Barney {
   Fred x;	//错误：类Fred的声明尚不完善
};

class Barney {
 public:
   void method()
   {
     x->yabbaDabbaDo();	//错误：Fred类的对象在定义之前被使用
   }
 private:
   Fred* x;   //正确，经过前向引用声明，可以声明Fred类的对象指针
 };
```

# 类

## 基类 派生类

### 构造函数

####  派生构造顺序

- 基类
- 成员
- 派生类自己

### 析构函数

- 先析构自己，再调用基类的析构函数

# 虚函数

## vptr & vtable

虚拟表：用于解决在动态/后期绑定方式的函数调用的查找表，又称vtable，虚函数表

- 虚函数表vtable是在**编译阶段**就已
- **每个使用虚函数的类（或者从使用虚函数的类派生）都有自己的虚拟表**。该表只是编译器在编译时设置的静态数组。虚拟表包含可由类的对象调用的每个虚函数的一个条目。此表中的每个条目只是一个函数指针，指向该类可访问的派生函数
- 指向虚函数表的vtpr指针在运行时才产生

其次，编译器还会添加一个隐藏指向基类的指针，我们称之为vptr。vptr在创建类实例时自动设置，以便指向该类的虚拟表。与this指针不同，this指针实际上是编译器用来解析自引用的函数参数，vptr是一个真正的指针。



虚函数是动态绑定的，默认参数是**静态绑定**的。默认参数的使用需要看**指针或者应用本身**的类型，而不是对象的类型！

> 也就是说，如果虚函数带参数，那么这个参数其实由父类决定

```c++
class Base 
{ 
    public: 
        virtual void fun ( int x = 10 ) 
        { 
            cout << "Base::fun(), x = " << x << endl; 
        } 
}; 

class Derived : public Base 
{ 
    public: 
        virtual void fun ( int x=20 ) 
        { 
            cout << "Derived::fun(), x = " << x << endl; 
        } 
}; 

int main() 
{ 
    Derived d1; 
    Base *bp = &d1; 
    bp->fun();  // 输出10
    return 0; 
} 
```

## 纯虚函数

- 没有实现的虚函数
- 有纯虚函数的类，就是抽象类
- <font color='red'>不能构造抽象类的对象</font>
