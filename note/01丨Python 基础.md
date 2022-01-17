---
author: 1ch0
index_img: https://raw.githubusercontent.com/1ch0/Figure-bed/main/img/python-programming.jpg
date: 2022-01-12-星期三 15:37
update: 2022-01-12-Wednesday 15:40:37
tags: Python
categories: Python
hide: false
title: Python核心技术与实战-基础篇 
---

# Python核心技术与实战-基础篇

## 1. 列表和元组

### 1.1 基础

- 列表是动态的，长度大小不固定，可以随意地增加、删减或者改变元素（mutable）。
- 而元组是静态的，长度大小固定，无法增加删减或者改变（immutable）。
- Python 中的列表和元组都支持负数索引，-1 表示最后一个元
  素，-2 表示倒数第二个元素，以此类推。
- 列表和元组都支持切片操作
- 列表和元组都可以随意嵌套
- 两者也可以通过 list() 和 tuple() 函数相互转换

### 1.2 存储方式的差异

- 列表是动态的、可变的，而元组是静态的、不可变的
- 由于列表是动态的，所以它需要存储指针，来指向对应的元素（上述例子中，对于int 型，8 字节）。另外，由于列表可变，所以需要额外存储已经分配的长度大小（8 字节），这样才可以实时追踪列表空间的使用情况，当空间不足时，及时分配额外空间。

### 1.3 性能

- 元组要比列表更加轻量级一些，所以总体上来说，元组的性能速度要略优于列表。

- Python 会在后台，对静态数据做一些资源缓存（resource caching）。对于一些静态变量，比如元组，如果它不被使用并且占用空间不大时，Python 会暂时缓存这部分内存。这样，下次我们再创建同样大小的元组时，Python 就可以不用再向操作系统发出请求，去寻找内存，而是可以直接分配之前缓存的内存空间，这样就能大大加快程序的运行速度。

- 元组的初始化速度，要比列表快 5 倍。

  ```python
  python3 -m timeit 'x=(1,2,3,4,5,6)'
  20000000 loops, best of 5: 9.97 nsec per loop
  python3 -m timeit 'x=[1,2,3,4,5,6]'
  5000000 loops, best of 5: 50.1 nsec per loop
  ```

- 如果是索引操作的话，两者的速度差别非常小，几乎可以忽略不计。

  ```python
  python3 -m timeit -s 'x=[1,2,3,4,5,6]' 'y=x[3]'
  10000000 loops, best of 5: 22.2 nsec per loop
  python3 -m timeit -s 'x=(1,2,3,4,5,6)' 'y=x[3]'
  10000000 loops, best of 5: 21.9 nsec per loop
  ```

### 1.4 使用场景

1. 如果存储的数据和数量不变，选用元组更合适。
2. 如果存储的数据或数量是可变的，用列表更合适。

```ad_summary
总的来说，列表和元组都是有序的，可以存储任意数据类型的集合，区别主要在于下面这两点。
- 列表是动态的，长度可变，可以随意的增加、删减或改变元素。列表的存储空间略大于元
组，性能略逊于元组。
- 元组是静态的，长度大小固定，不可以对元素进行增加、删减或者改变操作。元组相对于
列表更加轻量级，性能稍优。

元素不需要改变时:
两三个元素，使用 tuple，元素多一点使用namedtuple。
元素需要改变时:
需要高效随机读取，使用list。需要关键字高效查找，采用 dict。去重，使用 set。大型数
据节省空间，使用标准库 array。大型数据高效操作，使用 numpy.array。
```

## 2. 字典和集合

### 2.1 基础

- 字典是一系列由键（key）和值（value）配对组成的元素的集合，在 Python3.7+，字典被确定为有序（注意：在 3.6 中，**字典有序**是一个implementation detail，在 3.7 才正式成为语言特性，因此 3.6 中无法 100% 确保其有序性），而 3.6 之前是无序的，其长度大小可变，元素可以任意地删减和改变。
- 相比于列表和元组，字典的性能更优，特别是对于查找、添加和删除操作，字典都能在常数
  时间复杂度内完成。
- 集合和字典基本相同，唯一的区别，就是**集合没有键和值的配对，是一系列无序的、唯一的元素组合**。
- **Python 中字典和集合，无论是键还是值，都可以是混合类型。**
- 

#### 2.1.1 元素访问

- 字典访问可以直接索引键，如果不存在，就会抛出异常

  使用 get(key, default) 函数来进行索引。如果键不存在，调用 get() 函数可以返回一个默认值

- 集合并不支持索引操作，因为集合本质上是一个哈希表，和列表不一样

  判断一个元素在不在字典或集合内，我们可以用 value in dict/set 来判断

- 字典和集合也同样支持增加、删除、更新等操作

  ```python
  d = {'name': 'jason', 'age': 20}
  d['gender'] = 'male' # 增加元素对'gender': 'male'
  d['dob'] = '1999-02-01' # 增加元素对'dob': '1999-02-01'
  d
  {'name': 'jason', 'age': 20, 'gender': 'male', 'dob': '1999-02-01'}
  d['dob'] = '1998-01-01' # 更新键'dob'对应的值
  d.pop('dob') # 删除键为'dob'的元素对
  '1998-01-01'
  d
  {'name': 'jason', 'age': 20, 'gender': 'male'}
  s = {1, 2, 3}
  s.add(4) # 增加元素 4 到集合
  s
  {1, 2, 3, 4}
  s.remove(4) # 从集合中删除元素 4
  s
  {1, 2, 3}
  ```

- 集合的 pop() 操作是删除集合中最后一个元素，可是集合本身是无序的，你
  无法知道会删除哪个元素，因此这个操作得谨慎使用

#### 2.1.2 排序

- 对于字典，我们通常会根据键或值，进行升序或降序排序

  ```python
  d = {'b': 1, 'a': 2, 'c': 10}
  d_sorted_by_key = sorted(d.items(), key=lambda x: x[0]) # 根据字典键的升序排序
  d_sorted_by_value = sorted(d.items(), key=lambda x: x[1]) # 根据字典值的升序排序
  d_sorted_by_key
  [('a', 2), ('b', 1), ('c', 10)]
  d_sorted_by_value
  [('b', 1), ('a', 2), ('c', 10)]
  ```

- 对于集合，其排序和前面讲过的列表、元组很类似，直接调用 sorted(set) 即可，结果会返回一个排好序的列表

  ```python
  s = {3, 4, 2, 1}
  sorted(s) # 对集合的元素进行升序排序
  ```

### 2.2 性能

> 字典和集合是进行过性能高度优化的数据结构，特别是对于查找、添加和删除操作

假设列表有 n 个元素，而查找的过程要遍历列表，那么时间复杂度就为 O(n)。即使我们先对列表进行排序，然后使用二分查找，也会需要 O(logn) 的时间复杂度，更何况，列表的排序还需要 O(nlogn) 的时间。

```python
def find_product_price(products, product_id):
    for id, price in products:
        if id == product_id:
            return price
    return None

products = [
    (143121312, 100),
    (432314553, 30),
    (32421912367, 150)
]
print('The price of product 432314553 is {}'.format(find_product_price(products,432314553)))
```

但如果我们用字典来存储这些数据，那么查找就会非常便捷高效，只需 O(1) 的时间复杂度就可以完成。原因也很简单，刚刚提到过的，字典的内部组成是一张哈希表，你可以直接通过键的哈希值，找到其对应的值。

```python
products = {
143121312: 100,
432314553: 30,
32421912367: 150
}
print('The price of product 432314553 is {}'.format(products[432314553]))
```

### 2.3 工作原理

- 不同于其他数据结构，字典和集合的内部结构都是一张哈希表

  - 对于字典而言，这张表存储了哈希值（hash）、键和值这 3 个元素。
  - 对集合来说，区别就是哈希表内没有键和值的配对，只有单一的元素了。

- 为了提高存储空间的利用率，现在的哈希表除了字典本身的结构，会把索引和哈希值、键、值单独分开，也就是下面这样新的结构

  ```shell
  Indices
  ----------------------------------------------------
  None | index | None | None | index | None | index ...
  ----------------------------------------------------
  
  Entries
  --------------------
  hash0 key0 value0
  ---------------------
  hash1 key1 value1
  ---------------------
  hash2 key2 value2
  ---------------------
  ...
  ---------------------
  ```

### 2.4 插入操作

每次向字典或集合插入一个元素时，Python 会首先计算键的哈希值（hash(key)），再和mask = PyDicMinSize - 1 做与操作，计算这个元素应该插入哈希表的位置 index =hash(key) & mask。如果哈希表中此位置是空的，那么这个元素就会被插入其中。

而如果此位置已被占用，Python 便会比较两个元素的哈希值和键是否相等。

- 若两者都相等，则表明这个元素已经存在，如果值不同，则更新值。
- 若两者中有一个不相等，这种情况我们通常称为哈希冲突（hash collision），意思是两个元素的键不相等，但是哈希值相等。这种情况下，Python 便会继续寻找表中空余的位置，直到找到位置为止。

值得一提的是，通常来说，遇到这种情况，最简单的方式是线性寻找，即从这个位置开始，挨个往后寻找空位。当然，Python 内部对此进行了优化

### 2.5 查找操作

和前面的插入操作类似，Python 会根据哈希值，找到其应该处于的位置；然后，比较哈希表这个位置中元素的哈希值和键，与需要查找的元素是否相等。如果相等，则直接返回；如果不等，则继续查找，直到找到空位或者抛出异常为止。

### 2.6 删除操作

对于删除操作，Python 会暂时对这个位置的元素，赋于一个特殊的值，等到重新调整哈希表的大小时，再将其删除。

不难理解，哈希冲突的发生，往往会降低字典和集合操作的速度。因此，为了保证其高效性，字典和集合内的哈希表，通常会保证其至少留有 1/3 的剩余空间。随着元素的不停插入，当剩余空间小于 1/3 时，Python 会重新获取更大的内存空间，扩充哈希表。不过，这种情况下，表内所有的元素位置都会被重新排放。

虽然哈希冲突和哈希表大小的调整，都会导致速度减缓，但是这种情况发生的次数极少。所以，平均情况下，这仍能保证插入、查找和删除的时间复杂度为 O(1)。

```ad-summary
字典在 Python3.7+ 是有序的数据结构，而集合是无序的，其内部的哈希表存储结构，保证了其查找、插入、删除操作的高效性。所以，字典和集合通常运用在对元素的高效查找、去重等场景。
```

## 3. 字符串

### 3.1 基础

- 字符串是由独立字符组成的一个序列，通常包含在单引号（''）双引号（""）或者三引号之中（''' '''或""" """，两者一样）

- Python 中单引号、双引号和三引号的字符串是一模一样的，没有区别

- Python 也支持转义字符。所谓的转义字符，就是用反斜杠开头的字符串，来表示一
  些特定意义的字符

  | 转义字符 | 说明        |
  | -------- | ----------- |
  | \newline | 接下一行    |
  | \\\      | 表示 \      |
  | \\'      | 表示单引号' |
  | \\"      | 表示双引号  |
  | \\n      | 换行        |
  | \\t      | 横向制表符  |
  | \\b      | 退格        |
  | \\v      | 纵向制表符  |

### 3.2 常用操作

- 字符串的索引同样从 0 开始，index=0 表示第一个元素（字符），[index:index+2] 则表示第 index 个元素到 index+1 个元素组成的子字符串。

- 遍历字符串同样很简单，相当于遍历字符串中的每个字符。

- Python 的字符串是不可变的（immutable）。因此，用下面的操作，来改变一个字符串内部的字符是错误的，不允许的。

- Python 中字符串的改变，通常只能通过创建新的字符串来完成。比如上述例子中，想把'hello'的第一个字符'h'，改为大写的'H'，我们可以采用下面的做法：

  ```python
  s = 'H' + s[1:]
  s = s.replace('h', 'H')
  ```

  - 第一种方法，是直接用大写的'H'，通过加号'+'操作符，与原字符串切片操作的子字符串拼接而成新的字符串。
  - 第二种方法，是直接扫描原字符串，把小写的'h'替换成大写的'H'，得到新的字符串。

- 使用加法操作符'+='的字符串拼接方法,在写程序遇到字符串拼接时，如果使用’+='更方便，就放心地去用吧，不用过分担心效率问题了

- 除了使用加法操作符，我们还可以使用字符串内置的 join 函数。string.join(iterable)，表示把每个元素都按照指定的格式连接起来

- 常见的函数还有：

  - string.strip(str)，表示去掉首尾的 str 字符串；
  - string.lstrip(str)，表示只去掉开头的 str 字符串；
  - string.rstrip(str)，表示只去掉尾部的 str 字符串。
  - 从文件读进来的字符串中，开头和结尾都含有空字符，我们需要去掉它们，就可以用 strip() 函数
  - Python 中字符串还有很多常用操作，比如，string.find(sub, start, end)，表示从start 到 end 查找字符串中子字符串 sub 的位置

### 3.3 格式化

- 使用一个字符串作为模板，模板中会有格式符。这些格式符为后续真实值预留位置，以呈现出真实值应该呈现的格式。字符串的格式化，通常会用在程序的输出、logging等场景。

  ```python
  print('no data available for person with id: {}, name: {}'.format(id, name))
  ```

  其中的 string.format()，就是所谓的格式化函数；而大括号{}就是所谓的格式符，用来为后面的真实值——变量 name 预留位置

- string.format() 是最新的字符串格式函数与规范。自然，我们还有其他的表示方法，比如在 Python 之前版本中，字符串格式化通常用 % 来表示

  ```python
  print('no data available for person with id: %s, name: %s' % (id, name))
  ```

  其中 %s 表示字符串型，%d 表示整型等等，这些属于常识

  推荐使用 format 函数，毕竟这是最新规范，也是官方文档推荐的规范。

- 使用格式化函数，更加清晰、易读，并且更加规范，不易出错。

```ad_summary
Python 中字符串使用单引号、双引号或三引号表示，三者意义相同，并没有什么区别。其中，三引号的字符串通常用在多行字符串的场景。
Python 中字符串是不可变的（前面所讲的新版本 Python 中拼接操作’+='是个例外）。因此，随意改变字符串中字符的值，是不被允许的。
Python 新版本（2.5+）中，字符串的拼接变得比以前高效了许多，你可以放心使用。
Python 中字符串的格式化（string.format）常常用在输出、日志的记录等场景。
```

## 4. 输入与输出

> 在互联网上，没人知道你是一条狗。互联网刚刚兴起时，一根网线链接到你家，信息通过这条高速线缆直达你的屏幕，你通过键盘飞速回应朋友的消息，信息再次通过网线飞入错综复杂的虚拟世界，再进入朋友家。抽象来看，一台台的电脑就是一个个黑箱，黑箱有了输入和输出，就拥有了图灵机运作的必要条件。

### 4.1 基础

- input() 函数暂停程序运行，同时等待键盘输入；直到回车被按下，函数的参数即为提示语，输入的类型永远是字符串型（str）
- print() 函数则接受字符串、数字、字典、列表甚至一些自定义类的输出。
- **把 str 强制转换为 int 请用 int()，转为浮点数请用 float()。而在生产环境中使用强制转换时，请记得加上 try except（即错误和异常处理）**
- Python 对 int 类型没有最大限制（相比之下， C++ 的 int 最大为 2147483647，超过这个数字会产生溢出），但是对 float 类型依然有精度限制。这些特点，除了在一些算法竞赛中要注意，在生产环境中也要时刻提防，避免因为对边界条件判断不清而造成 bug 甚至0day（危重安全漏洞）。

### 4.2 文件输入输出

- 命令行的输入输出，只是 Python 交互的最基本方式，适用一些简单小程序的交互。而生产级别的 Python 代码，大部分 I/O 则来自于文件、网络、其他进程的消息等等。
- 计算机中文件访问的基础知识
  - 事实上，计算机内核（kernel）对文件的处理相对比较复杂，涉及到内核模式、虚拟文件系统、锁和指针等一系列概念
  - 先要用 open() 函数拿到文件的指针。其中，第一个参数指定文件位置（相对位置或者绝对位置）；第二个参数，如果是 'r'表示读取，如果是'w' 则表示写入，当然也可以用'rw' ，表示读写都要。a 则是一个不太常用（但也很有用）的参数，表示追加（append），这样打开的文件，如果需要写入，会从原始文件的最末尾开始写入。
  - **代码权限管理非常重要。如果你只需要读取文件，就不要请求写入权限。这样在某种程度上可以降低 bug 对整个系统带来的风险。**
  - 拿到指针后，我们可以通过 read() 函数，来读取文件的全部内容。代码 text = fin.read() ，即表示把文件所有内容读取到内存中，并赋值给变量 text。这么做自然也是有利有弊：
    - 优点是方便，接下来我们可以很方便地调用 parse 函数进行分析；
    - 缺点是如果文件过大，一次性读取可能造成内存崩溃。
  - 给 read 指定参数 size ，用来表示读取的最大长度。还可以通过 readline()函数，每次读取一行，这种做法常用于数据挖掘（Data Mining）中的数据清洗，在写一些小的程序时非常轻便。如果每行之间没有关联，这种做法也可以降低内存的压力。而write() 函数，可以把参数中的字符串输出到文件中
  - with 语句。open() 函数对应于 close() 函数，也就是说，如果你打开了文件，在完成读取任务后，就应该立刻关掉它。而如果你使用了with 语句，就不需要显式调用 close()。在 with 的语境下任务执行完毕后，close() 函数会被自动调用，代码也简洁很多
  - 所有 I/O 都应该进行错误处理。因为 I/O 操作可能会有各种各样的情况出现，而一个健壮（robust）的程序，需要能应对各种情况的发生，而不应该崩溃（故意设计的情况除外）。

### 4.3 JSON 序列化与实战

- JSON（JavaScript Object Notation）是一种轻量级的数据交换格式，它的设计意图是把所有事情都用设计的字符串来表示，这样既方便在互联网上传递信息，也方便人进行阅读（相比一些 binary 的协议）
  - 第一种，输入这些杂七杂八的信息，比如 Python 字典，输出一个字符串；
  - 第二种，输入这个字符串，可以输出包含原始信息的 Python 字典。

- json.dumps() 这个函数，接受 Python 的基本数据类型，然后将其序列化为 string；
- json.loads() 这个函数，接受一个合法字符串，然后将其反序列化为 Python 的基本数据类型。

- 输出字符串到文件，从文件中读取 JSON 字符串

  ```python
  import json
  params = {
  'symbol': '123456',
  'type': 'limit',
  'price': 123.4,
  'amount': 23
  }
  
  with open('params.json', 'w') as fout:
  	params_str = json.dump(params, fout)
  with open('params.json', 'r') as fin:
  	original_params = json.load(fin)
      
  print('after json deserialization')
  print('type of original_params = {}, original_params = {}'.format(type(original_params)
  ```

- 当开发一个第三方应用程序时，你可以通过 JSON 将用户的个人配置输出到文件，方便下次程序启动时自动读取。这也是现在普遍运用的成熟做法。

- Google，有类似的工具叫做 Protocol Buffer，相比于 JSON，它的优点是生成优化后的二进制文件，因此性能更好。但与此同时，生成的二进制序列，是不能直接阅读的。它在 TensorFlow 等很多对性能有要求的系统中都有广泛的应用。

```ad-summary
I/O 操作需谨慎，一定要进行充分的错误处理，并细心编码，防止出现编码漏洞；
编码时，对内存占用和磁盘占用要有充分的估计，这样在出错时可以更容易找到原因；
JSON 序列化是很方便的工具，要结合实战多多练习；
代码尽量简洁、清晰
```

## 5. 条件与循环

### 5.1 条件语句

```python
if x < 0:
	y = -x
else:
	y = x
```

- 在条件语句的末尾必须加上冒号（:）

- Python 中的表达是elif。

  ```python
  if condition_1:
  	statement_1
  elif condition_2:
  	statement_2
  ...
  elif condition_i:
  	statement_i
  else:
  	statement_n
  ```

  整个条件语句是顺序执行的，如果遇到一个条件满足，比如 condition_i 满足时，在执行完statement_i 后，便会退出整个 if、elif、else 条件语句，而不会继续向下执行

- 关于省略判断条件的常见用法

  | 数据类型            | 结果                                |
  | ------------------- | ----------------------------------- |
  | String              | 空字符串解析为False，其余为True     |
  | Int                 | 0解析为False，其余为True            |
  | Bool                | True为True，False为False            |
  | list/tuple/dict/set | Iterable为空解析为False，其余为True |
  | Object              | None解析为False，其余为True         |

  在实际写代码时，建议除了 boolean 类型的数据，条件判断最好是显性的

### 5.2 循环语句

- Python 中的循环一般通过 for 循环和 while 循环实现

  ```python
  l = [1, 2, 3, 4]
  for item in l:
  	print(item)
  ```

- Python 中的数据结构只要是可迭代的（iterable），比如列表、集合等等，那么都可以通过下面这种方式遍历

  ```python
  for item in <iterable>:
  	...
  ```

- 字典本身只有键是可迭代的，如果我们要遍历它的值或者是键值对，就需要通过其内置的函数 values() 或者 items() 实现。其中，values() 返回字典的值的集合，items() 返回键值对的集合。

- 通常通过 range() 这个函数，拿到索引，再去遍历访问集合中的元素

  ```python
  l = [1, 2, 3, 4, 5, 6, 7]
  for index in range(0, len(l)):
  	if index < 5:
  		print(l[index])
  ```

- Python 内置的函数enumerate()。用它来遍历集合，不仅返回每个元素，并且还返回其对应的索引

  ```python
  l = [1, 2, 3, 4, 5, 6, 7]
  for index, item in enumerate(l):
  	if index < 5:
  		print(item)
  ```

- 在循环语句中，我们还常常搭配 continue 和 break 一起使用。所谓 continue，就是让程序跳过当前这层循环，继续执行下面的循环；而 break 则是指完全跳出所在的整个循环体。在循环中适当加入 continue 和 break，往往能使程序更加简洁、易读。

  ```python
  # name_price: 产品名称 (str) 到价格 (int) 的映射字典
  # name_color: 产品名字 (str) 到颜色 (list of str) 的映射字典
  for name, price in name_price.items():
  	if price < 1000:
  		if name in name_color:
  			for color in name_color[name]:
  				if color != 'red':
  					print('name: {}, color: {}'.format(name, color))
  		else:
  			print('name: {}, color: {}'.format(name, 'None'))
  ```

  加入 continue 后，代码显然清晰了很多

  ```python
  # name_price: 产品名称 (str) 到价格 (int) 的映射字典
  # name_color: 产品名字 (str) 到颜色 (list of str) 的映射字典
  for name, price in name_price.items():
  if price >= 1000:
  	continue
  	if name not in name_color:
  		print('name: {}, color: {}'.format(name, 'None'))
  		continue
  	for color in name_color[name]:
  		if color == 'red':
  			continue
  		print('name: {}, color: {}'.format(name, color))
  ```

- 很多时候，for 循环和 while 循环可以互相转换,如果你只是遍历一个已知的集合，找出满足条件的元素，并进行相应的操作，那么使用 for 循环更加简洁。但如果你需要在满足某个条件前，不停地重复某些操作，并且没有特定的集合需要去遍历，那么一般则会使用 while 循环

  比如，某个交互式问答系统，用户输入文字，系统会根据内容做出相应的回答。为了实现这
  个功能，我们一般会使用 while 循环，大致代码如下

  ```python
  while True:
  	try:
  		text = input('Please enter your questions, enter "q" to exit')
  		if text == 'q':
  			print('Exit system')
  			break
  		...
  		...
  		print(response)
  except as err:
      print('Encountered error: {}'.format(err))
  	break
  ```

- for 循环的效率更胜一筹,range() 函数是直接由 C 语言写的，调用它速度非常快。while 循环中的“i+= 1”这个操作，得通过 Python 的解释器间接调用底层的 C 语言；并且这个简单的操作，又涉及到了对象的创建和删除（因为 i 是整型，是 immutable，i += 1 相当于 i =new int(i + 1)）

### 5.3 条件与循环的复用

- 在阅读代码的时候，你应该常常会发现，有很多将条件与循环并做一行的操作

  ```python
  expression1 if condition else expression2 for item in iterable
  ```

  将这个表达式分解开来，其实就等同于下面这样的嵌套结构：

  ```python
  for item in iterable:
  	if condition:
  		expression1
  	else:
  		expression2
  ```

  而如果没有 else 语句，则需要写成：

  ```python
  expression for item in iterable if condition
  ```

  比如我们要绘制 y = 2*|x| + 5 的函数图像，给定集合 x 的数据点，需要计算出y 的数据集合，那么只用一行代码，就可以很轻松地解决问题了

  ```python
  y = [value * 2 + 5 if value > 0 else -value * 2 + 5 for value in x]
  ```

  在处理文件中的字符串时，常常遇到的一个场景：将文件中逐行读取的一个完整语句，按逗号分割单词，去掉首位的空字符，并过滤掉长度小于等于 3 的单词，最后返回由单词组成的列表。这同样可以简洁地表达成一行

  ```python
  text = ' Today, is, Sunday'
  text_list = [s.strip() for s in text.split(',') if len(s.strip()) > 3]
  print(text_list)
  ```

  这样的复用并不仅仅局限于一个循环。比如，给定两个列表 x、y，要求返回 x、y 中
  所有元素对组成的元祖，相等情况除外

  ```python
  [(xx, yy) for xx in x for yy in y if xx != yy]
  # 等价于
  l = []
  for xx in x:
  	for yy in y:
  		if xx != yy:
  			l.append((xx, yy))
  ```

  ```ad-summary
  在条件语句中，if 可以单独使用，但是 elif 和 else 必须和 if 同时搭配使用；而 If 条件语句的判断，除了 boolean 类型外，其他的最好显示出来。
  在 for 循环中，如果需要同时访问索引和元素，你可以使用 enumerate() 函数来简化代码。
  写条件与循环时，合理利用 continue 或者 break 来避免复杂的嵌套，是十分重要的。
  要注意条件与循环的复用，简单功能往往可以用一行直接完成，极大地提高代码质量与效率。
  ```

## 6. 异常处理

### 6.1 错误与异常

- 程序中的错误至少包括两种，一种是语法错误，另一种则是异常。

  - 语法错误，代码不符合编程规范，无法被识别与执行，invalid syntax
  - 异常则是指程序的语法正确，也可以被执行，但在执行过程中遇到了错误，抛出了异常

  ZeroDivisionError NameError和TypeError，就是三种常见的异常类型

  [Python 中还有很多其他异常类型](https://docs.python.org/3/library/exceptions.html#bltin-exceptions)

### 6.2 处理异常

- 异常处理，通常使用 try 和 except 来解决

  ```python
  try:
  	s = input('please enter two numbers separated by comma: ')
  	num1 = int(s.split(',')[0].strip())
  	num2 = int(s.split(',')[1].strip())
  	...
  except ValueError as err:
  	print('Value Error: {}'.format(err))
  print('continue')
  ```

  except block 只接受与它相匹配的异常类型并执行，如果程序抛出的异常并不匹配，那么程序照样会终止并退出。

- 在 except block 中加入多种异常的类型，比如下面这样的写法

  ```python
  try:
  	s = input('please enter two numbers separated by comma: ')
  	num1 = int(s.split(',')[0].strip())
  	num2 = int(s.split(',')[1].strip())
  	...
  except (ValueError, IndexError) as err:
  	print('Error: {}'.format(err))
      
  print('continue')
  ...
  ```

  或者第二种写法：

  ```python
  try:
  	s = input('please enter two numbers separated by comma: ')
  	num1 = int(s.split(',')[0].strip())
  	num2 = int(s.split(',')[1].strip())
      ...
  except ValueError as err:
  	print('Value Error: {}'.format(err))
  except IndexError as err:
  	print('Index Error: {}'.format(err))
      
  print('continue')
  ...
  ```

  每次程序执行时，except block 中只要有一个 exception 类型与实际匹配即可

- **更通常的做法，是在最后一个 except block，声明其处理的异常类型是 Exception。Exception 是其他所有非系统异常的基类，能够匹配任意非系统异常**

  ```python
  try:
  	s = input('please enter two numbers separated by comma: ')
  	num1 = int(s.split(',')[0].strip())
  	num2 = int(s.split(',')[1].strip())
  	...
  except ValueError as err:
  	print('Value Error: {}'.format(err))
  except IndexError as err:
  	print('Index Error: {}'.format(err))
  except Exception as err:
  	print('Other error: {}'.format(err))
  print('continue')
  ...	
  ```

  也可以在 except 后面省略异常类型，这表示与任意异常相匹配（包括系统异常等）

  ```python
  try:
  	s = input('please enter two numbers separated by comma: ')
  	num1 = int(s.split(',')[0].strip())
  	num2 = int(s.split(',')[1].strip())
  	...
  except ValueError as err:
      print('Value Error: {}'.format(err))
  except IndexError as err:
  	print('Index Error: {}'.format(err))
  except:
  	print('Other error')
  print('continue')
  ...
  ```

- 当程序中存在多个 except block 时，最多只有一个 except block 会被执行。换句话说，如果多个 except 声明的异常类型都与实际相匹配，那么只有最前面的 exceptblock 会被执行，其他则被忽略。

- 异常处理中，还有一个很常见的用法是 finally，经常和 try、except 放在一起来用。无论发生什么情况，finally block 中的语句都会被执行，哪怕前面的 try 和 excep block 中使用了 return 语句。\

  一个常见的应用场景，便是文件的读取

  ```python
  import sys
  try:
  	f = open('file.txt', 'r')
  	.... # some data processing
  except OSError as err:
  	print('OS error: {}'.format(err))
  except:
  	print('Unexpected error:', sys.exc_info()[0])
  finally:
  	f.close()
  ```

  try block 尝试读取 file.txt 这个文件，并对其中的数据进行一系列的处理，到最后，无论是读取成功还是读取失败，程序都会执行 finally 中的语句——关闭这个文件流，确保文件的完整性。因此，在 finally 中，我们通常会放一些无论如何都要执行的语句。

### 6.3 用户自定义异常

- 下面这个例子，我们创建了自定义的异常类型 MyInputError，定义并实现了初始化函数和 str 函数（直接 print 时调用）

  ```python
  class MyInputError(Exception):
  	"""Exception raised when there're errors in input"""
  	def __init__(self, value): # 自定义异常类型的初始化
  		self.value = value
  	def __str__(self): # 自定义异常类型的 string 表达形式
  		return ("{} is invalid input".format(repr(self.value)))
  try:
  	raise MyInputError(1) # 抛出 MyInputError 这个异常
  except MyInputError as err:
  	print('error: {}'.format(err))
  ```

### 6.4 异常的使用场景与注意点

- 不确定某段代码能否成功执行，往往这个地方就需要使用异常处理

  大型社交网站的后台，需要针对用户发送的请求返回相应记录。用户记录往往储存在 keyvalue结构的数据库中，每次有请求过来后，我们拿到用户的 ID，并用 ID 查询数据库中此人的记录，就能返回相应的结果。

  而数据库返回的原始数据，往往是 json string 的形式，这就需要我们首先对 json string进行 decode（解码），你可能很容易想到下面的方法：

  ```python
  import json
  raw_data = queryDB(uid) # 根据用户的 id，返回相应的信息
  data = json.loads(raw_data)
  ```

  在 json.loads() 函数中，输入的字符串如果不符合其规范，那么便无法解码，就会抛出异常，因此加上异常处理十分必要。

  ```python
  try:
  	data = json.loads(raw_data)
  	....
  except JSONDecodeError as err:
  	print('JSONDecodeError: {}'.format(err))
  ```

  当你想要查找字典中某个键对应的值时，绝不能写成下面这种形式：

  ```python
  d = {'name': 'jason', 'age': 20}
  try:
  	value = d['dob']
  	...
  except KeyError as err:
  	print('KeyError: {}'.format(err))
  ```

  字典这个例子，写成下面这样就很好

  ```python
  if 'dob' in d:
  	value = d['dob']
  	...
  ```

```ad-summary
异常，通常是指程序运行的过程中遇到了错误，终止并退出。我们通常使用 try except语句去处理异常，这样程序就不会被终止，仍能继续执行。
处理异常时，如果有必须执行的语句，比如文件打开后必须关闭等等，则可以放在finally block 中。
异常处理，通常用在你不确定某段代码能否成功执行，也无法轻易判断的情况下，比如数据库的连接、读取等等。正常的 flow-control 逻辑，不要使用异常处理，直接用条件语句解决就可以了。
```

## 7. 自定义函数

