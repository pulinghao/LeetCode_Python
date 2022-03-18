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



## int  转 string

```c++
int a = 10;
string str_a = to_string(a);
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

# vector

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

  

