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

```
to_string(int)
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

