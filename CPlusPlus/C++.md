# 数据

## char 转 int

```c++
char a = '0';
int ia = a - '0';
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



# unordered_map

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
```



# vector

- 判断是否为空

```c++
vector<int>& arr;
if(arr.empty()){
	
}
```



- 反转

```c++
vector<int>& arr;
reverse(arr.begin(), arr.begin() + n);
```

- 排序

  - 按照字符串长度和字母序排序

  ```c++
  vector<string>& words;
  sort(words.begin(), words.end(), [](const string &a, const string &b) {
    // 如果两个字符串长度不相等，返回 更长的字符串；
    // 如果两个字符串长度相等，返回 字母序靠前的字符串
  	return a.size() != b.size() ? a.size() < b.size() : a > b;
  });
  ```


- 求和`accumulate`

```c++
#include<numeric>

vector<int> account;
accumulate(account.begin(), account.end(), 0)
```



# 数学

- `__builtin_popcount(x)`

精确计算二进制中1的个数

