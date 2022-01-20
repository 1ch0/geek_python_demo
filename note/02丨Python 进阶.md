---
author: 1ch0
index_img:  https://raw.githubusercontent.com/1ch0/Figure-bed/main/img/python-programming.jpg
date: 2022-01-19-星期三 10:04
update: 2022-01-19-Wednesday 10:05:04
tags: Python
categories: Python
hide: false
title: Python核心技术与实战-进阶篇  
---

# Python核心技术与实战-进阶篇 

## 1. Python 对象的比较、拷贝

### 1.1 '==' VS 'is'

- 等于（==）和 is 是 Python 中对象比较常用的两种方式。简单来说，'=='操作符比较对象之间的值是否相等，如下面的例子，**表示比较变量 a 和 b 所指向的值是否相等**。

- 'is'操作符比较的是对象的身份标识是否相等，即**它们是否是同一个对象，是否指向同一个内存地址**。

  **在 Python 中，每个对象的身份标识，都能通过函数 id(object) 获得。因此，'is'操作符，相当于比较对象之间 ID 是否相等**

  ```python
  
  a = 10
  b = 10
  
  a == b
  True
  
  id(a)
  4427562448
  
  id(b)
  4427562448
  
  a is b
  True
  ```

  首先 Python 会为 10 这个值开辟一块内存，然后变量 a 和 b 同时指向这块内存区域，即 a 和 b 都是指向 10 个变量，因此 a 和 b 的值相等，id 也相等，a == b和a is b都返回 True。

  a is b为 True 的结论，只适用于 -5 到 256 范围内的数字

- 出于对性能优化的考虑，Python 内部会对 -5 到 256 的整型维持一个数组，起到一个缓存的作用。这样，每次你试图创建一个 -5 到 256 范围内的整型数字时，Python 都会从这个数组中返回相对应的引用，而不是重新开辟一块新的内存空间。

- 当我们比较变量时，使用'=='的次数会比'is'多得多，因为我们一般更关心两个变量的值，而不是它们内部的存储地址。但是，当我们比较一个变量与一个单例（singleton）时，通常会使用'is'。一个典型的例子，就是检查一个变量是否为 None：

  ```python
  
  if a is None:
        ...
  
  if a is not None:
        ...
  ```

- 比较操作符'is'的速度效率，通常要优于'=='。因为'is'操作符不能被重载，这样，Python 就不需要去寻找，程序中是否有其他地方重载了比较操作符，并去调用。执行比较操作符'is'，就仅仅是比较两个变量的 ID 而已。

- 但是'=='操作符却不同，执行a == b相当于是去执行a.__eq__(b)，而 Python 大部分的数据类型都会去重载__eq__这个函数，其内部的处理通常会复杂一些。比如，对于列表，__eq__函数会去遍历列表中的元素，比较它们的顺序和值是否相等。

- 元组是不可变的，但元组可以嵌套，它里面的元素可以是列表类型，列表是可变的，所以如果我们修改了元组中的某个可变元素，那么元组本身也就改变了，之前用'is'或者'=='操作符取得的结果，可能就不适用了。

### 1.2 浅拷贝和深度拷贝

- 浅拷贝。常见的浅拷贝的方法，是使用数据类型本身的构造器，比如下面两个例子

  ```python
  
  l1 = [1, 2, 3]
  l2 = list(l1)
  
  l2
  [1, 2, 3]
  
  l1 == l2
  True
  
  l1 is l2
  False
  
  s1 = set([1, 2, 3])
  s2 = set(s1)
  
  s2
  {1, 2, 3}
  
  s1 == s2
  True
  
  s1 is s2
  False
  ```

  l2 就是 l1 的浅拷贝，s2 是 s1 的浅拷贝。当然，对于可变的序列，我们还可以通过切片操作符':'完成浅拷贝，比如下面这个列表的例子

  ```python
  
  l1 = [1, 2, 3]
  l2 = l1[:]
  
  l1 == l2
  True
  
  l1 is l2
  False
  ```

  Python 中也提供了相对应的函数 copy.copy()，适用于任何数据类型

  ```python
  
  import copy
  l1 = [1, 2, 3]
  l2 = copy.copy(l1)
  ```

  需要注意的是，对于元组，使用 tuple() 或者切片操作符':'不会创建一份浅拷贝，相反，它会返回一个指向相同元组的引用

  ```python
  
  t1 = (1, 2, 3)
  t2 = tuple(t1)
  
  t1 == t2
  True
  
  t1 is t2
  True
  ```

  元组 (1, 2, 3) 只被创建一次，t1 和 t2 同时指向这个元组。

- 浅拷贝你应该很清楚了。浅拷贝，是指重新分配一块内存，创建一个新的对象，里面的元素是原对象中子对象的引用。因此，如果原对象中的元素不可变，那倒无所谓；但如果元素可变，浅拷贝通常会带来一些副作用，尤其需要注意

- 深度拷贝，是指重新分配一块内存，创建一个新的对象，并且将原对象中的元素，以递归的方式，通过创建新的子对象拷贝到新对象中。因此，新对象和原对象没有任何关联。

- Python 中以 copy.deepcopy() 来实现对象的深度拷贝。比如上述例子写成下面的形式，就是深度拷贝：

  ```python
  
  import copy
  l1 = [[1, 2], (30, 40)]
  l2 = copy.deepcopy(l1)
  l1.append(100)
  l1[0].append(3)
  
  l1
  [[1, 2, 3], (30, 40), 100]
  
  l2 
  [[1, 2], (30, 40)]
  ```

  深度拷贝也不是完美的，往往也会带来一系列问题。如果被拷贝对象中存在指向自身的引用，那么程序很容易陷入无限循环

  ```python
  
  import copy
  x = [1]
  x.append(x)
  
  x
  [1, [...]]
  
  y = copy.deepcopy(x)
  y
  [1, [...]]
  ```

  深度拷贝函数 deepcopy 中会维护一个字典，记录已经拷贝的对象与其 ID。拷贝过程中，如果字典里已经存储了将要拷贝的对象，则会从字典直接返回，我们来看相对应的源码就能明白

  ```python
  
  def deepcopy(x, memo=None, _nil=[]):
      """Deep copy operation on arbitrary Python objects.
        
    See the module's __doc__ string for more info.
    """
    
      if memo is None:
          memo = {}
      d = id(x) # 查询被拷贝对象x的id
    y = memo.get(d, _nil) # 查询字典里是否已经存储了该对象
    if y is not _nil:
        return y # 如果字典里已经存储了将要拷贝的对象，则直接返回
          ...    
  ```

```ad-summary
- 比较操作符'=='表示比较对象间的值是否相等，而'is'表示比较对象的标识是否相等，即它们是否指向同一个内存地址。
- 比较操作符'is'效率优于'=='，因为'is'操作符无法被重载，执行'is'操作只是简单的获取对象的 ID，并进行比较；而'=='操作符则会递归地遍历对象的所有值，并逐一比较。
- 浅拷贝中的元素，是原对象中子对象的引用，因此，如果原对象中的元素是可变的，改变其也会影响拷贝后的对象，存在一定的副作用。
- 深度拷贝则会递归地拷贝原对象中的每一个子对象，因此拷贝后的对象和原对象互不相关。另外，深度拷贝中会维护一个字典，记录已经拷贝的对象及其 ID，来提高效率并防止无限递归的发生。
```

## 2. 参数传递

### 2.1 值传递和引用传递

- 值传递，通常就是拷贝参数的值，然后传递给函数里的新变量。这样，原变量和新变量之间互相独立，互不影响。
- 引用传递，通常是指把参数的引用传给新的变量，这样，原变量和新变量就会指向同一块内存地址。如果改变了其中任何一个变量的值，那么另外一个变量也会相应地随之改变。

### 2.2 Python 变量及其赋值

- Python 里的变量可以被删除，但是对象无法被删除。

  ```python
  l = [1, 2, 3]
  del l
  ```

  del l 删除了 l 这个变量，从此以后你无法访问 l，但是对象[1, 2, 3]仍然存在。Python 程序运行时，其自带的垃圾回收系统会跟踪每个对象的引用。如果[1, 2, 3]除了 l 外，还在其他地方被引用，那就不会被回收，反之则会被回收。

- 变量的赋值，只是表示让变量指向了某个对象，并不表示拷贝对象给变量；

- 而一个对象，可以被多个变量所指向。可变对象（列表，字典，集合等等）的改变，会影响所有指向该对象的变量。

- 对于不可变对象（字符串、整型、元组等等），所有指向该对象的变量的值总是一样的，也不会改变。但是通过某些操作（+= 等等）更新不可变对象的值时，会返回一个新的对象。

- 变量可以被删除，但是对象无法被删除。

### 2.3 Python 函数的参数传递

- Python 的参数传递是赋值传递 （pass by assignment），或者叫作对象的引用传递（pass by object reference）。Python 里所有的数据类型都是对象，所以参数传递时，只是让新变量与原变量指向相同的对象而已，并不存在值传递或是引用传递一说。
- 改变变量和重新赋值的区别
  - 单纯地改变了对象的值，因此函数返回后，所有指向该对象的变量都会被改变；l2.append(4)
  - 但 my_func4() 中则创建了新的对象，并赋值给一个本地变量，因此原变量仍然不变 l2 = l2 + [4] return l2

```ad-summary
赋值或对象的引用传递，不是指向一个具体的内存地址，而是指向一个具体的对象。
- 如果对象是可变的，当其改变时，所有指向这个对象的变量都会改变。
- 如果对象不可变，简单的赋值只能改变其中一个变量的值，其余变量则不受影响。
如果你想通过一个函数来改变某个变量的值，通常有两种方法
- 一种是直接将可变数据类型（比如列表，字典，集合）当作参数传入，直接在其上修改
- 第二种则是创建一个新变量，来保存修改后的值，然后将其返回给原变量。
在实际工作中，我们更倾向于使用后者，因为其表达清晰明了，不易出错。

```

## 3. 装饰器

### 3.1 函数核心

- 在 Python 中，函数是一等公民（first-class citizen），函数也是对象。我们可以把函数赋予变量
- 可以把函数当作参数，传入另一个函数中
- 可以在函数里定义函数，也就是函数的嵌套
- 函数的返回值也可以是函数对象（闭包）
- 

### 3.2 装饰器

```python
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

def greet():
    print('hello')

greet = my_decorator(greet)
greet()
```

变量 greet 指向了内部函数 wrapper()，而内部函数 wrapper() 中又会调用原函数 greet()，因此，最后
调用 greet() 时，就会先打印'wrapper ofdecorator'，然后输出'hello world'。

这里的函数 my_decorator() 就是一个装饰器，它把真正需要执行的函数 greet() 包裹在其中，并且改变了它的行为，但是原函数 greet() 不变。

上述代码在 Python 中有更简单、更优雅的表示：

```python
def my_decorator(func):
    def wrapper():
        print('wrapper of decorator')
        func()
    return wrapper

@my_decorator
def greet():
    print('hello')

greet()
```

这里的@，我们称之为语法糖，@my_decorator就相当于前面的greet=my_decorator(greet)语句，只不过更加简洁.如果你的程序中有其它函数需要做类似的装饰，你只需在它们的上方加上@decorator就可以了，这样就大大提高了函数的重复利用和程序的可读性。

### 3.3 带参数的装饰器

- 一个简单的办法，是可以在对应的装饰器函数 wrapper()上，加上相应的参数

  ```python
  def my_decorator(func):
      def wrapper(message):
          print('wrapper of decorator')
          func(message)
      return wrapper
  
  @my_decorator
  def greet(message):
      print(message)
  
  greet('hello')
  ```

- 把\*args和**kwargs，作为装饰器内部函数 wrapper() 的参数。*args和**kwargs，表示接受任意数量和类型的参数，因此装饰器就可以写成下面的形式：

  ```python
  def my_decorator(func):
      def wrapper(*args, **kwargs):
          print('wrapper of decorator')
          func(*args, **kwargs)
      return wrapper
  
  @my_decorator
  def greet(a):
      print(a)
  greet('hello')
  ```

### 3.4 带有自定义参数的装饰器

装饰器可以接受原函数任意类型和数量的参数，除此之外，它还可以接受自己定义的参数。

```python
def repeat(num):
    def my_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decoraotr')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(4)
def greet(message):
    print(message)

greet('a')
```

### 3.5 原函数还是原函数吗

- 打印 greet() 函数的元信息

  ```python
  greet.__name__
  help(greet)
  ```

  greet() 函数被装饰以后，它的元信息变了。元信息告诉我们“它不再是以前的那个 greet() 函数，而是被
  wrapper() 函数取代了”。

- 通常使用内置的装饰器@functools.wrap，它会帮助保留原函数的元信息（也就是将原函数的元信息，拷贝到对应的装饰器函数里）

  ```python
  import functools
  
  def my_decorator(func):
      @functools.wraps(func)
      def wrapper(*args, **kwargs):
          print('wrapper of decorator')
          func(*args,**kwargs)
      return wrapper
  
  @my_decorator
  def greet(message):
      print(message)
  
  greet.__name__
  
  ```

### 3.6 类装饰器

- 类装饰器主要依赖于函数__call_()，每当你调用一个类的示例时，函数__call__()就会被执行一次。

  ```python
  class Count:
      def __init__(self, func):
          self.func = func
          self.num_calls = 0
  
      def __call__(self, *args, **kwargs):
          self.num_calls += 1
          print('num of calls is: {}'.format(self.num_calls))
          return self.func(*args, **kwargs)
  
  @Count
  def example():
      print("hello")
  
  example()
  ```

### 3.7 装饰器的嵌套

- Python 也支持多个装饰器

  ```python
  @decorator1
  @decorator2
  @decorator3
  def func():
  	...
  ```

  它的执行顺序从里到外，所以上面的语句也等效于下面这行代码：

  ```python
  decorator1(decorator2(decorator3(func)))
  ```

### 3.8 装饰器用法实例

#### 3.8.1 身份认证

```python
import functools

def authenticate(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        request = args[0]
        if check_user_logged_in(request):
            return func(*args, **kwargs)
        else:
            raise Exception('Authentication failed')
    return wrapper

@authenticate
def post_comment(request, ...):
    ...
```

定义了装饰器 authenticate；而函数post_comment()，则表示发表用户对某篇文章的评论。每
次调用这个函数前，都会先检查用户是否处于登录状态，如果是登录状态，则允许这项操作；如果没有登录，则不允许。

#### 3.8.2 日志记录

日志记录同样是很常见的一个案例。在实际工作中，如果你怀疑某些函数的耗时过长，导致整个系统的 latency（延迟）增加，所以想在线上测试某些函数的执行时间，那么，装饰器就是一种很常用的手段。

```python
import time
import functools

def log_execution_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        print('{} took {} ms'.format(func.__name__, (end-start)))
        return res
    return wrapper

@log_execution_time
def calculate_similarity(items):
    ...
```

#### 3.8.3 输入合理性检查

调用机器集群进行模型训练前，往往会用装饰器对其输入（往往是很长的 json 文件）进行合理性检。这样就可以大大避免，输入不正确对机器造成的巨大开销。

```python
import functools

def validation_check(input):
	@functools.wraps(func)
	def wrapper(*args, **kwargs):
		... # 检查输入是否合法
        
@validation_check
def neural_network_training(param1, param2, ...):
	...
```

### 3.9 缓存

以 Python 内置的 LRU cache 为例，LRU cache，在 Python 中的表示形式是@lru_cache。lru_cache会缓存进程中的函数参数和结果，当缓存满了以后，会删除 least recenly used 的数据。

```python
@lru_cache
def check(param1, param2, ...) # 检查用户设备类型，版本号
	...
```

```ad-summary
所谓的装饰器，其实就是通过装饰器函数，来修改原函数的一些功能，使得原函数不需要修改。
装饰器通常运用在身份认证、日志记录、输入合理性检查以及缓存等多个领域中。合理使用装饰器，往往能极大地提高程序的可读性以及运行效率。
```

## 4. metaclass

- meta-class 的 meta 这个词根，起源于希腊语词汇 meta，包含下面两种意思：
  - “Beyond”，例如技术词汇 metadata，意思是描述数据的超越数据；
  - “Change”，例如技术词汇 metamorphosis，意思是改变的形态。

- [YAML](https://pyyaml.org/wiki/PyYAMLDocumentation)是一个家喻户晓的 Python 工具，可以方便地序列化 / 逆序列化结构数据。YAMLObject 的一个**超越变形能力**，就是它的任意子类支持序列化和反序列化（serialization & deserialization）

  ```python
  ```

## 5. 迭代器和生成器

- 迭代器（iterator）提供了一个 next 的方法。调用这个方法后，你要么得到这个容器的下一个对象，要么得到一个 StopIteration 的错误

  ```python
  def is_iterable(param):
      try: 
          iter(param) 
          return True
      except TypeError:
          return False
   
  params = [
      1234,
      '1234',
      [1, 2, 3, 4],
      set([1, 2, 3, 4]),
      {1:1, 2:2, 3:3, 4:4},
      (1, 2, 3, 4)
  ]
      
  for param in params:
      print('{} is iterable? {}'.format(param, is_iterable(param)))
   
  ########## 输出 ##########
   
  1234 is iterable? False
  1234 is iterable? True
  [1, 2, 3, 4] is iterable? True
  {1, 2, 3, 4} is iterable? True
  {1: 1, 2: 2, 3: 3, 4: 4} is iterable? True
  (1, 2, 3, 4) is iterable? True
  ```

  **除了数字 1234 之外，其它的数据类型都是可迭代的。**

- 生成器
- **生成器是懒人版本的迭代器**
- 迭代器是一个有限集合，生成器则可以成为一个无限集。我只管调用 next()，生成器根据运算会自动生成新的元素，然后返回给你，非常便捷。
- 

```ad-summary
容器是可迭代对象，可迭代对象调用 iter() 函数，可以得到一个迭代器。迭代器可以通过 next() 函数来得到下一个元素，从而支持遍历。
生成器是一种特殊的迭代器（注意这个逻辑关系反之不成立）。使用生成器，你可以写出来更加清晰的代码；合理使用生成器，可以降低内存占用、优化程序结构、提高程序速度。
生成器在 Python 2 的版本上，是协程的一种重要实现方式；而 Python 3.5 引入 async await 语法糖后，生成器实现协程的方式就已经落后了。我们会在下节课，继续深入讲解 Python 协程。
```

## 6.  Python 协程

### 6.1 执行协程常用的三种方法

- 首先，我们可以通过 await 来调用。await 执行的效果，和 Python 正常执行是一样的，也就是说程序会阻塞在这里，进入被调用的协程函数，执行完毕返回后再继续，而这也是 await 的字面意思。代码中 `await asyncio.sleep(sleep_time)` 会在这里休息若干秒，`await crawl_page(url)` 则会执行 crawl_page() 函数。
- 其次，我们可以通过 asyncio.create_task() 来创建任务，这个我们下节课会详细讲一下，你先简单知道即可。
- 最后，我们需要 asyncio.run 来触发运行。asyncio.run 这个函数是 Python 3.7 之后才有的特性，可以让 Python 的协程接口变得非常简单，你不用去理会事件循环怎么定义和怎么使用的问题（我们会在下面讲）。一个非常好的编程规范是，asyncio.run(main()) 作为主程序的入口函数，在程序运行周期内，只调用一次 asyncio.run。

```ad-summary
协程和多线程的区别，主要在于两点，一是协程为单线程；二是协程由用户决定，在哪些地方交出控制权，切换到下一个任务。
协程的写法更加简洁清晰，把 async / await 语法和 create_task 结合来用，对于中小级别的并发需求已经毫无压力。
写协程程序的时候，你的脑海中要有清晰的事件循环概念，知道程序在什么时候需要暂停、等待 I/O，什么时候需要一并执行到底。
```















