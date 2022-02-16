---
author: 1ch0
index_img: https://raw.githubusercontent.com/1ch0/Figure-bed/main/img/python-programming.jpg
date: 2022-01-12 15:37
update: 2022-01-30-Sunday 10:00:41
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

### 7.1 函数基础

- 函数就是为了实现某一功能的代码段，只要写好以后，就可以重复利用

  ```python
  def my_func(message):
      print('Got a message: {}'.format(message))
  my_func('Hello')
  ```

  def 是函数的声明；
  my_func 是函数的名称；
  括号里面的 message 则是函数的参数；
  而 print 那行则是函数的主体部分，可以执行相应的语句；
  在函数最后，你可以返回调用结果（return 或 yield），也可以不返回。

  ```python
  def name(param1, param2, ..., paramN):
  	statements
  	return/yield value # optional
  ```

- 和其他需要编译的语言（比如 C 语言）不一样的是，def 是可执行语句，这意味着函数直到被调用前，都是不存在的。当程序调用函数时，def 语句才会创建一个新的函数对象，并赋予其名字。

- 主程序调用函数时，必须保证这个函数此前已经定义过，不然就会报错

- 但是，如果我们在函数内部调用其他函数，函数间哪个声明在前、哪个在后就无所谓，因为def 是可执行语句，函数在调用之前都不存在，我们只需保证调用时，所需的函数都已经声明定义

  ```python
  def my_func(message):
  	my_sub_func(message) # 调用 my_sub_func() 在其声明之前不影响程序执行
  def my_sub_func(message):
  	print('Got a message: {}'.format(message))
  my_func('hello world')
  ```
  
- Python 函数的参数可以设定默认值
  
  ```python
  def func(param = 0):
  	...
  ```

  在调用函数 func() 时，如果参数 param 没有传入，则参数默认为 0；而如果传入了参数 param，其就会覆盖默认值。
  
- **Python 是 dynamically typed 的，可以接受任何数据类型（整型，浮点，字符串等等）**

- Python 不用考虑输入的数据类型，而是将其交给具体的代码去判断执行，同样的一个函数（比如这边的相加函数 my_sum()），可以同时应用在整型、列表、字符串等等的操作中。

- **多态**，必要时请你在开头加上数据的类型检查

- Python 支持函数的嵌套。所谓的函数嵌套，就是指函数里面又有函数，比如：

  ```python
  def f1():
  	print('hello')
  	def f2():
  		print('world')
  	f2()
  f1()
  ```

- 函数嵌套

  - 第一，函数的嵌套能够保证内部函数的隐私。内部函数只能被外部函数所调用和访问，不会暴露在全局作用域，因此，如果你的函数内部有一些隐私数据（比如数据库的用户、密码等），不想暴露在外，那你就可以使用函数的的嵌套，将其封装在内部函数中，只通过外部函数来访问。

    ```python
    def connect_DB():
    	def get_DB_configuration():
    		...
    		return host, username, password
    	conn = connector.connect(get_DB_configuration())
    	return conn
    ```

  - 第二，合理的使用函数嵌套，能够提高程序的运行效率

    ```python
    def factorial(input):
    	# validation check
    	if not isinstance(input, int):
    		raise Exception('input must be an integer.')
    	if input < 0:
    		raise Exception('input must be greater or equal to 0' )
    	...
    
        def inner_factorial(input):
    		if input <= 1:
    			return 1
    		return input * inner_factorial(input-1)
    	return inner_factorial(input)
    
    print(factorial(5))
    ```

### 7.2 函数变量作用域

- Python 函数中变量的作用域和其他语言类似。如果变量是在函数内部定义的，就称为局部变量，只在函数内部有效。一旦函数执行完毕，局部变量就会被回收，无法访问

- 全局变量则是定义在整个文件层次上的

- **不能在函数内部随意改变全局变量的值**

- Python 的解释器会默认函数内部的变量为局部变量，但是又发现局部变量MIN_VALUE 并没有声明，因此就无法执行相关操作。所以，如果我们一定要在函数内部改变全局变量的值，就必须加上 global 这个声明：

  ```python
  MIN_VALUE = 1
  MAX_VALUE = 10
  def validation_check(value):
  	global MIN_VALUE
  	...
  	MIN_VALUE += 1
  	...
  validation_check(5)
  ```

  这里的 global 关键字，并不表示重新创建了一个全局变量 MIN_VALUE，而是告诉Python 解释器，函数内部的变量 MIN_VALUE，就是之前定义的全局变量，并不是新的全局变量，也不是局部变量。这样，程序就可以在函数内部访问全局变量，并修改它的值了。

- 如果遇到函数内部局部变量和全局变量同名的情况，那么在函数内部，局部变量会覆盖全局变量，比如下面这种

  ```python
  MIN_VALUE = 1
  MAX_VALUE = 10
  def validation_check(value):
  	MIN_VALUE = 3
  	...
  ```

- 对于嵌套函数来说，内部函数可以访问外部函数定义的变量，但是无法修改，若要修改，必须加上 **nonlocal** 这个关键字

  ```python
  def outer():
  	x = "local"
  	def inner():
  		nonlocal x # nonlocal 关键字表示这里的 x 就是外部函数 outer 定义的变量 x
  		x = 'nonlocal'
  		print("inner:", x)
  	inner()
  	print("outer:", x)
  outer()
  ```

- 如果不加上 nonlocal 这个关键字，而内部函数的变量又和外部函数变量同名，那么同样的，内部函数变量会覆盖外部函数的变量。

  ```python
  def outer():
  	x = "local"
  	def inner():
  		x = 'nonlocal' # 这里的 x 是 inner 这个函数的局部变量
  		print("inner:", x)
  	inner()
  	print("outer:", x)
  outer()	
  ```

### 7.3 闭包

- 闭包其实和刚刚讲的嵌套函数类似，不同的是，这里外部函数返回的是一个函数，而不是一个具体的值。返回的函数通常赋于一个变量，这个变量可以在后面被继续执行调用。

  计算一个数的 n 次幂

  ```python
  def nth_power(exponent):
  	def exponent_of(base):
  		return base ** exponent
  	return exponent_of # 返回值是 exponent_of 函数
  square = nth_power(2) # 计算一个数的平方
  cube = nth_power(3) # 计算一个数的立方
  square
  cube
  print(square(2)) # 计算 2 的平方
  print(cube(2)) # 计算 2 的立方
  ```

  这里外部函数 nth_power() 返回值，是函数 exponent_of()，而不是一个具体的数值。需要注意的是，在执行完square = nth_power(2)和cube = nth_power(3)后，外部函数 nth_power() 的参数 exponent，仍然会被内部函数 exponent_of() 记住。这样，之后我们调用 square(2) 或者 cube(2) 时，程序就能顺利地输出结果，而不会报错说参数exponent 没有定义了。

- **使用闭包的一个原因，是让程序变得更简洁易读**

```ad-summary
1. Python 中函数的参数可以接受任意的数据类型，使用起来需要注意，必要时请在函数开头加入数据类型的检查；
2. 和其他语言不同，Python 中函数的参数可以设定默认值；
3. 嵌套函数的使用，能保证数据的隐私性，提高程序运行效率；
4. 合理地使用闭包，则可以简化程序的复杂度，提高可读性。
```

## 8. 匿名函数

### 8.1 基础

- 匿名函数的格式：`lambda argument1, argument2,... argumentN : expression`

- 匿名函数的关键字是 lambda，之后是一系列的参数，然后用冒号隔开，最后则是由这些参数组成的表达式

  ```python
  square = lambda x: x**2
  square(3)
  ```
  
- 与常规函数区别
  
  - 第一，lambda 是一个表达式（expression），并不是一个语句（statement）。lambda 可以用在一些常规函数 def 不能用的地方，比如，lambda 可以用在列表内部，而常规函数却不能
  
    ```python
    [(lambda x: x*x)(x) for x in range(10)]
    ```
  
    lambda 可以被用作某些函数的参数，而常规函数 def 也不能
  
    ```python
    l = [(1, 20), (3, 0), (9, 10), (2, -1)]
    l.sort(key=lambda x: x[1]) # 按列表中元祖的第二个元素排序
    print(l)
    ```
  
    常规函数 def 必须通过其函数名被调用，因此必须首先被定义。但是作为一个表达式的
    lambda，返回的函数对象就不需要名字了。
  
  - 第二，lambda 的主体是只有一行的简单表达式，并不能扩展成一个多行的代码块。
  
    这其实是出于设计的考虑。Python 之所以发明 lambda，就是为了让它和常规函数各司其职：lambda 专注于简单的任务，而常规函数则负责更复杂的多行逻辑
  
### 8.2 为什么使用匿名函数 

- 使用匿名函数 lambda，可以帮助我们大大简化代码的复杂度，提高代码的可读性。

### 8.3 函数式编程

- 函数式编程，是指代码中每一块都是不可变的（immutable），都由纯函数（purefunction）的形式组成。这里的纯函数，是指函数本身相互独立、互不影响，对于相同的输入，总会有相同的输出，没有任何副作用。

- 函数式编程的优点，主要在于其纯函数和不可变的特性使程序更加健壮，易于调试（debug）和测试；缺点主要在于限制多，难写。

- map(function, iterable) 函数

  - 对 iterable 中的每个元素，都运用 function 这个函数，最后返回一个新的可遍历的集合。

    要对列表中的每个元素乘以 2，那么用 map 就可以表示为下面这样

    ```python
    l = [1, 2, 3, 4, 5]
    new_list = map(lambda x: x * 2, l) # [2， 4， 6， 8， 10]
    ```

    我们可以以 map() 函数为例，看一下 Python 提供的函数式编程接口的性能。还是同样的列表例子，它还可以用 for 循环和 list comprehension（目前没有统一中文叫法，你也可以直译为列表理解等）实现，我们来比较一下它们的速度：

    ```shell
    python3 -mtimeit -s'xs=range(1000000)' 'map(lambda x: x*2, xs)'
    
    python3 -mtimeit -s'xs=range(1000000)' '[x * 2 for x in xs]'
    
    python3 -mtimeit -s'xs=range(1000000)' 'l = []' 'for i in xs: l.append(i * 2)'
    ```

    **map() 是最快的。因为 map() 函数直接由 C 语言写的，运行时不需要通过Python 解释器间接调用，并且内部做了诸多优化，所以运行速度最快。**

- filter(function, iterable) 函数

  - 它和 map 函数类似，function 同样表示一个函数对象。filter() 函数表示对 iterable 中的每个元素，都使用 function 判断，并返回True 或者 False，最后将返回 True 的元素组成一个新的可遍历的集合。

    返回一个列表中的所有偶数，可以写成下面这样

    ```python
    l = [1, 2, 3, 4, 5]
    new_list = filter(lambda x: x % 2 == 0, l) # [2, 4]
    ```

- reduce(function, iterable) 函数

  - function 同样是一个函数对象，规定它有两个参数，表示对 iterable 中的每个元素以及上一次调用后的结果，运用 function 进行计算，所以最后返回的是一个单独的数值。

    ```python
    l = [1, 2, 3, 4, 5]
    product = reduce(lambda x, y: x * y, l) # 1*2*3*4*5 = 120
    ```
    
```ad-summary
匿名函数 lambda，它的主要用途是减少代码的复杂度。需要注意的是 lambda 是一个表达式，并不是一个语句；它只能写成一行的表达形式，语法上并不支持多行。匿名函数通常的使用场景是：程序中需要使用一个函数完成一个
简单的功能，并且该函数只调用一次。
Python 的函数式编程，主要了解了常见的 map()，fiilter() 和reduce() 三个函数，并比较了它们与其他形式（for 循环，comprehension）的性能，显然，它们的性能效率是最优的。
```

## 9. 面向对象

### 9.1 基础

- 基本概念
  - 类，一群有着相同属性和函数的对象的集合。
  - 对象：集合中的一个事物，这里对应由 class 生成的某一个 object。
  - 属性：对象的某个静态特征。
  - 函数：对象的某个动态能力。

### 9.2 代码示例

- 如何在一个类中定义一些常量，每个对象都可以方便访问这些常量而不用重新构造？

  在 Python 的类里，你只需要和函数并列地声明并赋值，就可以实现这一点，例如这段代码中的 WELCOME_STR。一种很常规的做法，是用全大写来表示常量，因此我们可以在类中使用 self.WELCOME_STR ，或者在类外使用 Entity.WELCOME_STR ，来表达这个字符串。

- 如果一个函数不涉及到访问修改这个类的属性，而放到类外面有点不恰当，怎么做才能更优雅呢？

  提出了类函数、成员函数和静态函数三个概念。它们其实很好理解，前两者产生的影响是动态的，能够访问或者修改对象的属性；而静态函数则与类没有什么关联，最明显的特征便是，静态函数的第一个参数没有任何特殊性。

  ```python
  # 类函数
  @classmethod
  
  # 静态函数
  @staticmethod
  ```

  - 一般而言，静态函数可以用来做一些简单独立的任务，既方便测试，也能优化代码结构。静态函数还可以通过在函数前一行加上 @staticmethod 来表示

  - 类函数的第一个参数一般为 cls，表示必须传一个类进来。类函数最常用的功能是实现不同的 init 构造函数,类函数需要装饰器 @classmethod 来声明
  - 成员函数则是我们最正常的类的函数，它不需要任何装饰器声明，第一个参数 self 代表当前对象的引用，可以通过此函数，来实现想要的查询 / 修改类的属性等功能。

- 既然类是一群相似的对象的集合，那么可不可以是一群相似的类的集合呢？

### 9.3 继承

- 类的继承，顾名思义，指的是一个类既拥有另一个类的特征，也拥有不同于另一个类的独特特征。在这里的第一个类叫做子类，另一个叫做父类，特征其实就是类的属性和函数。
- 首先需要注意的是构造函数。每个类都有构造函数，继承类在生成对象的时候，是不会自动调用父类的构造函数的，因此你必须在 init() 函数中显式调用父类的构造函数。它们的执行顺序是 子类的构造函数 -> 父类的构造函数。
- 减少重复的代码，降低系统的熵值（即复杂度）。
- 抽象类是一种特殊的类，它生下来就是作为父类存在的，一旦对象化就会报错。同样，抽象函数定义在抽象类之中，子类必须重写该函数才能使用。相应的抽象函数，则是使用装饰器@abstractmethod 来表示。
- **软件工程中一个很重要的概念，定义接口**
- **抽象类就是这么一种存在，它是一种自上而下的设计风范，你只需要用少量的代码描述清楚要做的事情，定义好接口，然后就可以交给不同开发人员去开发和对接。**

```ad-summary
面向对象编程是软件工程中重要的思想。正如动态规划是算法中的重要思想一样，它不是某一种非常具体的技术，而是一种综合能力的体现，是将大型工程解耦化、模块化的重要方法。在实践中要多想，尤其是抽象地想，才能更快掌握这个技巧。
```

## 10. 面向对象 - 实现一个搜索引擎

### 10.1 基础

- 一个搜索引擎由搜索器、索引器、检索器和用户接口四个部分组成。
- 搜索器，通俗来讲就是我们常提到的爬虫（scrawler），它能在互联网上大量爬取各类网站的内容，送给索引器。索引器拿到网页和内容后，会对内容进行处理，形成索引（index），存储于内部的数据库等待检索。

### 10.2 Bag of Words 和 Inverted Index

- BOW Model，即 [Bag of Words Model](https://en.wikipedia.org/wiki/Bag-of-words_model)，词袋模型
- Inverted Index Model，即倒序索引，是非常有名的搜索引擎方法

### 10.3 LRU 和多重继承

- LRU 缓存是一种很经典的缓存（同时，LRU 的实现也是硅谷大厂常考的算法面试题，这里为了简单，我直接使用 pylru 这个包），它符合自然界的局部性原理，可以保留最近使用过的对象，而逐渐淘汰掉很久没有被用过的对象。
- 多重继承有两种初始化方法
  - 第一种，super(BOWInvertedIndexEngineWithCache, self).__init__()直接初始化该类的第一个父类，不过使用这种方法时，要求继承链的最顶层父类必须要继承object；
  - 第二种，对于多重继承，如果有多个构造函数需要调用， 我们就必须用传统的方法LRUCache.__init__(self) 
- 

## 11. Python 模块化

### 11.1 简单模块化

- 最简单的模块化方式，你可以把函数、类、常量拆分到不同的文件，把它们放在同一个文件夹，然后使用 from your_file import function_name, class_name 的方式调用。之后，这些函数和类就可以在文件内直接使用了。
- import 同一个模块只会被执行一次，这样就可以防止重复导入模块出现问题。当然，良好的编程习惯应该杜绝代码多次导入的情况。在 Facebook 的编程规范中，除了一些极其特殊的情况，import 必须位于程序的最前端。
- 在 Python 3 规范中，__init__.py 并不是必须的

### 11.2 项目模块化

- 固定一个确定路径对大型工程来说是非常必要的
- 事实上，在 Facebook 和 Google，整个公司都只有一个代码仓库，全公司的代码都放在这个库里
  - 第一个优点，简化依赖管理。整个公司的代码模块，都可以被你写的任何程序所调用，而你写的库和模块也会被其他人调用。调用的方式，都是从代码的根目录开始索引，也就是前面提到过的相对的绝对路径。这样极大地提高了代码的分享共用能力，你不需要重复造轮子，只需要在写之前，去搜一下有没有已经实现好的包或者框架就可以了。
  - 第二个优点，版本统一。不存在使用了一个新模块，却导致一系列函数崩溃的情况；并且所有的升级都需要通过单元测试才可以继续。
  - 第三个优点，代码追溯。你可以很容易追溯，一个 API 是从哪里被调用的，它的历史版本是怎样迭代开发，产生变化的。

- Python 解释器在遇到 import 的时候，它会在一个特定的列表中寻找模块。这个特定的列表，可以用下面的方式拿到：

  ```python
  import sys
  print(sys.path)
  ```

  它的第一项为空。其实，Pycharm 做的一件事，就是将第一项设置为项目根目录的绝对地址。这样，每次你无论怎么运行 main.py，import 函数在执行的时候，都会去项目根目录中找相应的包。

- 使得普通的 Python 运行环境也能做到？这里有两种方法可以做到：

  ```python
  import sys
  sys.path[0] = '/home/ubuntu/workspace/your_projects'
  ```

  第一种方法，“大力出奇迹”，我们可以强行修改这个位置，这样，你的 import 接下来肯定就畅通无阻了。但这显然不是最佳解决方案，把绝对路径写到代码里，是我非常不推荐的方式（你可以写到配置文件中，但找配置文件也需要路径寻找，于是就会进入无解的死循环）。

  第二种方法，是修改 PYTHONHOME。这里我稍微提一下 Python 的 Virtual Environment（虚拟运行环境）

  回到第二种修改方法上。在一个 Virtual Environment 里，你能找到一个文件叫activate，在这个文件的末尾，填上下面的内容：

  ```python
  export PYTHONPATH="/home/ubuntu/workspace/your_projects"
  ```

  这样，每次你通过 activate 激活这个运行时环境的时候，它就会自动将项目的根目录添加到搜索路径中去。

### 11.3 神奇的 if __name__ == '__main__'

- Python 是脚本语言，和 C++、Java 最大的不同在于，不需要显式提供 main() 函数入口

- import 在导入文件的时候，会自动把所有暴露在外面的代码全都执行一遍。因此，如果你要把一个东西封装成模块，又想让它可以执行的话，你必须将要执行的代码放在 if \__name__ == '\__main__'下面。

- \__name__ 作为 Python 的魔术内置参数，本质上是模块对象的一个属性。我们使用 import 语句时，__name__ 就会被赋值为该模块的名字，自然就不等于__main__了。

  ```python
  if __name__ == '__main__'
  ```

```ad-summary
1. 通过绝对路径和相对路径，我们可以 import 模块；
2. 在大型工程中模块化非常重要，模块的索引要通过绝对路径来做，而绝对路径从程序的根目录开始；
3. 记着巧用if __name__ == '__main__'来避开 import 时执行。
```



