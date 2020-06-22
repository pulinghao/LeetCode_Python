# 字符与数字

## 字符

### 取ascii码

```python
# 小写
ascii = ord(char)
```

### 判断某个字符是否是数字

```python
c.isdigit()
s[i].isdigit()
```



## 数字

### 获取最大值、最小值

```python
# 整数最大值
import sys

sys.maxint
```



# 排序

## 普通排序

```python
a = [1,2,3,4]

# 排序
a.sort() #改变a的内容，默认升序

a = sorted(a) # 不改变a的内容，默认升序
```

## lamda表达式

```
# 第一个键降序，当第一个键相等时，第二个键升序
array.sort(key = lambda x: (-x[0], x[1]))
```



## 按某个Key排序对元组排序

```python
# 对第一个key排序
intervals = [[1,2],[3,4]] 
intervals.sort(key=lambda intv: intv[0])
intervals.sort(key=lambda x: x[0])
```



# 数据结构

## 数组List（Python原生）

#### 插入元素

```python
# 插入元素
# index为要插入的索引，item为插入的元素
array.insert(index,item) 
```

#### 构造三维数组

```python
list = [[[0 for i in range(m)] for i in range(n) ] for i in range(k)]
```

#### 数组反转

```python
# 将list反转，list本身不会变化
reverselist = list[::-1] 
```



#### 在末尾添加另外一个数组

```python
list.extend(anotherList)
```



## Collections

```python
import collections
```

### 字典 defaultdict

```python
from collections import defaultdict

# 初始化
dict1 = defaultdict(int)
dict2 = defaultdict(set)
dict3 = defaultdict(str)
dict4 = defaultdict(list)
```

作用是当key不存在时，返回的是工厂函数的默认值，比如list对应[ ]，str对应的是空字符串，set对应set( )，int对应0，



### 队列 deque

```python
# 初始化
queue = deque()

# 设置队列长度
queue = deque(maxlen=10)

# 获取第一个元素
first = queue.popleft()

# 在队尾添加一个元素
queue.append(item)

# 在队头添加一个元素
queue.appendleft(item)
```

# 二分查找框架 [bisect](https://www.cnblogs.com/zhaoyingjie/p/9468935.html)

使用前，务必确保列表是已经排序的

```python
array = [2,4,7,9]
array.sort()
# 插入函数
bisect.insert(array,3) #结果为[2,3,4,7,9]

# 查找该数值将会插入的位置并返回，而不会插入。
bisect.bisect(data,1) # 结果0

#bisect_left 有重复数的情况下，插入到最左边的那个位置。返回将会插入的位置
bisect.bisect_left(array,4) # 结果为2

#bisect_right 有重复数的情况下，插入到最右边的那个位置。返回将会插入的位置
bisect.bisect_right(array,4) #结果为3
```

# 正则表达式

### 字符串处理

### 提取左右括号中的内容

```python
import re
re.findall(r'[(](.*?)[)]', str1) 
```

