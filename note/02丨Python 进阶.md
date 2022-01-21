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

  ```python
  import asyncio
   
  async def crawl_page(url):
      print('crawling {}'.format(url))
      sleep_time = int(url.split('_')[-1])
      await asyncio.sleep(sleep_time)
      print('OK {}'.format(url))
   
  async def main(urls):
      tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
      await asyncio.gather(*tasks)
   
  %time asyncio.run(main(['url_1', 'url_2', 'url_3', 'url_4']))
  ```

  

```ad-summary
协程和多线程的区别，主要在于两点，一是协程为单线程；二是协程由用户决定，在哪些地方交出控制权，切换到下一个任务。
协程的写法更加简洁清晰，把 async / await 语法和 create_task 结合来用，对于中小级别的并发需求已经毫无压力。
写协程程序的时候，你的脑海中要有清晰的事件循环概念，知道程序在什么时候需要暂停、等待 I/O，什么时候需要一并执行到底。
```

## 7. 并发编程 - Futures

### 7.1 并发和并行

并发（Concurrency）和并行（Parallelism）

- 在 Python 中，并发并不是指同一时刻有多个操作（thread、task）同时进行。相反，某个特定的时刻，它只允许有一个操作发生，只不过线程 / 任务之间会互相切换，直到完成。

![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABlQAAAIMCAYAAACDnEExAAAgAElEQVR4AezdCfzsU/04/nO5JOFeS30Rbt+E7FukZA8pa9KCkIoUslaISz/+fLOGskQIZStbi5uUrRDKEtnda0nKci/iJnz+j9ep95jP/pn5zMx7PjPP83hcM/Oe9/uc93me93zm7bzmnDOup6enJ9WQZsyYkSZMmFDDEY3ZtdvKnTZtWpo0aVJj8GrIpducy6qv9q3hohzFrtp3FHg1HFqWc1nl+vzWcHGMYlftOwq8Gg4ty7mscn1+a7g4RrGr9h0FXg2HluVcVrk+vzVcHKPYVfuOAq+GQ8tyLqtcn98aLo5R7Kp9R4FXw6FlOZdVrs9vDRfHKHbVvqPAq+HQRjnPUkOZdiVAgAABAgQIECBAgAABAgQIECBAgAABAgQIdKWAgEpXNrtKEyBAgAABAgQIECBAgAABAgQIECBAgAABArUIjJs6dWpNU37Vkrl9CRAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQKdIDDOGipDN2Oj5lYbupT+75qjsL9JM7Zo32ao9s+zLOeyyvX57X8NNGOL9m2Gav88y3Iuq1yf3/7XQDO2aN9mqPbPsyznssr1+e1/DTRji/Zthmr/PMtyLqtcn9/+10AztmjfZqj2z7Ms57LK9fntfw00Y4v2bYZq/zzLci6rXJ/f/tfASLaY8mskSvYhQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEulpAQKWrm1/lCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgZEICKiMRMk+BAgQIECAAAECBAgQIECAAAECBAgQIECAQFcLCKh0dfOrPAECBAgQIECAAAECBAgQIECAAAECBAgQIDASAQGVkSjZhwABAgQIECBAgAABAgQIECBAgAABAgQIEOhqAQGVrm5+lSdAgAABAgQIECBAgAABAgQIECBAgAABAgRGIiCgMhIl+xAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJdLSCg0tXNr/IECBAgQIAAAQIECBAgQIAAAQIECBAgQIDASAQEVEaiZB8CBAgQIECAAAECBAgQIECAAAECBAgQIECgqwUEVLq6+VWeAAECBAgQIECAAAECBAgQIECAAAECBAgQGImAgMpIlOxDgAABAgQIECBAgAABAgQIECBAgAABAgQIdLWAgEpXN7/KEyBAgAABAgQIECBAgAABAgQIECBAgAABAiMREFAZiZJ9CBAgQIAAAQIECBAgQIAAAQIECBAgQIAAga4WEFDp6uZXeQIECBAgQIAAAQIECBAgQIAAAQIECBAgQGAkAgIqI1GyDwECBAgQIECAAAECBAgQIECAAAECBAgQINDVAgIqXd38Kk+AAAECBAgQIECAAAECBAgQIECAAAECBAiMREBAZSRK9iFAgAABAgQIECBAgAABAgQIECBAgAABAgS6WkBApaubX+UJECBAgAABAgQIECBAgAABAgQIECBAgACBkQgIqIxEyT4ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAVwsIqHR186s8AQIECBAgQIAAAQIECBAgQIAAAQIECBAgMBIBAZWRKNmHAAECBAgQIECAAAECBAgQIECAAAECBAgQ6GoBAZWubn6VJ0CAAAECBAgQIECAAAECBAgQIECAAAECBEYiIKAyEiX7ECBAgAABAgQIECBAgAABAgQIECBAgAABAl0tIKDS1c2v8gQIECBAgAABAgQIECBAgAABAgQIECBAgMBIBARURqJkHwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCrBQRUurr5VZ4AAQIECBAgQIAAAQIECBAgQIAAAQIECBAYiYCAykiU7EOAAAECBAgQIECAAAECBAgQIECAAAECBAh0tYCASlc3v8oTIECAAAECBAgQIECAAAECBAgQIECAAAECIxEYN3369J6R7Gif1gpMnz49TZw4sbWFKq1lAtq3ZdSlFKR9S2FvWaHat2XUpRSkfUthb1mh2rdl1KUUpH1LYW9Zodq3ZdSlFKR9S2FvWaHat2XUpRSkfUthb1mh2rdl1KUUpH3rYx8/YcKEmo6cMWNGqvWYmgoYZOduKzcuaM6DXAwN3FzWdaV9G9iIQ2SlfYfAaeBbZTmXVa7PbwMvniGy0r5D4DTwrbKcyyrX57eBF88QWWnfIXAa+FZZzmWV6/PbwItniKy07xA4DXyrLOeyyvX5beDFM0RW2ncInAa+VZZzWeX6/Dbw4hkiK+07BE4D32qUsym/GtgosiJAgAABAgQIECBAgAABAgQIECBAgAABAgQ6U0BApTPbVa0IECBAgAABAgQIECBAgAABAgQIECBAgACBBgoIqDQQU1YECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAZwoIqHRmu6oVAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0EABAZUGYsqKAAECBAgQIECAAAECBAgQIECAAAECBAgQ6EwBAZXObFe1IkCAAAECBAgQIECAAAECBAgQIECAAAECBBooIKDSQExZESBAgAABAgQIECBAgAABAgQIECBAgAABAp0pIKDSme2qVgQIECBAgAABAgQIECBAgAABAgQIECBAgEADBQRUGogpKwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKAzBQRUOrNd1YoAAQIECBAgQIAAAQIECBAgQIAAAQIECBBooICASgMxZUWAAAECBAgQIECAAAECBAgQIECAAAECBAh0poCASme2q1oRIECAAAECBAgQIECAAAECBAgQIECAAAECDRQQUGkgpqwIECBAgAABAgQIECBAgAABAgQIECBAgACBzhQQUOnMdlUrAgQIECBAgAABAgQIECBAgAABAgQIECBAoIECAioNxJQVAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0JkCAiqd2a5qRYAAAQIECBAgQIAAAQIECBAgQIAAAQIECDRQQEClgZiyIkCAAAECBAgQIECAAAECBAgQIECAAAECBDpTQEClM9tVrQgQIECAAAECBAgQIECAAAECBAgQIECAAIEGCgioNBBTVgQIECBAgAABAgQIECBAgAABAgQIECBAgEBnCgiodGa7qhUBAgQIECBAgAABAgQIECBAgAABAgQIECDQQAEBlQZiyooAAQIECBAgQIAAAQIECBAgQIAAAQIECBDoTAEBlc5sV7UiQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEGiggoNJATFkRIECAAAECBAgQIECAAAECBAgQIECAAAECnSkgoNKZ7apWBAgQIECAAAECBAgQIECAAAECBAgQIECAQAMFBFQaiCkrAgQIECBAgAABAgQIECBAgAABAgQIECBAoDMFBFQ6s13VigABAgQIECBAgAABAgQIECBAgAABAgQIEGiggIBKAzFlRYAAAQIECBAgQIAAAQIECBAgQIAAAQIECHSmgIBKZ7arWhEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQINFBg3ffr0ngbmJ6sGCUyfPj1NnDixQbnJpt0EtG+7tUhjz0f7Ntaz3XLTvu3WIo09H+3bWM92y037tluLNPZ8tG9jPdstN+3bbi3S2PPRvo31bLfctG+7tUhjz0f7Ntaz3XLTvu3WIo09H+1bn+f4CRMm1HTkjBkzUq3H1FTAIDt3W7lxQXMe5GJo4Oayrivt28BGHCIr7TsETgPfKsu5rHJ9fht48QyRlfYdAqeBb5XlXFa5jfr83n333enZZ5+ttMSKK66Y5p133srrvk/Kqm+3lduo9u3bfsO97jbnsuqrfYe7EhvzvvZtjONwuZTlXFa5Pr/DXRGNeV/7NsZxuFzKci6rXJ/f4a6IxryvfRvjOFwujXIeP1xB3idAgAABAgQIECBA4E2BW2+9NV111VXpiiuuSK+++mr61a9+lT784Q+/uYNnBAgQIECAAAECBAgQINCRAtZQ6chmVSkCBAgQIECAQOcI3HHHHWn55ZfPo0BmmWWWVP1v1llnTYssskhad91108EHH5xi9Eiz084775wuvPDCfD49PT0pzkEiQIAAAQIECBAgQIAAgc4XEFDp/DZWQwIECBAgQIDAmBZYaaWV0l133ZWee+65ShBju+22S3feeWf69a9/nY488si04IILpsMPPzytuuqq6YQTTmh6fceNG1cpQ0ClQuEJAQIECBAgQIAAAQIEOlrAlF8d3bwqR4AAAQIECBDoDIHqAEbUKIIYMWqlSNtvv3165zvfmY477ri0zz77pDXWWCP/K96v9/H222/P66VstNFGg2YhoDIojTcIECBAgAABAgQIECDQUQJGqHRUc6oMAQIECBAgQKA7BSLgEiNUJkyYkGIarqOOOqohEHvssUdeI2WozGIKMokAAQIECBAgQIAAAQIEOl/A//11fhurIQECBAgQIECgKwTe+ta3ptVXXz3X9YEHHhh1nWM6sZtuumnYfEYzQuWJJ55I119/fbr55ptzIGjYwpq0w2uvvZbC7LbbbksvvPDCsKW88sor6ZZbbknXXntt+sc//jHs/qPZ4dVXX01/+ctf0h//+Mf00ksvjSarER376KOPpn/961+D7hsBuwcffDC98cYb/fZ58cUX0+9///t0ww03pDBtVgqHGD0Vbfbvf/+7WcXIlwABAgQIECBAgACBPgICKn1AvCRAgAABAgQIEBi7Am95y1vyycd6K5H+7//+L6233nr536c//en8uO2226YICER67LHH0sc//vHKPltvvXX67W9/m/baa6/0uc99Lu8TC9AXefzsZz/L26r/8/rrr6ezzz47rb322imCOjFiJaYji471gVJ0tH//+99PSy+9dFpsscXSuuuumz74wQ+mJZdcMv3whz/sdcitt96a1l9//Ur50ZF/wQUX5G1zzjlnnvrsU5/6VA449DpwhC+mTp2aYrq0eeaZJ733ve/NAamJEyem+eefP22++eb9crn33nvTZz/72TwS6AMf+EA+j6jDrrvumv7+97/32j/yLdyOPfbYfI677LJLmjRpUjb63//933Tqqaem8Bsoxbo50TZxbssuu2x63/vel5+/4x3vSDvuuGM+ZL/99quUEedVnU466aS0wQYbVN6PwFWk6dOnV7bF+UXbRTrttNNSnNN73vOeHOAqzj0ef/rTn+aA1/HHH58WXXTRbPXyyy/n4+I/kUes9RN2H/rQh9I666yTllhiiXT55ZdX9olAzYc//OFK2b/73e/SL37xi/Sxj30s1yuumzjf4jwrB1Y9+fGPf5ze//735/0jr2izuObe9a53pR/84Ad5naENN9ywUkace7w+//zzK7mcccYZlfOIPGKKPIkAAQIECBAgQIAAgZEJCKiMzMleBAgQIECAAAECY0AgAg6RotM+0le/+tW06aab5pEUMQrk85//fO5cjk7oSBEMuPjii3MwJDq843mMctlyyy1zJ37sE8GOyZMn53+x6H3fdMABB+QgTAQ+ooN/ueWWS3/+859z5/jjjz/ea/cI5ESn+W677ZYieHPnnXemv/3tbzmQEqMidtppp3TYYYdVjllttdVSBAYiuBCjQQ488MB033335fPdd999c1DmoosuSqusskrqW1Ylk0GeRLAm6hMBoygzynj22WdTBI3CL15Xp/POOy8Hih555JF02WWX5c776Pz/xCc+kU4//fQcSIhgRZG++93v5uBEnHe8f+6556aFF144B6oi2DJt2rT05S9/OR1yyCHFIZXH3/zmN9l9ypQp6ZhjjkkRyImRMFFuBC3uueeevO+RRx6ZA0JRRrRvdYrp2qJuDz30UK+RNHF8BCYiMHPdddflfTbeeOM8Tdxss82WAydR/zjfCNDFPhGQWGuttdL3vve9VOxTlHXyySennXfeOc0xxxy53SNAFIGxGH0UAaFrrrkm7xrBmgjaROAp8vzWt76VR/lEG++99975uot6RxAk2qY6xaiYcNpuu+1yMPCSSy5JDz/8cLr//vvTiSeemJ588snc/vPNN1865ZRT0j//+c9c59gewaA4rkhf+MIX8nUeo3622GKLFMEuiQABAgQIECBAgACBEQr01JimT59e4xGN2b3byp06dWpj4GrMpducy6qv9q3xwqxzd+1bJ1yNh5XlXFa5Pr81XiB17q5964Sr8bCynEdT7nzzzdeTUurZcccd+9X2pptuyu/F+9/61rcq77/++us9Cy64YH5vp512qmyvfrLOOuv0HH744dWbenbYYYd8zL777ttre/GiyHPKlCk9b7zxRt4cjzNnzuxZZZVV8rH/3//3//VU1/eb3/xm3r7HHntUjinyu/fee3tmmWWWnllnnbUnnlen6rKK7VHWyy+/3LPUUkvlPI844ojirfxYXW6vN3p6embMmNGzyCKL5ONOO+20vm/3XH311T2TJk2qbH/sscd65phjjp4JEyb0qk/sEOex3nrrVepVXW6cU7THpptu2qu+cczRRx+d31tooYUq5cSTp59+umeBBRbI711xxRW93osXF1xwQc+qq65a2X7rrbfmfWebbbbKtuonSyyxRH7/kksuqd7cs88+++Ttq6++es8f/vCHfH6vvPJKz7LLLtvz6KOP5tdxncX5b7DBBj133nln3hb1W2yxxXpefPHFnr/97W89b3nLW3rGjRvX89BDD1Xyj/qdcsop+dgPfvCDvbavscYaef9q99j/tdde61l//fXzMbvsskvlmHhy+eWX52Pi+n/yySfze4VzHLv99tv3HHrooZVjfvjDH+Z84rweeOCByvbiSZhFexZ5FNtH8ljPMSPJd7h9fP8OJ9SY97VvYxyHy6Us57LK9fkd7opozPvatzGOw+VSlnNZ5fr8DndFNOZ97dsYx+FyaZSzESojDDzZjQABAgQIECBAoH0F4pf4MZVXpJj+KKbsKlJMpRRTUkWKkQnx6/3qFNNe3XjjjXmUQfX2Wp6PGzcu7x6PMaohpn2KFKM5ihTlHnfccfllTH1VHFO8H1OAxfRMMcIhRkIMl+L46nVjYoTNSNOZZ56ZR1DEqIk4l74pRknEtFVFilEMM2fOTDFt2oQJE4rN+THOI0bLRIp8q6fCqt6xur7xvMj/qaeeSrFOSpFiRM4zzzyTYkqxzTbbrNhceYypyGL6r0alZZZZJsUokTinGGUS03AtuOCCvbKP6bxWWGGFvE/UP0aShH1cTzGyKN5bfPHFK8dEXjEFWayvE+vwPP/885X3BnoS+8d1GqOhIlW3ZYxOiZFJkcI5RvlUpzh2hx12qIzKive22WabPG1bHNv3WoptZ511Vh4h1bctq/P1nAABAgQIECBAgACB/gICKv1NbCFAgAABAgQIEGhzgTvuuCNPUxVTVX3xi19M0SkendDRSR/TP80999y9avClL30pd1hH5/c555zT670IAnz0ox9NCy20UK/to3kxfvz4fHj1guGxiHsEG2LKqJgWbKAU041FivU1RpqiIz5SdVnDHRtTZ0WK9TsGShEIKNYWifevvvrqvNuKK6440O55uqp4I+p39913D7hP340RCChSdUDl0ksvzZtjGq6BUgQyYlqrZqWYBi4CK9Wp+lxjewRPwj0Who/07ne/u3r3/DzWuIngRaTqwFq/Hf+7IcoI90jVbRnXdTHF2WAmEYiL6eKKFEG9Yg2gaMe47osUeUcgKD43EgECBAgQIECAAAECtQkIqNTmZW8CBAgQIECAAIE2EIh1R2Lx+PgXa2TEGhbRuR2vi/VTqk8zRhxEp3Ok6s746PCOxbxb0blcdKovsMAC1afW63kx+uDpp5/utb3RL4r1VmLh9MFSdRChOPf/+Z//GXD3t7/97ZVgQN/F6Qc8YIiNtZ7bEFk1/a0YSRMpRjjFqJ7qf7GmzhtvvJHfrw5o1HpShUccN1R7Vecbbbf77rvnETUzZsxIP/nJTypvx5oqMTKlGCFUecMTAgQIECBAgAABAgSGFfjPT+eG3c0OBAgQIECAAAECBNpH4CMf+Uietqj6jKoDANXbi+exEHosch4Lxsei3zHNU4y8iKDKYCM1imMb8VhMNTb77LMPml2MLIg02LRZgx5Y4xvF4vFFecMdHtN9RRru3OO8R3vuL7zwQi5rpOc23Lk38/3XXnstZx8Bu4ECFMW2GPVSbyraKo6vxSTKjCDir371q3T66afnKfHiWo8RK7vttlu9p+M4AgQIECBAgAABAl0tIKDS1c2v8gQIECBAgACBsSswXAClb81iXZPoZH7sscdyB3MEVGItiRjdUkyb1feYRr5+29velrMbarRCEXSZa665Gll0v7wi/1jXI0b6jCTFFFgRVBns3KOjvgi6jPbcY6qsCMqM9NxGcv7N2qeYWi7WdDn00EObUky1Z5gMNAJroILj8xGBkwioXH/99enBBx9MYRtT4p133nkDHWIbAQIECBAgQIAAAQLDCJjyaxggbxMgQIAAAQIECHSGQHQw77nnnrkysYZELGQf0x+1YrqvKDQWgI8U00QVU0HlDVX/mTp1an5V7Fv1VkOfvutd78r5XXfddSPKtzifwYIc06ZNq9RppB3+gxVc67kNlk8rthcjT/761782rbjCIwqIwEgtabPNNksxeiYCXjFKJQKIm266aRpq2rla8rcvAQIECBAgQIAAgW4TEFDpthZXXwIECBAgQIBAFwtE8CSmTYqRIB//+MfT2muvPewv/gcLftTK+IEPfCCPEIhpou68884BD4/RA5GK9V4G3KkBG4vFzWPNmaLMobLdaKON8tt//OMfB9ytCMzEGitLL730gPuMdGNxbpdddlm66667hj2sGPkTi603qq2GLTSlvD7J+9///rxrBDqeeuqpkRxW8z6x4P173vOeHBQ58sgjBx0lNFDGsch9Mb1XTPUV/77whS8MtKttBAgQIECAAAECBAiMQEBAZQRIdiFAgAABAgQIEOgMgXnmmSd96lOfypX5wx/+MOTolIkTJ+b9brrppoZ01Md0S3vttVfO87TTTusHeumll6bbb789Rblf/vKX+73fyA3RyT7//PPnLD/5yU+m3//+90NmH+cdgaiLLrooTxVWvXMEp771rW/lTQcccEBlcfrqfWp5vu+++6a3vvWtKQIkMZriT3/605CHR8Bh/Pj/zGR83HHHDblvo9/caqutUgSRXnnllfTpT386vfjii40uIgduDj744JzvX/7yl7T55punWGh+pCmCiOETI6PiPIuA1UiPtx8BAgQIECBAgAABAm8KCKi8aeEZAQIECBAgQIBAmwrEVFjnnntu7hCOU4yF5S+88MIUHcy1jkoofrEf0x5Fh/hgqVhQ/Oabb07LL7982m+//XJAJEaY3H///enVV1/Nhz7wwAO9OrhjKrFitEJMkfX0009XivjmN7+Z1lprrRQBla9//eupGCFy1FFHpc985jM5aPGjH/2oEuyINUti9MdAZcU0TrEezD/+8Y+cf5Q12JRclRP475P55psv+0WQJ46P9WWWXXbZvHD51772tbTJJpukJZZYIj333HP5iJh2KqaMiuBJdMhffvnleWTLlVdemdZYY430yCOPZMvdd9+9UtTdd9+dHn300fw61muJfYq2inyi7YpUHTR55zvfmdt6ttlmS48//niK9UlWWGGFtMMOO6T9998/l7/MMstUTCLQUwSq4txXXHHFtN5666UYPRJrnER7RLr33nsr10+0T2H197//PUUb9l0fJo4rbGNKr4ceeqhSZnHesbbMmWeemdstRqlEcOeggw5KV1xxRTrnnHNSeOy4445596j7jTfemF544YU82iTarvraiHN64okn8r6xEH0x/Vts+OxnP1sZWRJrosQ0Xh/5yEfyFHa77rprWnPNNfNaQMV5VT/GvltssUUOzMS+ta49VJ2X5wQIECBAgAABAgS6XWBcT/yfWA0pfg01YcKEGo5ozK7dVm7MQz3a+afrke8257Lqq33ruTprP0b71m5WzxFlOZdVrs9vPVdJ7cdo39rN6jmiLOday3399dfT//t//2/QKsY6Eauuuuqg7xdvVH9+Y1qqj370o+nYY48t3h7w8ZRTTkk//OEP0y233JLe/va3pwiIrLTSSumaa67ptX90Uk+ePDlFx3sEHqpTLHgfIzciQBApgiNnnHFGLrsIOMSIjO233z4HWaJTvkgx5VWs81KdirIefvjhHHiofi8CJHvvvXcuayTOEbA44YQTclAg9l9yySXTQgstlOKcI/C0zTbbVGefp+CKaacuueSSFO0SafXVV88BjRjpEscV5UaQqFiovsgkzGP/k046KT377LPF5vwYIy9WWWWVyrYIwET7RGAiAjAR8IkgWExjFaNYIq8iRbAiAhkxJVkERsIogipf+tKX0s9+9rMceIp955133hzgiDpXp9h/4YUXroxYGqgdY5+Yemu77barPjTXN+oSLrHYe5Qf11cEOWJKua233jqPuIkAyg9+8INex0aeX/3qV7NlmFSnuF4iIFP8v1f8b9uUKVPSd77znfwY1hE0iv2iXieeeGJadNFFq7OoPP/lL3+Z4nMS7R3tO5pUtO9o8qjn2OrPbz3H13tMWfXttnK1b71XaG3HlXVdad/a2qnevbVvvXK1HVeWc1nl+vzWdn3Uu7f2rVeutuMa5SygMox7o6CHKabf2/5g9SNpygbt2xTWfpmW5VxWuT6//S6BpmzQvk1h7ZdpWc5llevz2+8SaMqGsts3RghEp3KMiogAwnCp+vdH0QFeaxqsvtX5FnnWk39xbN/Hwcrtu99A5xH7DHYuA+1fve9Iy+17HgO9Hqiswc4tPr/FIvGD7TNQGaPdVtR3oHOtdhltOcXxRTlFucX2ocr69re/nUc6/fznPy92r/uxb7l1Z1Tjgf4+1whW5+7at064Gg8ry7mscn1+a7xA6txd+9YJV+NhZTmXVa7Pb40XSJ27a9864Wo8rFHO/5lsuMbC7U6AAAECBAgQIGEZg0AAACAASURBVEBgrAqcddZZeSTESIIpUcehOqpHY9CsfGs9p1rPo9b9az2f6v1rLavW/avLGu3zVpVdlBOPxfOhzj1GEp188sl5BMtQ+3mPAAECBAgQIECAAIHhBayhMryRPQgQIECAAAECBMaoQCzyHlMtFSkWDY8pk2IqKIlAJwpceumlvaoVU9ZFiinVJAIECBAgQIAAAQIERicgoDI6P0cTIECAAAECBAi0scBtt92WDj300LwY+k033ZQ22mijNPvss+cF4Nv4tJ0agboEYjqwb3zjG+mee+5Jzz33XDr++ONTLER/yCGH5PVt6srUQQQIECBAgAABAgQIVARM+VWh8IQAAQIECBAgQKATBWKKr7PPPjtXLab5uuqqq3Qud2JDq1MWiKDK8ssvX9E48MAD0+c///nKa08IECBAgAABAgQIEKhfQEClfjtHEiBAgAABAgQItLnAxz72sXTuueemJ598Mi9Y/olPfCLNNttsbX7WTo9AfQKxpsqpp56a7r///jwqa7PNNkuLLrroiNZaqa9ERxEgQIAAAQIECBDoLgEBle5qb7UlQIAAAQIECHSVwCKLLJK23377XOdp06YJpnRV63dnZddff/0U/yQCBAgQIECAAAECBBovYA2VxpvKkQABAgQIECBAgAABAgQIECBAgAABAgQIEOgwAQGVDmtQ1SFAgAABAgQIECBAgAABAgQIECBAgAABAgQaLzBu+vTpPY3PVo6jFZg+fXqaOHHiaLNxfJsKaN82bZgGnZb2bRBkm2ajfdu0YRp0Wtq3QZBtmo32bdOGadBpad8GQbZpNtq3TRumQaelfRsE2abZaN82bZgGnZb2bRBkm2ajfdu0YRp0Wtq3PsjxEyZMqOnIGTNmpFqPqamAQXbutnLjguY8yMXQwM1lXVfat4GNOERW2ncInAa+VZZzWeX6/Dbw4hkiK+07BE4D3yrLuaxyfX4bePEMkZX2HQKngW+V5VxWuT6/Dbx4hshK+w6B08C3ynIuq1yf3wZePENkpX2HwGngW2U5l1Wuz28DL54hstK+Q+A08K1GOZvyq4GNIisCBAgQIECAAAECBAgQIECAAAECBAgQIECgMwUEVDqzXdWKAAECBAgQIECAAAECBAgQIECAAAECBAgQaKCAgEoDMWVFgAABAgQIECBAgAABAgQIECBAgAABAgQIdKaAgEpntqtaESBAgAABAgQIECBAgAABAgQIECBAgAABAg0UEFBpIKasCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgc4UEFDpzHZVKwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCBAgIqDcSUFQECBAgQIECAAAECBAgQIECAAAECBAgQINCZAgIqndmuakWAAAECBAgQIECAAAECBAgQIECAAAECBAg0UEBApYGYsiJAgAABAgQIECBAgAABAgQIECBAgAABAgQ6U0BApTPbVa0IECBAgAABAgQIECBAgAABAgQIECBAgACBBgoIqDQQU1YECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAZwoIqHRmu6oVAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0EABAZUGYsqKAAECBAgQIECAAAECBAgQIECAAAECBAgQ6EwBAZXObFe1IkCAAAECBAgQIECAAAECBAgQIECAAAECBBooIKDSQExZESBAgAABAgQIECBAgAABAgQIECBAgAABAp0pIKDSme2qVgQIECBAgAABAgQIECBAgAABAgQIECBAgEADBQRUGogpKwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKAzBQRUOrNd1YoAAQIECBAgQIAAAQIECBAgQIAAAQIECBBooICASgMxZUWAAAECBAgQIECAAAECBAgQIECAAAECBAh0poCASme2q1oRIECAAAECBAgQIECAAAECBAgQIECAAAECDRQQUGkgpqwIECBAgAABAgQIECBAgAABAgQIECBAgACBzhQQUOnMdlUrAgQIECBAgAABAgQIECBAgAABAgQIECBAoIECAioNxJQVAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0JkCAiqd2a5qRYAAAQIECBAgQIAAAQIECBAgQIAAAQIECDRQQEClgZiyIkCAAAECBAgQIECAAAECBAgQIECAAAECBDpTQEClM9tVrQgQIECAAAECBAgQIECAAAECBAgQIECAAIEGCgioNBBTVgQIECBAgAABAgQIECBAgAABAgQIECBAgEBnCgiodGa7qhUBAgQIECBAgAABAgQIECBAgAABAgQIECDQQIFxU6dO7WlgfrIiQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECHScwLienp6aAiozZsxIEyZMaDlEt5U7bdq0NGnSJM5NFijrutK+TW7Y/2avfTvbWftq32YI+PvcDNX+efr89jdpxpaynMsq1+e3GVdR/zy1b3+TZmwpy7mscn1+m3EV9c9T+/Y3acaWspzLKtfntxlXUf88tW9/k2ZsKcu5rHJ9fuu7ikz5VZ+bowgQIECAAAECBAgQIECAAAECBAgQIECAAIEuEhBQ6aLGVlUCBAgQIECAAAECBAgQIECAAAECBAgQIECgPgEBlfrcHEWAAAECBAgQIECAAAECBAgQIECAAAECBAh0kYCAShc1tqoSIECAAAECBAgQIECAAAECBAgQIECAAAEC9QkIqNTn5igCBAgQIECAAAECBAgQIECAAAECBAgQIECgiwQEVLqosVWVAAECBAgQIECAAAECBAgQIECAAAECBAgQqE9AQKU+N0cRIECAAAECBAgQIECAAAECBAgQIECAAAECXSQgoNJFja2qBAgQIECAAAECBAgQIECAAAECBAgQIECAQH0CAir1uTmKAAECBAgQIECAAAECBAgQIECAAAECBAgQ6CIBAZUuamxVJUCAAAECBAgQIECAAAECBAgQIECAAAECBOoTEFCpz81RBAgQIECAAAECBAgQIECAAAECBAgQIECAQBcJCKh0UWOrKgECBAgQIECAAAECBAgQIECAAAECBAgQIFCfgIBKfW6OIkCAAAECBAgQIECAAAECBAgQIECAAAECBLpIQEClixpbVQkQIECAAAECBAgQIECAAAECBAgQIECAAIH6BARU6nNzFAECBAgQIECAAAECBAgQIECAAAECBAgQINBFAgIqXdTYqkqAAAECBAgQIECAAAECBAgQIECAAAECBAjUJyCgUp+bowgQIECAAAECBAgQIECAAAECBAgQIECAAIEuEhBQ6aLGVlUCBAgQIECAAAECBAgQIECAAAECBAgQIECgPgEBlfrcHEWAAAECBAgQIECAAAECBAgQIECAAAECBAh0kYCAShc1tqoSIECAAAECBAgQIECAAAECBAgQIECAAAEC9QkIqNTn5igCBAgQIECAAAECBAgQIECAAAECBAgQIECgiwQEVLqosVWVAAECBAgQIECAAAECBAgQIECAAAECBAgQqE9AQKU+N0cRIECAAAECBAgQIECAAAECBAgQIECAAAECXSQgoNJFja2qBAgQIECAAAECBAgQIECAAAECBAgQIECAQH0CAir1uTmKAAECBAgQIECAAAECBAgQIECAAAECBAgQ6CIBAZUuamxVJUCAAAECBAgQIECAAAECBAgQIECAAAECBOoTEFCpz81RBAgQIECAAAECBAgQIECAAAECBAgQIECAQBcJjG/3ul577bXpuuuuSzNnzkxzzDFHy0+3rHKnT5+eJk6c2DX1Lcu5rHKjfbfYYou07rrrtryNFUhgrAuU/b3g73NrrqAy/z6X9f278cYb+15ozeWlFAIECBAg0FUC7p9b29xl3ceWVW6Z/3/k/rm117bSCBD4j8D4GTNm1GxRzzE1F/LfA6ZMmZKOOuqoeg93HIG2FYgA4corr9zy82vl57e6csqt1mje825w9r3QvOtHzuUL+F5ofht0w9/JakX1rdZo3nPOzbOtzplztUbznnNunm11zq10dv9cLe95pwm4f25+i7by71V1bZRbrdG855xrtx0/YcKEmo4K5FqPqamAPjuXMSqlzyl4SaApAnFtt/KzFJVo9ee3gOu2cuMXOq1u225qX98LxSfLY6cJ+F5ofov6+9x84yihrO997at9myFQ1vXcbeX6/Dbj6n0zT/fPb1p41lkC7p+b357+PjffOEoo63tf+9bXvm0/5Vd1tWJ6JFMkVYt4PtYEYqh1/JMIEGiMgO+FxjjKpTwB3wvl2SuZAAECBAh0o4D7525s9c6qs/vnzmpPtSEwFgXGXEBl8uTJY9HZOROoCAioVCg8ITBqgfgfQt8Lo2aUQckCvhdKbgDFEyBAgACBLhJw/9xFjd3BVXX/3MGNq2oExoDALGPgHJ0iAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBUAQGVUvkVToAAAQIECBAgQIAAAQIECBAgQIAAAQIECIwFAQGVsdBKzpEAAQIECBAgQIAAAQIECBAgQIAAAQIECBAoVUBApVR+hRMgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJjQUBAZSy0knMkQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEShUQUCmVX+EECBAgQIAAAQIECBAgQIAAAQIECBAgQIDAWBAQUBkLreQcCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgVIFBFRK5Vc4AQIECBAgQIAAAQIECBAgQIAAAQIECBAgMBYEBFTGQis5RwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBUAQGVUvkVToAAAQIECBAgQIAAAQIECBAgQIAAAQIECIwFAQGVsdBKzpEAAQIECBAgQIAAAQIECBAgQIAAAQIECBAoVUBApVR+hRMgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJjQWD8WDjJVp3jiy++mG6//fZKcRMmTEgrr7xy5fVYfXLzzTenmTNnVk5/qaWWSgsttFDldSc8ef7559Odd95ZqcoCCyyQlltuucprTwgQIFCPgO+FetTa4xjfC+3RDs6CAAECBAgQ6C4B989jt73dP4/dtnPmBAi0VsAIlSrv+OK/4IIL0u67757WW2+9tMcee1S9O3afXnPNNemUU05JW265Za7XlVdeOWxlnn766fToo48Ou1+xwxtvvJGuvfbaNGPGjGJTSx+fffbZdP7556dddtkl1/GAAw4YVfk9PT0pAlESAQLdLeB74c32973ge+HNq8EzAgQIECBAgMDAAn3vn/fcc8+BdxxjW6v7VdZff/3UDf0qBx544KhaSb/KqPgcTIBAGwsIqFQ1zsILL5xOPfXUSiBl1llnrXp37D496KCD0oUXXjiiERv/+te/0lFHHZUWX3zx9P3vf3/Elb7uuuvSRhttlGaZpZxL6j3veU8+35122mnE5zzYjrfccksembThhhsOtovtBAh0iYDvhZR8L6Tke6FLPvCqSYAAAQIECIxaoLh/jh+qRuqkfpX4Ae5IZsKovn8+44wzRmwaP1LdeOONS+9X2XHHHUd8zoPtGD9QjRlfop9IIkCAQKcJmPJriBbtlC/+oorD1efyyy9PX/3qV9O0adOKQ0b8GDcWm266aZp77rlHfEy77fjkk0+mr3/963mkS5zbXHPN1W6n6HwIEChZYLi/oyWfXs3FD1cf3wu+F2q+qBxAgAABAgQIEKgSGO5+s2rXMfF0uPpcdtllaa+99qq5XyVGc8QPYcd6v8oTTzyRvvGNb1T6VcZyH9GYuCCdJAECpQiUM5yglKr2L/TYY49Nr776av83/rtluC/KQQ9s0zcGGz0SX3jrrrtu2meffdJ2221X87oxr7/+err44ovTJz/5yV41j464v/zlL722teuLY445Jq244or5eth7773b9TSdFwECTRbwvfAfYN8LKfleaPKHTfYECBAgQIBARwi4f/5PMz7++OO5X2Xfffetu1/lkksuSdtss02v62Ks9austNJK+lV6taAXBAh0okDXBlSuvvrqtN9++w0ZUBksADFWL4TBAkSvvPJK+va3v50efvjhdMQRR6RY0L2W9Otf/zover/FFltUDnvppZdSDBO99957K9va+ckSSyyRpk6dmi666KK8Bks7n6tzI0CgOQK+F9509b2Qku+FN68HzwgQIECAAAECAwn86le/Svvvv79+lZRyn0jRr3L44Yc3pF8l1qOJac3HYr9K/GhXIkCAQKcKdO2UX4cccsiwbTpYAGLYA6t2iBEwjz32WIo1Pvqmv/71r+mhhx7K02TF3JKNThEgiV9JzDnnnGmVVVYZdO7S6DQaTYrpvj72sY+lt771rZVsjj/++NIWqK+cRA1PqoNBNRxmVwIEOkjA98Kbjel7ISXfC29eD54RIECAAAECBPoKxBRVkydP7ru53+tO6leJfpvB6jOa++diui/9Kv0uHxsIECDQlgJdN0Llt7/9bfrwhz+cYoGsSJtsskkelvmJT3yiXwPFF+V9992XvvjFL6ZJkyalcePGpXnmmSd97nOf6/ULjBiWGdH34l8EUF544YX0la98JU2cODHtsMMOlbxffvnlFFNKLbTQQumd73xnWmeddXKwY6211hrwVwcnn3xy3ifmnVxyySVTLPAWnTy/+MUvKnlWP3njjTfSmWeemVZbbbUcxFlvvfXS+9///nwesahuo9O///3v9JOf/KQy3VdME7PtttvmES9RVtxgFS6PPvpopfgjjzwyrbnmmultb3tbWnrppbNvtEEswjZQ+tnPfpbzmWOOOXI7LL744vn19ddfP9Du/bZdeeWVlfOI84m1YiQCBAiEgO+Fxl4Hvhca6yk3AgQIECBAgEC7CcT984Ybbpj7VSIYUPSr9J2uKs57sH6VnXfeedB+lejHiH6VGTNmVPpVqhdK/+c//zlgv8raa6/d1H6VeeedNzWrX+WnP/1pZbqv+GFs9KscffTRqQhcRT9GuDS6XyXyrLdfJdaKkQgQINCNAl0XUHnHO96RvvCFL1Ta+sADD0yHHnpoinku+6Y77rgjLyb29re/PQdRIrAyc+bMdPbZZ+ftxf4RCDjppJPS3Xffna677rr8fPnll09/+MMf0myzzVbslh8//vGPpxNOOCF/UT7zzDPptddeywGbG2+8MQdO/vGPf/TaP4I1iyyySIqFzR544IH85R3lxEJlsa1vipuSqN9b3vKWdNVVV6WYtiW+gCMwFPk0Ov3yl7/MdYjziTR+/Pi0yy675ABOvI51VcI3/oV9kc4///y07LLLppguLNZZueaaa9Lvfve7tNFGG/ULqsQQ4i233DKbxU1VLB4fU5NF+/T1KvLv+7jZZpvl+t91113pqKOOSt/5znf67uI1AQJdKuB7obEN73uhsZ5yI0CAAAECBAi0m0DcP3/+85/PpxU/PC36VWJd1r7pT3/604D9KmeddVYOihT7R7/KiSeemPtV4oeW0ceywgor9OtXif6NrbfeOverRH9D9KvED3qiv+aGG27IP6Ss7ieI/fv2q8QPbKNfJfoJ+varxP5Fv0r8oLO6XyX6LlrRrxL9SFGf+IFu+Bb9KvGD1aJfJc6zb79K9K9Ev8rGG2/cq18l9o1+la222qpXv0pMTVZLv0r0+0T9wy76VaJvSyJAgEA3CnTdlF/RiR9TYBUpRobMNddcxctej4suumj+8qzeGL/CiC+zH/zgB+l73/te5a0IoMw+++z5dSzSfuutt+Yvungsovbxi4MpU6akd7/73flGoTj49NNPz4GB+CL/7ne/m4MPxXsRoIiFcWNES6Q4pxjhsueee+ZfK0SgoUhxk3DOOeek+eefP0WHVoxqKVJ86VW/LraP9vHCCy9Mm2++eWW6rwUXXDDFv2L6r/COX1L0TWEei9cV5xRTou26667psMMOS8cdd1zlmH/96185+BGjc2LET5E+/elPZ7PwGUk65ZRT8qieuMGKc5IIECBQCPheKCQa8+h7oTGOciFAgAABAgQItKtA3D8X/88f5zhUv8piiy3Wr18lZg351Kc+lftVog+kSNX9KjH7RtGvEj9WLYI1Rb9KzFpR/UPJ0047rdKvEn011dORRYCiul8lzin6aWLmitg+UL9KrC0bM4MUfRZxjs3oV4lgR6zl2rdf5X/+538qxoP1q8S5VferxLRjRb9KTMNe9MUM1q/ymc98JgekaulXib6mGNGiX6W4aj0SINCNAl03QmW0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ueeem9cZ6ft+o17HYu/xC5cYYjpYKoz7+s4///z5kNdff73fDVAMH+2b4iYj3F566aVeb8Ww1DvuuCOPkFliiSV6vTfQi7POOiuvvxIBmnCSCBAgUC1Q/M2KbX3/blXv1+jnvhdS8r3Q6KtKfgQIECBAgACB5guUcf8cI0322muv3K8Sa4h87WtfG7KitfarRP4HH3xwW/WrRADjd7/7Xa961nr//MILL+Qp0EfTrxI2MTol1rV99NFH8xrAvU7KCwIECHSRQFcGVOadd94893q081ZbbZV/ERCdWtddd12eg3LatGn5EojO/FgYwUlA+QAAIABJREFUPjr/I8XaJXfddVd+Hv+588478/NYF+T++++v/OIhFj2Laaj6/opghRVWqHzpHHPMMXmExbHHHptiEbIYPhlDLk899dSc58ILL5xvFOJFnNtSSy2VF7CPPK6//vq8T/zCIhYVK9Iaa6yR5wWN+TRjYbF4vd9+++W5RWMYZwyLjRTnV/1FGl/QMafotddem+fCjOGekW666aYUwZl4/Pvf/563xX9iWGqcawwvHSyts846+a2oVzyP84jnsXBcjBKJtN1226UVV1wx1+u9731vXhMltv/zn/+snGu8jnVnYsG4U045JZ/jeeedl4M50S4HHXRQnu4l9otzDPdIMa1Y9Zosc889dz7neO/4449PF198cQqnIsUNRix2H9tjfZhI4Rvr18RonLgOop0lAgQ6U8D3gu8F3wud+dlWKwIECBAgQKA5AsX9c/QnDNSvEuvBRmp0v0r0IUyePDnnffTRR4+oXyXOsW+/yg033JDz6Nuv8oEPfCD3XcT2vv0qyy+/fO6riPyij2CwfpVYu7XoV/n973/fr18ljr/oootG3K/yne98Z8B+lcinb7/Kvffem+vVt18lXlf3q0RfT8xyEv1WBx54YK9+lWKa+tH0q1x22WUVX/0qmcJ/CBDoIIFZDz300ENrqU8EFVo5/2YEOaKjP9K6666b/9VyvoPtu8UWW6QY6RGR9QiMzDPPPCmmhjrjjDPyrxGirGWWWSYHLGadddb0rne9K3/h3XrrrZXziHVOYi2QCEZcccUVKaZuieMiABCjUMJp0UUX7XUK8X58QcdojFtuuSXXLQIccTMSc1/GwmpFihEgEUiJL+m55porRTAlRlfsuuuuKc5ptdVWy2uyRDnFGiKx7X3ve1/+xUYEFMIughgnnHBCPrfIb/bZZ8/n96EPfSgXFeuaRJAiRm9EYCHKifOMOsfi7rHoe9Q71i2JYZ277bZbOuKII9JQI0Pi+Phyj8XgwyJMtt1227xAfMwRuthii+W83va2t+WblKOOOioPG41ROXGDFCNQwiSm9grjCGSdc845KUaaxLnEGjERpNlnn31yHeJm57jjjkuRX5QdC9FHAOmDH/xgtogF7KO9472Y6zOexzFFHeILPsqI7fErlthvrbXWyucdQZoIXEVAJfIdTWrW9TzSc2r157c4r24rN4ZgV/9iq3Bo9mO3ODfrc+R74Y/J94LvhWb/nSryL+vvlb/PRQs091H7Nte3yL0s57LK9fktWr65j9q3ub5F7q12bsb9c4xYiA76Z555ptKvEv8vvf322/fqV4n+iPj/6YH6VeLHl9X9KldeeWXuV4ntjehXiXMcrl8l+k+iT6S6X2X11Vfv168S/UPx48zoK6i3X+W2226r9Kt8+ctfTocffnilT6K4NorHOPcoq7pfJfpj6ulXiX6MRvSrRLCm1n6V+P+LaEv9KkXL1v/Y6r8bxZn6/i0kmvuofZvrW+TeKOdxPfHXuYYUH6T4kmxVOuyww1IR84nH4pcIrSpfOQQaKVD29dzqz29h123lxii3SZMmFdVv2WO3OJf9OWpZgyqoKwTKvp675e9GcTH5+1xINPexrOtK+za3XYvctW8h0dzHspzLKtfnt7nXU9n3G82tndy7TaDs67msv5Nllevvc2s+Ydp3bDl35ZRfrWkipRAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQKdIiCg0iktqR4ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBA0wQEVJpGK2MCBAgQIECAAAECBAgQIECAAAECBAgQIECgUwQEVDqlJdWDAAECBAgQIECAAAECBAgQIECAAAECBAgQaJqAgErTaGVMgAABAgQIECBAgAABAgQIECBAgAABAgQIdIqAgEqntKR6ECBAgAABAgQIECBAgAABAgQIECBAgAABAk0TEFBpGq2MCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgU4REFDplJZUDwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBpAgIqTaOVMQECBAgQIECAAAECBAgQIECAAAECBAgQINApAgIqndKS6kGAAAECBAgQIECAAAECBAgQIECAAAECBAg0TUBApWm0MiZAgAABAgQIECBAgAABAgQIECBAgAABAgQ6RUBApVNaUj0IECBAgAABAgQIECBAgAABAgQIECBAgACBpgkIqDSNVsYECBAgQIAAAQIECBAgQIAAAQIECBAgQIBApwgIqHRKS6oHAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0DQBAZWm0cqYAAECBAgQIECAAAECBAgQIECAAAECBAgQ6BQBAZVOaUn1IECAAAECBAgQIECAAAECBAgQIECAAAECBJomIKDSNFoZEyBAgAABAgQIECBAgAABAgQIECBAgAABAp0iIKDSKS2pHgQIECBAgAABAgQIECBAgAABAgQIECBAgEDTBARUmkYrYwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBTBARUOqUl1YMAAQIECBAgQIAAAQIECBAgQIAAAQIECBBomoCAStNoZUyAAAECBAgQIECAAAECBAgQIECAAAECBAh0ioCASqe0pHoQIECAAAECBAgQIECAAAECBAgQIECAAAECTRMY37Scm5Dxtdde24RcZUmgdQKu4dZZK6k7BHymuqOdO7mWruFObl11I0CAAAEC7Sfg3qP92sQZ1SbgGq7Ny94ECDReYPyMGTNqzrWeY2ou5L8HzJw5s3Jo/NH0h7PC4ckYF4hru5WfpYKrjDKjbOUWLdDcx25w9r3Q3GtI7uUJ+F5ojX03/J2sllTfao3mPefcPNvqnDlXazTvOefm2Vbn3Epn98/V8p53koD759a0Ziv/XlXXSLnVGs17zrl22/ETJkyo6ahArvWYmgros/Mcc8zRZ4uXBDpDIK7tVn6WQq3Vn9+ipbqt3OnTp7e8bbupfX0vFJ8sj50m4Huh+S3q73PzjaOEsr73ta/2bYZAWddzt5Xr89uMq/fNPN0/v2nhWWcJuH9ufnv6+9x84yihrO997Vtf+7b9lF/rrLNOOvTQQ1NEncu4CSir3LigJ06cWF+rjuKosurbbeVG+8a1LREgULtA2d8L/j7X3mb1HFHW90KZ7et7oZ4rxTEECBAgQIDAcALun4cTauz7Zd3HllWu++fGXj9yI0Cg/QXaPqCy7rrrpvhXVqSurHKnTZuWJk2a1PIrqKz6dlu5ZbVvyy8oBRJogkDZ3wtlfX677e9kWfXttvZtwkdUlgQIECBAgECbCbh/bm2DlHUfW1a57p9be30pjQCB8gVmKf8UnAEBAgQIECBAgAABAgQIECBAgAABAgQIECBAoL0FBFTau32cHQECBAgQIECAAAECBAgQIECAAAECBAgQINAGAgIqbdAIToEAAQIECBAgQIAAAQIECBAgQIAAAQIECBBobwEBlfZuH2dHgAABAgQIECBAgAABAgQIECBAgAABAgQItIGAgEobNIJTIECAAAECBAgQIECAAAECBAgQIECAAAECBNpbQEClvdvH2REgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJtICCg0gaN4BQIECBAgAABAgQIECBAgAABAgQIECBAgACB9hYQUGnv9nF2BAgQIECAAAECBAgQIECAAAECBAgQIECAQBsICKi0QSM4BQIECBAgQIAAAQIECBAgQIAAAQIECBAgQKC9BQRU2rt9nB0BAgQIECBAgAABAgQIECBAgAABAgQIECDQBgICKm3QCE6BAAECBAgQIECAAAECBAgQIECAAAECBAgQaG8BAZX2bh9nR4AAAQIECBAgQIAAAQIECBAgQIAAAQIECLSBgIBKGzSCUyBAgAABAgQIECBAgAABAgQIECBAgAABAgTaW0BApb3bx9kRIECAAAECBAgQIECAAAECBAgQIECAAAECbSAgoNIGjeAUCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgfYWEFBp7/ZxdgQIECBAgAABAgQIECBAgAABAgQIECBAgEAbCAiotEEjOAUCBAgQIECAAAECBAgQIECAAAECBAgQIECgvQUEVNq7fZwdAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0AYCAipt0AhOgQABAgQIECBAgAABAgQIECBAgAABAgQIEGhvAQGV9m4fZ0eAAAECBAgQIECAAAECBAgQIECAAAECBAi0gYCAShs0glMgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIE2ltAQKW928fZESBAgAABAgQIECBAgAABAgQIECBAgAABAm0gIKDSBo3gFAgQIECAAAECBAgQIECAAAECBAgQIECAAIH2FhBQae/2cXYECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAGwgIqLRBIzgFAgQIECBAgAABAgQIECBAgAABAgQIECBAoL0Fxrf36Tk7Ap0lcO2116brrrsuTZ8+PU2cOLHllZs5c2aaY445lNtkgW5s34033jitu+66TZaVPQECBAi0s0Bxn1PW/UY3fv92031dme3rPqed//I4NwIECBAgQIBAawXGTZ06tae1RSqNQPcKnHDCCSn+SQQ6TWCvvfZK8U8iQIAAge4VcJ/TvW3f6TV3n9PpLax+BAgQIECAAIGRC4yfNGnSyPdOKc2YMSNNmDChpmMasXO3lTtt2rRUa9twrl2g1ddVGaNSaldxBIHaBeLabvXfrFZ/fgsVf58LieY+at/m+ha5l+VcVrk+v0XLN+fRfU5zXOVavkA33ef4+9ya660s57LK9f3b2deV9tW+zRAo6+9Vt5Xr81vf1WvKr/rcHEVg1AIxPZIpkkbNKIMSBWJql/gnESBAgACBvgLuc/qKeD3WBNznjLUWc74ECBAgQIAAgdYICKi0xlkpBPoJREfD5MmT+223gcBYEhBQGUut5VwJECDQOgH3Oa2zVlLzBNznNM9WzgQIECBAgACBsSowy1g9cedNgAABAgQIECBAgAABAgQIECBAgAABAgQIEGiVgIBKq6SVQ4AAAQIECBAgQIAAAQIECBAgQIAAAQIECIxZAQGVMdt0TpwAAQIECBAgQIAAAQIECBAgQIAAAQIECBBolYCASquklUOAAAECBAgQIECAAAECBAgQIECAAAECBAiMWQEBlTHbdE6cAAECBAgQIECAAAECBAgQIECAAAECBAgQaJWAgEqrpJVDgAABAgQIECBAgAABAgQIECBAgAABAgQIjFkBAZUx23ROnAABAgQIECBAgAABAgQIECBAgAABAgQIEGiVgIBKq6SVQ4AAAQIECBAgQIAAAQIECBAgQIAAAQIECIxZAQGVMdt0TpwAAQIECBAgQIAAAQIECBAgQIAAAQIECBBolYCASquklUOAAAECBAgQIECAAAECBAgQIECAAAECBAiMWQEBlTHbdE6cAAECBAgQIECAAAECBAgQIECAAAECBAgQaJWAgEqrpJVDgAABAgQIECBAgAABAgQIECBAgAABAgQIjFmB8WP2zJ04AQJDCrz44ovp9ttvr+wzYcKEtPLKK1dej9UnN998c5o5c2bl9Jdaaqm00EILVV53wpPnn38+3XnnnZWqLLDAAmm55ZarvPaEAAECBAh0u4D7nLF7BbjPGbtt58wJECBAgAABAgRSElBxFRDoUIHoaLjgggvSjTfemO6555605ppr5udjvbrXXHNNuuuuu9KUKVPSjBkz0mmnnZZ22WWXXtV67LHH0iOPPJLGjRuX5ptvvrT44ounOeecs9c+Q71444030vXXX58DUBGIanV69tln0/nnn5+uu+669OCDD6ZNN900XXnllSM+jVdeeSX96U9/Sq+++mp6y1vekiZNmpSDTuEhESBAgACBThBwn+M+x31OJ3yS1YEAAQIECBAgMPYETPk19trMGRMYkcDCCy+cTj311LTHHnvk/WedddYRHdfuOx100EHpwgsvHHTExvve974cQNhss83SN7/5zbTzzjuneeaZJ6266qrpmGOOSa+//vqwVYxAxkYbbZRmmaWcP5Hvec970ve///200047DXuufXeIANPEiRPThz70ofTVr341HXDAAdkqRrl87nOfS1OnTu17iNcECBAgQGDMCbjPcZ/jPmfMfWydMAECBAgQIECgIwTK6S3sCDqVIDC2BDoloFKoD1afRx99NO2///4pRnnccMMN6dZbb00PP/xwmnfeefP2DTbYoNeUYUV+1Y8xsidGhcw999zVm8fE86eeeiq9613vSg888ECeNuzaa69N//jHP9KBBx6YR70sv/zyKUb5SAQIECBAoJMEBrsvGKt1HKw+7nPc54zVa9p5EyBAgAABAgQ6RUBApVNaUj26XuDYY4/NUzwNBjHY/5gPtn+7bx9q9MgXv/jFNPvss1eqEFNe/fznP8/Tf8Xokxi1MViKESwXX3xx+uQnP9lrl8svvzz95S9/6bWtXV9svPHGKUa5FCnaft9990377bdfeumll9JnPvOZFPOXSwQIECBAYKwIuM95s6Xc57jPefNq8IwAAQIECBAgQKDVAgIqrRZXHoEmCFx99dW5szzmkh4sDRWAGOyYdt4+WIBovfXWS0sssUS/U4+1RGJ0SqQf//jH/d4vNvz617/OI1i22GKLYlMOQuy4447p3nvvrWxr1ycxOiWmKxsobbLJJnlzjFgxSmUgIdsIECBAoB0F3Oe82Sruc9znvHk1eEaAAAECBAgQIFCGgEXpy1BXJoEGCxxyyCHD5jhYAGLYA6t2iIBNLPhePfqhePuvf/1reuihh/I0WSuvvHKxuWGPMW3X448/nheXX2WVVdJg9bnkkksGLbNYYD4CCq+99loaP77/n8CY7utjH/tYeutb31rJ5/jjj08zZsyovG7nJ0Otu1LUP84/pgaTCBAgQIDAWBBwn/NmK7nPGXx9Ofc5b14nnhEgQIAAAQIECDRPwAiV5tnKmUDTBX7729+mD3/4w+nmm2/OZcUIhHXXXTd94hOf6Fd2BCDuu+++FNNExBRY48aNy4u1x0Ll1SNb4n/UI4/iXwRQXnjhhfSVr3wlL3a+ww47VPJ++eWX0957750WWmih9M53vjOts846KYIda6211oCjOU4++eS8T6xNsuSSS6ZYUDZGgvziF7+o5Fn95I033khnnnlmWm211XIQJ36V+f73vz+fxy233FK964ieP/nkk3m/FVZYYcBgyr///e/0k5/8pDLd1xNPPJG23Xbb9O1vfzsfN3ny5IpLzGFepCOPPDKtueaa6W1ve1taeumls2+0QaxfMlD62c9+lvOZY445cjssvvji+fX1118/0O79tl155ZWV84h2ikVZR5KK+se+zQh6jeQc7EOAAAECBEYq4D5npFL/2a/4nnef4z6ntivH3gQIECBAgAABArUICKjUomVfAm0m8I53vCN94QtfqJxVLDx+6KGH5vUyKhv/++SOO+5Ie+21V3r729+eIogSgZWZM2ems88+O28v9o9AwEknnZTuvvvuFOuNxPNYyPwPf/hDmm222Yrd8uPHP/7xdMIJJ6RtttkmPfPMM3nUR+R744035sBJjASpThGsWWSRRdJll12WF02PoEiUEwvAx7a+aeedd871i+m6rrrqqvTKK6+knp6eHBiKfGpNMcIlUjH1V9/jf/nLX+Y6xPlEihEsu+yySw7gxOtYVyV841/YF+n8889Pyy67bIrpwmKdlZhO63e/+12eeqtvUGX//fdPW265ZTaLYFV0fhxxxBEp2qevV5F/38fNNtssO951113pqKOOSt/5znf67jLg66L+EdBaddVVB9zHRgIECBAg0C4C7nNqa4nie959jvuc2q4cexMgQIAAAQIECNQi0H++m1qOti8BAqUKRCf+nHPOWTmHGBky11xzVV5XP1l00UVzUKJ624YbbpiDBD/4wQ/S9773vcpbEUApFnWPRdpvvfXWHECIxwjKRPrpT3+apkyZkt797nenE088sXLs6aefngMDESD57ne/m4MPxZsRoDjmmGPyiJbYFucUI1z23HPPdPTRR+dAQ7FvBF/OOeecNP/886cIdEQQoEgRTKl+XWwf6jECHX/+859zUGifffYZcNcLL7wwbb755pXpvhZccMEU/4rpv8I7RoT0TWEei+UW5xRTou26667psMMOS8cdd1zlmH/96185+BGjc2LET5E+/elPZ7OBpiAr9ql+POWUU/KonhtuuCEHcqrfG+r5j370o/z2HnvsUanTUPt7jwABAgQIlCngPmfk+u5zUnKfM/LrxZ4ECBAgQIAAAQL1CxihUr+dIwmMeYGYLixSdPTHGigDpY985COV0Rgx9VaMaIl0xhln5McYpdI3xciSSDG1VXWKERwxPVh1WnHFFfPLadOmVW+uBGliNE0RqOi1Q40vDj/88HzEt771rTzVWN/DY/TLpZdeWpnuq+/7Q72OKdf6nuNA9YrRKDGt2P3335+mTp3aK8sIcsT0Z8OlCH4ddNBBqdZgSowwihFHEQA7+OCDhyvG+wQIECBAYMwLuM95swnd57xp4RkBAgQIECBAgACB0QgIqIxGz7EExrhA9YiI6OgfSVpiiSXybrfddlt+jA76vinWEonUN2jQd794XZxDrJdSpJiK7KabbsovY82U0abLL788/2px4403Tl/72tcGzO7nP/953h7TaTUiDVSvWGcmAi9R1/XXXz+P8KmlrJhabLfddqs5mPLiiy+mT33qU3lUSqy/Emu3SAQIECBAoNMFiu/iqKf7HPc5nX69qx8BAgQIECBAgEBrBEz51RpnpRDoOIFivY9YvyOmyqpOzz33XH4ZgZG+KUZnxNRhDz/8cF7DJUZa9E0RiHnttdfy5kmTJvV9u6bXMTIjptSKaUMuvvjiNMssA8eRL7jggrTVVlv1WydmpIXde++9KdaEiXVR/vnPf6bf/OY3/Q6NtWBierQYdROL2sfon1gcPhaV33bbbYcsO6ZA++xnP5vXkIlpPaI+I0nhGGu2xLzqV1xxRVpmmWVGcph9CBAgQIBAVwu4z+nd/O5zent4RYAAAQIECBAg0L0CA/csdq+HmhMgUKPA0ksvndcIibVFin8xDdjkyZPz1FRFdg8++GBac801cyDgj3/8Y4pASYwYGWiaq+eff744rN9UWpU3RvAkFm2PMmIUTQQ4+k7LVWQR02D84he/qGu6r6jLSiutlAMjEeiI9VM++tGPpk022aTIvtfjTjvtlO6+++4c5Im1Wf70pz+l2BaBlcFG9Nx+++1p++23rywkv/vuu6cZM2b0ynegFxFM+cxnPpOn+jrrrLPyeQ20n20ECBAgQIDAwALuc9znDHxl2EqAAAECBAgQINCtAuNH0inXF6eeY/rmUc9r5dajVvsxnGs3G+kRA43YGOmx7bbfnHPOmV5++eU8lVSMABkq9fT0pJjHPEZvnHzyyb0WZI/1W/qmBRZYoLIpgh31pAhCRJkf+MAH0kUXXZRi4fjBUqydEtOCRCCklhQBi4022ig9++yzeZTOJz/5ycrhg61JEzsst9xy6cc//nFeuyamGov1U+655560wQYb5JE7lUz++yQCTLEeTQRdFl988fT000+nffbZJ5155pl9d628jqlNIlgVU6f96le/ylOMVd5swpO4tsv421FGmcGn3CZcRANkyXkAlCZs4twE1AGy7AZn9znuc+LSd58zwB+AOjd1w9+Nahr1rdZo3nPOzbOtzplztUbznnNunm11zpyrNZr3nHPzbKtzboTz+AkTJlTnOezzKLTWY4bNdAQ7dFu506dP5zyC62K0u7T6uuqktStihEmMyIiF1odLTz31VA6mxH4x3dVwKdYaGTduXJ7eKkZtRCChlhSLxG+44YZ5vZH/+7//y3kNdXxM9xXTYs0222xD7dbvvah/BFMiGFMdTOm34yAbYgqwGM0TI1xiCq9HHnkkPfHEE2mRRRbpdUQEhoqFdU866aS0ww47pFicfscdd0xrr712r33jRQShYi2YcL/jjjvyaKB+OzV4Q1zbrf5uaPXntyDz97mQaO6j9m2ub5F7Wc5llevzW7R8cx7d57jPqb6y3OdUa9T+vKy/k2WV6+9z7ddIPUdo33rUaj+mLOeyyvX5rf0aqecI7VuPWu3HlOVcVrk+v7VfI3GEKb/qc3MUgbYUqF7YvdknWCwW/6Mf/WjYouKLoUivvvpq8XTQxxj9EuuLRIqRGbWka665Jk/zdeqpp6Zvf/vbwwZTYsH2q666akQBkb6+Rb1iBE78Gy5FcOj000/vt1tMSVasiRJfZkOlWEclgkWRIqDSdwRPrN8SC95HkCfWdBntGjRDnYv3CBAgQIBAKwX6fg83s2z3OW+OxnSf08wrTd4ECBAgQIAAAQJjTcCi9GOtxZwvgT4CEydOrGy58cYba562qnJwjU/23nvvdM4556RYQ2T//fdPRx999KA5xMiFWAw+OkLOPvvstNdee1X2LRZ9rWz475NDDjkkTZkyJZ177rkp1gwZySiVCKbE2iVrrbVWijVbDj300L7ZVl5HYCKmz4rF3uMXtbHWymCpMA7fbbbZprLb/PPPn5+//vrreQqvWFi+SH/729+Kp5XHCN6EW+xXPQXZn//85zySJEbILLHEEpX9B3sS66HEfhGgCafCPqZPW2edddJDDz2UpxE75phjBssiLbXUUnl9lUF38AYBAgQIEGgDgeI7OE7FfY77HPc5bfChdAoECBAgQIAAgS4XEFDp8gtA9ce+wLzzzpvnqo5O+a222iptvvnmecqomMJq+eWXT9OmTcuVjM78CDLEaIhZZ501r98Ri7YX6c4778yjGWJdkIcffjgVI0keeOCBtMwyy6SFF144B0WK/VdYYYW88HwELaLjPhZ133nnnfO+Uc51112XR1J86UtfysdGEOW4447LAYVTTjklLbTQQunMRfcfAAAgAElEQVS5555La6yxRs4yyovF2uOcI8X2mN7qK1/5SlpllVVS/FL0Qx/6UHr88cfzeiPFVGNxfi+99FIOUPz6179OsXZILEAf/4ZKH/zgB3NA5cILL0xbb731kNN9xf+833rrrenEE0/MgY/VVlstLbbYYmnPPffMo0QisLTddtulmF4s2iOCKWuuuWYuPkaM3Hfffem9731vfh3rzkQbRWAmFrqNKb6+/vWvpwjKHHzwwSmmx4j097//Pb8Xz2NasViTJdog0txzz53P+bzzzkvHH398Wn311fOUZbFfrB0T6fDDD8+Pg/1n0003FVAZDMd2AgQIEGgbAfc57nPc57TNx9GJECBAgAABAgQIpJQEVFwGBDpAIKasOuCAA9KVV16ZYoH1WG8jAhjf/e530+yzz54DH1HN888/P6233np5FMNPfvKTFMGIyZMnZ4EYaTLffPPlqatipEcslB7pmWeeSWeccUYewRELvFenODYCHxFQiWDGgQcemIMfMUJk1113zQu2F/sfe+yx6X3ve18e1RJBj1iwNEaJxLZFF100BxTinCIAUQRZvvzlL+fARSzgHgGjWIQ9AgGx5kmsNxLnHCkWuv/GN76R610EJIpyB3uM0Smx2Hucd7gNlY444ogc6Lj44ovT9ddfnxckL0aFxIibWMckzimmxFhxxRVzYGnJJZfM9Yp8470IdkWZETSJacwiGBPBq1gvJQJGEZj64he/mE8jgkvf+9730jve8Y5K+0Tb7bfffnkKsxiBEnkVbRcL2seIlwg4FduGqk+8FyNUJAIECBAgMBYE3Oe4z3GfMxY+qc6RAAECBAgQINAdAuN6RjLxf5VFWYvkdFu5MaqgjLUPus251fU97LDDKtNQRQf6SDu/qz6CnhJoG4Gyr+dWf34LeH+fC4nmPmrf5voWuZflXFa5Pr9FyzfnsezvhebUSq7dKlD29VzW38myyvX3uTWfNO3b2c7aV/s2Q8Df52ao9s/T57e/STO2NMrZovTNaB15EiBAgAABAgQIECBAgAABAgQIECBAgAABAh0lIKDSUc2pMgQIECBAgAABAgQIECBAgAABAgQIECBAgEAzBARUmqEqTwIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCjBARUOqo5VYYAAQIECBAgQIAAAQIECBAgQIAAAQIECBBohoCASjNU5UmAAAECBAgQIECAAAECBAgQIECAAAECBAh0lICASkc1p8oQIECAAAECBAgQIECAAAECBAgQIECAAAECzRAQUGmGqjwJECBAgAABAgQIECBAgAABAgQIECBAgACBjhIQUOmo5lQZAgQIECBAgAABAgQIECBAgAABAgQIECBAoBkCAirNUJUnAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0FECAiod1ZwqQ4AAAQIECBAgQIAAAQIECBAgQIAAAQIECDRDQEClGaryJECAAAECBAgQIECAAAECBAgQIECAAAECBDpKQEClo5pTZQgQIECAAAECBAgQIECAAAECBAgQIECAAIFmCAioNENVngQIECBAgAABAgQIECBAgAABAgQIECBAgEBHCQiodFRzqgwBAgQIECBAgAABAgQIECBAgAABAgQIECDQDAEBlWaoypMAAQIECBAgQIAAAQIECBAgQIAAAQIECBDoKAEBlY5qTpUhQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEmiEgoNIMVXkSIECAAAECBAgQIECAAAECBAgQIECAAAECHSUgoNJRzakyBAgQIECAAAECBAgQIECAAAECBAgQIECAQDMEBFSaoSpPAgQIECBAgAABAgQIECBAgAABAgQIECBAoKMEBFQ6qjlVhgABAgQIECBAgAABAgQIECBAgAABAgQIEGiGgIBKM1TlSeD/b+9uwOyoygMAn4SIQcCNhYqlaAAVRBRIEFBBs8EfCqhYRNoGgVC1tvZHAgIqPE2oIgqoIBWsjZBWsYqtpQIiVCEBW6EURSAqipAg+AMiu/wZQUifb+wsN/tzd2d35s7due88z3LvnTlzzpz3m5ks99szhwABAgQIECBAgAABAgQIECBAgAABAgQINEpAQqVR4dQZAgQIECBAgAABAgQIECBAgAABAgQIECBAoAqBWVVUqk4CBMYXWLly5fiFlCDQxQLO4S4OjkMjQIBAzQL+jag5AJqfsoBzeMqEKiBAgAABAgQINFJg1uDgYOGOTWafwo2MsoN2R0GpYBXnClD/v8p169YNVR7/k+Z/1IY4vJnmAnFu13HvqKPNCJV2O3PCcuZchYDzqgrV39bp95zqbNVcr4Dfczrj7/7MuQoB51UVqiPr5DzSpIo1nKtQHVkn55EmVayZzs6z+vr6CplEZ4vuU6iBMQr3WrsDAwOcxzgXylzd6fNq9uzZZR6+ugh0jUCc253+t6HT12+O7f6cS1T7Kr7V+ua11+VcV7uu3zzy1bz6PacaV7XWL9BLv+e4P3fmfKvLua52/fvb7PNKfMW3CoG67le91q7rd3Jnr0d+Tc7NXgQmJbBgwYK0bNmyFDesOXPmTKqOqewUf11Xx5cdvdZuL8Y3zm0LAQIECPS2QP57Tl3/7vfiv7+99HtdnfH1e05v39v0ngABAgQIECDQKiCh0qrhPYGKBfr7+1P8rF27Ns2dO7fi1kZW32uZ9rr6K74jzz1rCBAgQKD5AvnvOf797Uys63Kuq91e+/2qM2eRVggQIECAAAECBIoKzCy6g/IECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TkFDptYjrLwECBAgQIECAAAECBAgQIECAAAECBAgQIFBYQEKlMJkdCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgV4TmNVrHdZfAgQIECBAgEC3CKxcuTKtWrUqrVu3Ls2ePbvjh9Vr7Q4MDKQ5c+Zwrlggzqv99tsv9ff3V9yS6glUJ+D+XJ3taDW7P4+mUv469+fyTdVIgAABAr0nMGtwcLBwryezT+FGRtlBu6OgVLCKcwWoo1TJeRSUClZxrgB1lCo5j4JSwSrOFaCOUmUnnS+//PL0oQ99aJSjsIrA9BeYN29exzvRyeu3tXPabdWo7n0nnd2fq4ujmusXcH+uPgadvF+19ka7rRrVvedcnW1rzZxbNap7z7m47ay+vr5CewVy0X0KNTBG4V5rN/5Ch/MYJ0OJq+s6r8S3xCC2qUp82+CUuKku57radf2WePK0qapX4lvHqJQ27DYRKE0gzu1O/y7r/lxa+NpW5P7clsdGAl0v4P5cfYjquk/W1a5/f6s/p6IF8W22s/hOr/h65Fdn4qUVAgQIECBAgEBbgXg8kkcktSWyscsF4hFJ8WMh0DQB9+emRbT3+uP+3Hsx12MCBAgQqE5AQqU6WzUTIECAAAECBCYsEF/YLV26dMLlFSTQjQISKt0YFcc0VQH356kK2r8bBNyfuyEKjoEAAQIEmiAwswmd0AcCBAgQIECAAAECBAgQIECAAAECBAgQIECAQJUCEipV6qqbAAECBAgQIECAAAECBAgQIECAAAECBAgQaISAhEojwqgTBAgQIECAAAECBAgQIECAAAECBAgQIECAQJUCEipV6qqbAAECBAgQIECAAAECBAgQIECAAAECBAgQaISAhEojwqgTBAgQIECAAAECBAgQIECAAAECBAgQIECAQJUCEipV6qqbAAECBAgQIECAAAECBAgQIECAAAECBAgQaISAhEojwqgTBAgQIECAAAECBAgQIECAAAECBAgQIECAQJUCEipV6qqbAAECBAgQIECAAAECBAgQIECAAAECBAgQaISAhEojwqgTBAgQIECAAAECBAgQIECAAAECBAgQIECAQJUCEipV6qqbAAECBAgQIECAAAECBAgQIECAAAECBAgQaISAhEojwqgTBAgQIECAAAECBAgQIECAAAECBAgQIECAQJUCEipV6qqbAAECBAgQIECAAAECBAgQIECAAAECBAgQaITArEb0QicIECBAgAABAgTaCjz44IPphhtuGCrT19eX5s2bN/R5ur659tpr07p164YOf8cdd0y/93u/N/S5CW/uv//+9J3vfGeoK1tuuWV60YteNPTZGwIEpreA+/P0jZ/78/SNnSMnQIAAAQKTFZBQmayc/QgQIECAAAEC00ggvrD7/Oc/n/7rv/4rrV69Ou29997pmmuumUY9GP1Qv/71r6ebbropXXHFFWlwcDB98pOfTH/2Z3+2QeEnnngirVmzJv34xz/O1j/zmc9Mz3ve89JTnvKUDcqN9SH2v/rqq7MEVCSiOr3cd9996YILLsiO4Yc//GF63etel7785S8XOowHHnggffe7382ST7Nnz06ReHrGM55RqA6FCRCoRsD92f3Z/bmaa0utBAgQIECgCgGP/KpCVZ0ECBAgQIAAgS4T2HrrrdO5556b/uqv/iqtX78+zZzZjF8DTzzxxCxRtPPOO2f9Gs6+YMGCtOmmm6YXv/jFKcqecMIJabfddkuRGDniiCNSJCjGW1atWpX222+/2swi+fOpT30qHXnkkVkfI34TXZYvX56e9axnpTlz5mSJppNPPjkddNBBaYsttki77757Ou+88yZalXIECFQk4P7s/hx/COD+XNEFploCBAgQIFCyQDP+T7pkFNURIECAAAECBJooMGPGjKFubbTRRkPvp/ub6NdY/bnlllvSW97ylnTPPfdkI3K++c1vpjvvvDO99KUvTZ/5zGfSrrvumm6++ea2BDGy58ADD0ybb75523JVbmyNXZF27rrrrjRr1qysj/HYsCuvvDL99Kc/TR/72MfSt7/97fS2t70tLVmypEiVyhIgUIFA6zU+1v2sgmYrr9L9eWxi9+exbWwhQIAAAQLdLCCh0s3RcWwECBAgQIAAgUkKfOQjH0mPPvromHs36Qu76GS7ETdvfetbs1Eq8cVe/Gy11VbpP/7jP7K5Vn71q1+lD3zgA2M6Pf744+mLX/xiOvTQQzcoE/t/73vf22Bdt36IUToxgifvf1i9613vykbrxGiXs88+O/3kJz/p1sN3XAQaJ+D+/GRI3Z/dn588G7wjQIAAAQLTQ0BCZXrEyVESIECAAAECBCYs8J//+Z/puOOOa5tQaZeAmHBDXVRwrATRPvvskz3aavihxmiTN77xjdnqGMUy1vK1r30tm3ckHpOVLw899FBavHhxNidJvq5bX7fddttsdM1ox3f44YdnqyNp9P3vf3+0ItYRIFCygPvzk6Duz+7PT54N3hEgQIAAgekjYFL66RMrR0qAAAECBAgQmJDA0qVLR51PpHXnsRIQrWXGex8jYOLxWTHHx/AlRjzcdttt2WOy5s2bN3zzlD//6Ec/yiaZf9rTnpbmz58/5iO/LrroomxkxmgN5pOyb7LJJqNtztblj/tqLROPyxoYGBhzn27aEImfsZa8/7G9tX9jlbeeAIGpC7g/P2no/uz+/OTZ4B0BAgQIEJg+AkaoTJ9YOVICBAgQIECAQFuBq666Kr3mNa9JMU9ILAcccEBauHBhevOb3zxiv0ioxKiEmAg3RjHEiJWYqP1P//RPNxjZ8q//+q9ZHVFP/EQC5YEHHsgmt48v5GOi9Hx55JFH0jHHHJNiguVtttkm9ff3Z6NDXvnKV446muPv//7vszJPf/rT04477ph+//d/Pxs18pWvfCWvcoPXJ554In36059Oe+65Z3r+85+f9t1332wulDiO6667boOy+Yd4zNVYy3e/+91s00te8pJRizz22GPp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gAABAgQIECBAgAABAgQIECDQEAEJlYYEUjcIECBAgAABAgQIECBAgAABAgQIECBAgACB6gQkVKqzVTMBAgQIECBAgAABAgQIECBAgAABAgQIECDQEAEJlYYEUjcIECBAgAABAgQIECBAgAABAgQIECBAgACB6gQkVKqzVTMBAgQIECBAgAABAgQIECBAgAABAgQIECDQEAEJlYYEUjcIECBAgAABAgQIECBAgAABAgQIECBAgACB6gQkVKqzVTMBAgQIECBAgAABAgQIECBAgAABAgQIECDQEIFZDemHbhAgQIAAAQIEprXAypUrp/XxO3gCzmHnQFMFnNtNjWzv9Ms53Dux1lMCBAgQqF5g1uDgYOFWJrNP4UZG2UG7o6BUsIpzBaijVMl5FJQKVnGuAHWUKjmPglLBKs4VoI5SZSed161bN3QE8WWHLzyGOLyZ5gJxbnfyWsq56mgz2tZuHoFqXzvp7P5cbSzVXp+A+3Nn7Dt5v2rtkXZbNap7z7k629aaObdqVPeec3HbWX19fYX2CuSi+xRqYIzCvdbuwMAA5zHOhTJX13VeiW+ZURy7LvEd26bMLXU519Wu67fMs2fsunolvrNnzx4bwRYC01ggzu1O/z+D+3NnThj35844a4VAVQLuz1XJPllvXffJutr17++Tsa/ynfhWqftk3XU519Wu6/fJ2Bd555FfRbSUJUCAAAECBAiUKLBgwYK0bNmyFH8tWkdypdfajf9hmDNnTokRnFhVveYc/Y1z20JgOgu4P3c2eu7PnfF2f+6Ms1YIECBAoNkCEirNjq/eESBAgAABAl0s0N/fn+Knrr9I6rV2165dm+bOndvxM6LXnOvqb8cDq8FGC7g/dza87s+d8XZ/7oyzVggQIECg2QIzm909vSNAgAABAgQIECBAgAABAgQIECBAgAABAgQITF1AQmXqhmogQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEGi4godLwAOseAQIECBAgQIAAAQIECBAgQIAAAQIECBAgMHUBCZWpG6qBAAECBAgQIECAAAECBAgQIECAAAECBAgQaLiAhErDA6x7BAgQIECAAAECBAgQIECAAAECBAgQIECAwNQFJFSmbqgGAgQIECBAgAABAgQIECBAgAABAgQIECBAoOECEioND7DuESBAgAABAgQIECBAgAABAgQIECBAgAABAlMXkFCZuqEaCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgYYLSKg0PMC6R4AAAQIECBAgQIAAAQIECBAgQIAAAQIECExdQEJl6oZqIECAAAECBAgQIECAAAECBAgQIECAAAECBBouIKHS8ADrHgECBAgQIECAAAECBAgQIECAAAECBAgQIDB1AQmVqRuqgQABAgQIECBAgAABAgQIECBAgAABAgQIEGi4gIRKwwOsewQIECBAgAABAgQIECBAgAABAgQIECBAgMDUBSRUpm6oBgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKDhAhIqDQ+w7hEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJTF5BQmbqhGggQIECAAAECBAgQIECAAAECBAgQIECAAIGGC0ioNDzAukeAAAECBAgQIECAAAECBAgQIECAAAECBAhMXUBCZeqGaiBAgAABAgQIECBAgAABAgQIECBAgAABAgQaLjCr4f3TPQIECBAgQIAAAQIECBAgQIAAAQIECBAgQGAUgaOOOiptu+22acGCBam/v3+UEla1CkiotGp4T4AAAQIECBAgQIAAAQIECBAgQIAAAQIEekRgzZo1acWKFVlvI7GyePHiNHfu3Oy1RwgKdVNCpRCXwgQIECBAgAABAgQIECBAgAABAgQIECBAoHkCkVxZtmxZ1rGTTz55KKmydOnS5nV2kj0yh8ok4exGgAABAgQIECBAgAABAgQIECBAgAABAgSaKJAnVyLBMmPGjLRw4cIUSZZeXyRUev0M0H8CBAgQIECAAAECBAgQIECAAAECBAgQINBGYOXKldnolV5PrkiotDlJbCJAgAABAgQIECBAgAABAgQIECBAgAABAgSeFGhNrmy33XY9NXJFQuXJ88A7AgQIECBAgAABAgQIECBAgAABAgQIECBAYIIC+aPBYuRKLyRXZqxfv379BG2yYoODg6mvr6/ILqWUfe9735tmz55dSl1FKlm3bl0t7Q4MDKQ5c+YUOdRSytbV315rV3xLOV3HraSu80p8xw1NKQXEtxTGcSupy7mudl2/454SpRQQ31IYx62kLue62nX9jntKlFJAfEthHLeSupzratf1O+4pUUoB8S2FcdxK6nKuq13X77inRCkFxLcUxnErqcu5rnbz63fFihUpkiJlL9tuu202qf2RRx6Z4n2+1JVfKKvdGQMDA4USKnnHO/1aR3Kh033UHgECBAgQIECAAAECBAgQIECAAAECBAgQaJLAc57znLRo0aLsJ95P52VW0dEmZWVypjOaYydAgAABAgQIECBAgAABAgQIECBAgAABAgTGF5g5c2b2FKj77rsvRUKlaE5i/BbGL1FWXmPW+E11R4n3vOc9tTx6q+4hV53Wr6u/vdZuPqROfKsVqOu8Et9q45rXLr65RLWvdTnX1a7rt9rzKa9dfHOJal/rcq6rXddvtedTXrv45hLVvtblXFe7rt9qz6e8dvHNJap9rcu5rnZdv9WeT3nt4ptLVPtal3Nd7ebXb9WP/FqwYEHq7+8fCl4kNqbzMq0SKtM5c1X0JFm7dm2aO3du0d2mXL6sTF3RA+m1dsW36BkyufJ1nVfiO7l4Fd1LfIuKTa58Xc51tev6ndx5UnQv8S0qNrnydTnX1a7rd3LnSdG9xLeo2OTK1+VcV7uu38mdJ0X3Et+iYpMrX5dzXe26fid3nhTdS3yLik2ufF3OdbWbX78rV64sbQ6VseZNmVxEunOvaZNQ6U4+R0WAAAECBAgQIECAAAECBAgQIECAAAECBHpPIBIo8RMTz8colNbJ55uqIaHS1MjqFwECBAgQIECAAAECBAgQIECAAAECBAgQKFGgNYmyePHiEmueHlVJqEyPODlKAgQIECBAgAABAgQIECBAgAABAgQIECDQcYFIosQIlJgPpReTKK3gEiqtGt4TIECAAAECBAgQIECAAAECBAgQIECAAIEeF5BEGf0EkFAZ3cVaAgQIECBAgAABAgQIECBAgAABAgQIECDQMwKSKOOHWkJlfCMlCBAgQIAAAQIECBAgQIAAAQIECBAgQIBA4wQiiRKP8conlm9cB0vukIRKyaCqI0CAAAECBAgQIECAAAECBAgQIECAAAEC00Hg/PPPnw6H2TXHOLNrjsSBECBAgAABAgQIECBAgAABAgQIECBAgAABAgS6VEBCpUsD47AIECBAgAABAgQIECBAgAABAgQIECBAgACB7hGQUOmeWDgSAgQIECBAgAABAgQIECBAgAABAgQIECBAoEsFJFS6NDAOiwABAgQIECBAgAABAgQIECBAgAABAgQIEOgeAQmV7omFIyFAgAABAgQIECBAgAABAgQIECBAgAABAgS6VEBCpUsD47AIECBAgAABAgQIECBAgAABAgQIECBAgACB7hGQUOmeWDgSAgQIECBAgAABAgQIECBAgAABAgQIECBAoEsFJFS6NDAOiwABAgQIECBAgAABAgQIECBAgAABAgQIEOgeAQmV7omFIyFAgAABAgQIECBAgAABAgQIECBAgAABAgS6VEBCpUsD47AIECBAgAABAgQIECBAgAABAgQIECBAgACB7hGQUOmeWDgSAgQIECBAgAABAgQIECBAgAABAgQIECBAoEsFJFS6NDAOiwABAgQIECBAgAABAgQIECBAgAABAgQIEOgeAQmV7omFIyFAgAABAgQIECBAgAABAgQIECBAgAABAgS6VEBCpUsD47AIECBAgAABAgQIECBAgAABAgQIECBAgACB7hGQUOmeWDgSAgQIECBAgAABAgQIECBAgAABAgQIECBAoEsFJFS6NDAOiwABAgQIECBAgAABAgQIECBAgAABAgQIEOgeAQmV7omFIyFAgAABAgQIECBAgAABAgQIECBAgAABAgS6VEBCpUsD47AIECBAgAABAgQIECBAgAABAgQIECBAgACB7hGQUOmeWDgSAgQIECBAgAABAgQIECBAgAABAgQIECBAoEsFZgwMDKzv0mPr6cMaGBhIc+bM6WmDJndefJsc3ZTEV3ybLdDs3rl+xbfZAs3unetXfJst0OzeuX7Ft9kCze6d61d8my3Q7N65ficX31l9fX2F9hwcHExF9ynUwBiFe63dOKE5j3EylLi6rvNKfEsMYpuqxLcNTomb6nKuq13Xb4knT5uqxLcNTomb6nKuq13Xb4knT5uqxLcNTomb6nKuq13Xb4knT5uqxLcNTomb6nKuq13Xb4knT5uqxLcNTomb6nKuq13Xb4knT5uqxLcNTombynL2yK8Sg6IqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKSKiUiKkqAgQIECBAgAABAgQIECBAgAABAgQIECBAoJkCEirNjKteESBAgAABAgQIECBAgAABAgQIECBAgAABAiUKzFizZs36EutTFQECBAgQIECAAAECBAgQIECAAAECBAgQIECgcQIz1q9fXyihMjg4mPr6+joO0Wvtrl27Ns2dO5dzxQJ1nVfiW3Fg/7968W22s/iKbxUC7s9VqI6s0/U70qSKNXU519Wu67eKs2hkneI70qSKNXU519Wu67eKs2hkneI70qSKNXU519Wu67eKs2hkneI70qSKNXU519Wu63dyZ5FHfk3OzV4ECBAgQIAAAQIEek7guuuuS9dff33P9VuHCRAgQIAAAQIECBAgEAISKs4DAgQIECBAgAABAg0X+OAHP5hmzpw56Z+HHnooXXXVVellL3tZ2muvvdLXvva1hovpHgECBAgQIECAAAECBEYKSKiMNLGGAAECBAgQIECAQOMEXvGKV6Qrr7wy3Xbbbenxxx/Pfh555JEUTwCOnxNOOCE98MAD6e6770633npruuGGG9L555+fbQuMjTfeeKjsXXfd1TgfHSJAgAABAgQIECBAgMB4ArPGK2A7AQIECBAgQIAAAQLTX+AlL3lJ6u/v36AjM2bMGPoc7zfbbLPsJ1+50047pcWLF2cf995773TppZem1atXp0WLFuVFvBIgQIAAAQIECBAgQKBnBCRUeibUOkqAAAECBAgQINDLAs997nMLd3/27Nlpyy23HNrvgAMOSPFjIUCAAAECBAgQIECAQC8KSKj0YtT1mQABAgQIECBAoKcE3ve+9026v/fcc09qHcky6YqmuOPPfvaz9IMf/CAbQTN//vwp1mZ3AgQIECBAgAABAgQIFBcwh0pxM3sQIECAAAECBAgQ6BmBSKasWLEivepVr0oLFy7Mfq6++uqh/q9atWpofWy/5ZZb0ic+8Yl06KGHpt/93d9NM2fOTPPmzUtXXHFF+vWvf52WL1+eXvnKV6ZNN90027bddtul448/Pts2VOn/v1m3bl067rjj0jbbbJO23nrr7JFl8eiyl7/85enmm28eXtxnAgQIECBAgAABAgQIVCogoVIpr8oJECBAgAABAgQITH+BmEflwgsvzCa0X7lyZbr33nuHOrVgwYJ01llnpWuvvTbFtsMOOyz9z//8T3rhC1+Y/vzP/zztvPPO6cYbb0z7779/2m233dLll1+e9t133yxR8prXvCatWbMmnX766enUU08dqjN/c8ghh6Qzzjgjvf71r08xQuXRRx9N73znO9M3v/nNLLkS6ywECBAgQIAAAQIECBDolIBHfnVKWjsECBAgQIAAAQIEprHAFltskTbZZJNRe7DLLrukjTbaKNv24Q9/OBudEiNb1q9fn0466aS0xx57ZCNKlixZkt7+9rcPPUIsth9zzDHpzDPPTJdddllatmzZUP2XXHJJuvTSS7PRKTHiJUa6xHL22WdnCZ1I8MT7U045ZWgfbwgQIECAAAECBAgQIFClgBEqVeqqmwABAgQIECBAgECPCUQiJZ9zJV6f+tSnpj333DNT+MlPfjK0LVbE9gMPPDDbduedd24gFY8Gi+Xggw8eSqbE59gnRszEcvHFF2ev/kOAAAECBAgQIECAAIFOCEiodEJZGwQIECBAgAABAgR6WCAfXdL6qLCcY9as3w6af+yxx/JV2esNN9yQvW6//fYbrI8Pm2++ebbujjvuGLHNCgIECBAgQIAAAQIECFQl4JFfVcmqlwABAgQIECBAgACBDQSeeOKJDT63+/CLX/wi2xyP+7rooos2KDowMJB9jknuLQQIECBAgAABAgQIEOiUgIRKp6S1Q4AAAQIECBAgQKDHBYokVH7zm99kWi94wQvS/PnzR8gddNBBKR/dMmKjFQQIECBAgAABAgQIEKhAQEKlAlRVEiBAgAABAgQIECAwUqBIAiQe63X//fenQw45JB1xxBEjK7OGAAECBAgQIECAAAECHRYwh0qHwTVHgAABAgQIECBAoFcFYoL6iS5z587Nit59990T3UU5AgQIECBAgAABAgQIVCogoVIpr8oJECBAgAABAgQIEMgFZsyYkb8d93WvvfbKynzuc59L69evH7e8AgQIECBAgAABAgQIEKhaQEKlamH1EyBAgAABAgQIECCQCRRJjBx99NEpEjC33HJLWrJkCUECBAgQIECAAAECBAjULiChUnsIHAABAgQIECBAgACBzgrE3CTXXHNNOvfcc4cavu6669KXvvSldNttt40YEfLggw+m1atXp1/96ldZ+Shz1113ZeVi3cqVK9Pjjz+ebbv99tvTvffem72PSejXrFmTfv7zn2ef4/Fd8TkvG+VuvfXWbNtjjz2Wbrzxxux9/Ccmoz/ttNOyz2eddVbaaaed0umnn56+8pWvpI9//OPp0EMPzV6HdvCGAAECBAgQIECAAAECFQuYlL5iYNUTIECAAAECBAgQ6DaBf/qnf0oDAwPZYS1dunTo8G666aYUP4sWLUo77LDD0Pqzzz47Pfroo+mtb31rti6SKMuXL08HHHBANookEionnHBCtm1wcDCdc8456dhjj82SJRdffHGaN29e9hMFVqxYkfbbb78sQRLlYtRKfgwXXXRRevjhh9Pee++d1fXud7877b777unDH/5wuuKKK9JJJ52U5s+fn/bZZ5901FFHpf333z8r5z8ECBAgQIAAAQIECBDohICESieUtUGAAAECBAgQIECgiwTicVpFlve9731ti++xxx5D2yOh0tfXl32OZEj8jLXkiZSxtsf6hQsXpv7+/hFFiszHMmJnKwgQIECAAAECBAgQIDAJAQmVSaDZhQABAgQIECBAgACBzglInnTOWksECBAgQIAAAQIECIwtYA6VsW1sIUCAAAECBAgQIECAAAECBAgQIECAAAECBAhkAhIqTgQCBAgQIECAAAECBAgQIECAAAECBAgQIECAwDgCEirjANlMgAABAgQIECBAgAABAgQIECBAgAABAgQIEJBQcQ4QIECAAAECBAgQIECAAAECBAgQIECAAAECBMYRkFAZB8hmAgQIECBAgAABAgQIECBAgAABAgQIECBAgICEinOAAAECBAgQIECAAAECBAgQIECAAAECBAgQIDCOgITKOEA2EyBAgAABAgQIECBAgAABAgQIECBAgAABAgRmDAwMrMfQfQIDAwNpzpw53XdgjqgUAfEthbFrKxHfrg1NKQcmvqUwdm0l4tu1oSnlwMS3FMaurUR8uzY0pRyY+JbC2LWViG/XhqaUAxPfUhi7thLx7drQlHJg4lsKY9dWIr6TC82svr6+QnsODg6movsUamCMwr3WbpzQnMc4GUpcXdd5Jb4lBrFNVeLbBqfETXU519Wu67fEk6dNVeLbBqfETXU519Wu67fEk6dNVeLbBqfETXU519Wu67fEk6dNVeLbBqfETXU519Wu67fEk6dNVeLbBqfETXU519Wu67fEk6dNVeLbBqfEsYkb4AAAATNJREFUTWU5e+RXiUFRFQECBAgQIECAAAECBAgQIECAAAECBAgQINBMAQmVZsZVrwgQIECAAAECBAgQIECAAAECBAgQIECAAIESBSRUSsRUFQECBAgQIECAAAECBAgQIECAAAECBAgQINBMAQmVZsZVrwgQIECAAAECBAgQIECAAAECBAgQIECAAIESBSRUSsRUFQECBAgQIECAAAECBAgQIECAAAECBAgQINBMAQmVZsZVrwgQIECAAAECBAgQIECAAAECBAgQIECAAIESBSRUSsRUFQECBAgQIECAAAECBAgQIECAAAECBAgQINBMAQmVZsZVrwgQIECAAAECBAgQIECAAAECBAgQIECAAIESBSRUSsRUFQECBAgQIECAAAECBAgQIECAAAECBAgQINBMgf8DkcxYdmDMnR4AAAAASUVORK5CYII=)

图中出现了 thread 和 task 两种切换顺序的不同方式，分别对应 Python 中并发的两种形式——threading 和 asyncio。

对于 threading，操作系统知道每个线程的所有信息，因此它会做主在适当的时候做线程切换。很显然，这样的好处是代码容易书写，因为程序员不需要做任何切换操作的处理；但是切换线程的操作，也有可能出现在一个语句执行的过程中（比如 x += 1），这样就容易出现 race condition 的情况。

而对于 asyncio，主程序想要切换任务时，必须得到此任务可以被切换的通知，这样一来也就可以避免刚刚提到的 race condition 的情况。

- 并行，指的才是同一时刻、同时发生。Python 中的 multi-processing 便是这个意思，对于 multi-processing，你可以简单地这么理解：比如你的电脑是 6 核处理器，那么在运行程序时，就可以强制 Python 开 6 个进程，同时执行，以加快运行速度，它的原理示意图如下：

![img](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABjYAAAI2CAYAAADzb7G3AAAgAElEQVR4AezdC5BcVZ0w8JOYSAjKREA0bMmQDRSiPJIQQZaFJIjELbUKSxFhCewa10eJJeLCEhZI4ANJLGV9oLUFakHJriiUK6IoPjAUKo+gZiUIKoYMoCXycEZEAiLz1f983vlmMjNJ9zCnbzf9O1VDd98+r/s7905N7p9zzpTBwcHB1EQaGBhIPT09TZSYnKzd1m5fX1/q7e2dHLwmauk257rO1/g2cVE+i6zG91ngNVG0Lue62nX/NnFxPIusxvdZ4DVRtC7nutp1/zZxcTyLrMb3WeA1UbQu57radf82cXE8i6zG91ngNVG0Lue62nX/NnFxPIusxvdZ4DVRtC7nutp1/zZxcTyLrMZ3YnhTJ1ZMKQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBA6wUENlpvrkUCBAgQIECAAAECBAgQIECAAAECBAgQIEBgggICGxOEU4wAAQIECBAgQIAAAQIECBAgQIAAAQIECBBovYDARuvNtUiAAAECBAgQIECAAAECBAgQIECAAAECBAhMUEBgY4JwihEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQKtFxDYaL25FgkQIECAAAECBAgQIECAAAECBAgQIECAAIEJCkzZtGnT4ATLKkaAAAECBAgQIECAAAECBAgQIECAAAECBAgQaKnAlMHBwaYCGwMDA6mnp6elnYzGuq3dvr6+1Nvby7mwQF3XlfEtPLB/rd74Predja/xLSHg93MJ1dF1un9Hm5Q4UpdzXe26f0tcRaPrNL6jTUocqcu5rnbdvyWuotF1Gt/RJiWO1OVcV7vu3xJX0eg6je9okxJH6nKuq91Ov38tRVXiLlAnAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUERAYKMIq0oJECBAgAABAgQIECBAgAABAgQIECBAgACBEgICGyVU1UmAAAECBAgQIECAAAECBAgQIECAAAECBAgUERDYKMKqUgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCEgMBGCVV1EiBAgAABAgQIECBAgAABAgQIECBAgAABAkUEBDaKsKqUAAECBAgQIECAAAECBAgQIECAAAECBAgQKCEgsFFCVZ0ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAEQGBjSKsKiVAgAABAgQIECBAgAABAgQIECBAgAABAgRKCAhslFBVJwECBAgQIECAAAECBAgQIECAAAECBAgQIFBEQGCjCKtKCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgRICAhslVNVJgAABAgQIECBAgAABAgQIECBAgAABAgQIFBEQ2CjCqlICBAgQIECAAAECBAgQIECAAAECBAgQIECghIDARglVdRIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJFBAQ2irCqlAABAgQIECBAgAABAgQIECBAgAABAgQIECghILBRQlWdBAgQIECAAAECBAgQIECAAAECBAgQIECAQBEBgY0irColQIAAAQIECBAgQIAAAQIECBAgQIAAAQIESggIbJRQVScBAgQIECBAgAABAgQIECBAgAABAgQIECBQREBgowirSgkQIECAAAECBAgQIECAAAECBAgQIECAAIESAgIbJVTVSYAAAQIECBAgQIAAAQIECBAgQIAAAQIECBQRENgowqpSAgQIECBAgAABAgQIECBAgAABAgQIECBAoISAwEYJVXUSIECAAAECBAgQIECAAAECBAgQIECAAAECRQQENoqwqpQAAQIECBAgQIAAAQIECBAgQIAAAQIECBAoISCwUUJVnQQIECBAgAABAgQIECBAgAABAgQIECBAgEARAYGNIqwqJUCAAAECBAgQIECAAAECBAgQIECAAAECBEoICGyUUFUnAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUERAYKMIq0oJECBAgAABAgQIECBAgAABAgQIECBAgACBEgICGyVU1UmAAAECBAgQIECAAAECBAgQIECAAAECBAgUEZhWpFaVTlhg7dq16cYbb0z9/f1p1qxZE65nogU3b96cZsyYMdHiEy7Xbe0a3wlfKk0VrOu6Mr5NDdOEMxvfCdM1VbAu57radf82dXlMOLPxnTBdUwXrcq6rXfdvU5fHhDMb3wnTNVWwLue62nX/NnV5TDiz8Z0wXVMF63Kuq91uvH+XLl2aFi9e3NR1ITMBApMvMG1gYKDpWidSpulGxijQDe1ef/31afXq1WOcvUMECBAgQIAAAQIECBAgQIAAAQIECNQtMH/+/JZ3oRueiw5Hdb7DNcq972TnaT09PU3JxMk2W6apBsbJ3C3t1jFbYhxyhwkQIECAAAECBAgQIECAAAECBAgQGCYQz+5a/Wy0rueiMSOn1eca1HWdb7e12+njaymqYb+Y2u1tTGszta3dRkV/CBAgQIAAAQIECBAgQIAAAQIEukkglo6PH4kAgfYRENhon7EY1ZMIaqxcuXLUcQcIECBAgAABAgQIECBAgAABAgQIEGidgMBG66y1RKARgamNZJKHAAECBAgQIECAAAECBAgQIECAAAECBAgQINAOAgIb7TAK+kCAAAECBAgQIECAAAECBAgQIECAAAECBAg0JCCw0RCTTAQIECBAgAABAgQIECBAgAABAgQIECBAgEA7CAhstMMo6AMBAgQIECBAgAABAgQIECBAgAABAgQIECDQkIDARkNMMhEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQLtICCw0Q6joA8ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAQwICGw0xyUSAAAECBAgQIECAAAECBAgQIECAAAECBAi0g4DARjuMgj4QIECAAAECBAgQIECAAAECBAgQIECAAAECDQkIbDTEJBMBAgQIECBAgAABAgQIECBAgAABAgQIECDQDgICG+0wCvpAgAABAgQIECBAgAABAgQIECBAgAABAgQINCQgsNEQk0wECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAOwgIbLTDKOgDAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0JCAwEZDTDIRIECAAAECBAgQIECAAAECBAgQIECAAAEC7SAgsNEOo6APBAgQIECAAAECBGoWePDBB9O9995bcy80T4AAAQIECBAgQIAAgW0LCGxs20gOAgQIECBAgACBmgXWr1+f9t133zRr1qw0ZcqUET9Tp05Nf/M3f5MWLVqUzjrrrHTHHXfU3NvOav7JJ59Mq1evTnPnzk2XXnppZ3VebwkQIECAAAECBAgQ6EoBgY2uHHYnTYAAAQIECBDoLIF58+alDRs2pP7+/rTTTjvlzp9wwgk5iHHDDTekNWvWpNmzZ6cLLrggLViwIH3sYx/rrBOsqbfXXHNN2nvvvdOKFSvS448/XlMvNEuAAAECBAgQIECAAIHmBKY1l11uAgQIECBAgAABAu0h8LznPS/P4qh6E4GOmLlx0UUXpQ984APp1a9+df6pvvf6/wUeeOCBFF73339/+sd//Mf0jW98I/3kJz/5/xm8I0CAAAECBAgQIECAQBsLmLHRxoOjawQIECBAgAABAs0JxIyNnp6eXOjCCy9srnAX5X7iiSfShz/84fSrX/0qz3LZZZdduujsnSoBAgQIECBAgAABAp0uILDR6SOo/wQIECBAgAABAkMCM2bMSAcddFD+/Mtf/nLo+HhvnnrqqXTPPfeM+XU8/L/11lvT2rVr00MPPTRmnrEO/u53v0u33HJL6uvrS88888xYWYaObd68Od12223pxhtvbOlSUHvttdeQ01BnvCFAgAABAgQIECBAgECHCAhsdMhA6SYBAgQIECBAgEBjAtttt13O+Oijj+bXq6++Oi1evHjo57777kt/+MMf0nvf+968GfmJJ544ouKf/exneZmmHXfcMS9ltWTJkvSyl70svfOd70wRtBgrRQAj9vmYM2dOeslLXpIOOeSQtMcee6Ttt98+RRDhhz/84Yhi3/rWt3KeF7zgBenggw/Ofdt9993Tpz71qRH54kPsK3LaaaelPffcM2+aHnVG8OYtb3nLqLzf+9730lFHHZVmzpyZ8/b29ua6v/a1r43K6wABAgQIECBAgAABAgQ6VUBgo1NHTr8JECBAgAABAgTGFKhmasRD/UgRAPjkJz+ZNxqPmRGf+MQn0n777ZdnSkyfPn1EHVdccUXet+Pee+9NX/3qV3NQ4fvf/3465phj0qWXXpoOPfTQfGx4oQhqvOENb0hnnHFGesUrXpG+/e1v58DJj3/84/S+970vzwipgixRLup93etel37729+mm2++Oc/qiFkhUc/JJ588IrgxMDCQ9tlnnxSBkM9+9rPpj3/8Y/rBD36QFi5cOCpYEktLHXHEESkCMXfffXcOwsQm6rHc1G9+85vhXfaeAAECBAgQIECAAAECHS1g8/COHj6dJ0CAAAECBAgQGC4QS0D9/Oc/z4ci2FClCGQ8//nPzx8jgLBu3bq066675tdTTjklH4+NtN/xjnekmKkRm2nHa6QIZsTPr3/96xQzIs4+++wcKMlfppRWrVqV87/qVa9K11xzTZo27f/9iT1//vwUP1//+terrDl4EcGOwcHBHMCIMpEWLVqUvvzlL+fAxHnnnZfe/e53p9gc/fLLL88BkHPOOSfnibwLFixIF198cdq4ceNQvfHm/PPPz+e0YsWKoeNvetObcjAkzlkiQIAAAQIECBAgQIDAc0XAjI3nykg6DwIECBAgQIBA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QIAAAQJtITBlMP53rSZSt22i0urzPffcc9OqVavyiMTrypUrmxgdWQkQIECAAAECBAgQIECAAAECBAgQmEyBup/Xtfr5ZGXX19eXent7q48te63rfLut3U4f37Hn67fsMtUQAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBxAYGNxq3kJECAAAECBAgQIECAAAECBAgQIECAAAECBGoWENioeQA0T4AAAQIECBAgQIAAAQIECBAgQIAAAQIECDQuILDRuJWcBAgQIECAAAECBAgQIECAAAECBAgQIECAQM0CAhs1D4DmCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgcYFBDYat5KTAAECBAgQIECAAAECBAgQIECAAAECBAgQqFlAYKPmAdA8AQIECBAgQIAAAQIECBAgQIAAAQIECBAg0LiAwEbjVnISIECAAAECBAgQIECAAAECBAgQIECAAAECNQsIbNQ8AJonQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEGhcQ2GjcSk4CBAgQIECAAAECBAgQIECAAAECBAgQIECgZgGBjZoHQPMECBAgQIAAAQIECBAgQIAAAQIECBAgQIBA4wICG41byUmAAAECBAgQIECAAAECBAgQIECAAAECBAjULCCwUfMAaJ4AAQIECBAgQIAAAQIECBAgQIAAAQIECBBoXEBgo3ErOQkQIECAAAECBAgQIECAAAECBAgQIECAAIGaBQQ2ah4AzRMgQIAAAQIECBAgQIAAAQIECBAgQIAAAQKNCwhsNG4lJwECBAgQIECAAAECBAgQIECAAAECBAgQIFCzgMBGzQOgeQIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBxAYGNxq3kJECAAAECBAgQIECAAAECBAgQIECAAAECBGoWENioeQA0T4AAAQIECBAgQIAAAQIECBAgQIAAAQIECDQuILDRuJWcBAgQIECAAAECBAgQIECAAAECBAgQIECAQM0CAhs1D4DmCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgcYFBDYat5KTAAECBAgQIECAAAECBAgQIECAAAECBAgQqFlgWs3ta34rAmvXrt3Kt74iQIAAAQIECBAgQIAAAQIECBAgQKC0gGd0pYXVT6B5gWkDAwNNl5pImaYbGaNAN7S7efPmoTOPX5p+cQ5xeEOAAAECBAgQIECAAAECBAgQIECgVoF4dlfHM8o62gxo7bbmcuPcvPO0np6epkoFcrNlmmpgnMzd0u6MGTPGEXCYAAECBAgQIECAAAECBAgQIECAAIE6BeLZXaufjdb1XLS/v7/l5xpjW9f5dlu7nT6+lqKq8zfhGG0vWrQorVq1KsWFNWvWrDFylD0UUec6givd1q7xLXsdV7XXdV0Z32oEyr4a37K+Ve11OdfVrvu3Gvmyr8a3rG9Ve13OdbXr/q1Gvuyr8S3rW9Vel3Nd7bp/q5Ev+2p8y/pWtdflXFe73Xj/xrM7iQCB+gUENuofgxE9WLx4cYqfvr6+1NvbO+K7VnzotshkXedrfFtxNdcX4Te+xreEQF2/r7qtXfdviat3dJ11XVfGd/RYlDhifEuojq6zLue62nX/jr4GShwxviVUR9dZl3Nd7bp/R18DJY4Y3xKqo+usy3l0TxwhQGAqAgIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBApwgIbHTKSOknAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkAQ2XAQECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAxwgIbHTMUOkoAQIECBAgQIAAAQIECBAgQIAAAQIECBAgILDhGiBAgAABAgQIECBAgAABAgQIECBAgAABAgQ6RkBgo2OGSkcJECBAgAABAgQIECBAgAABAgQIECBAgAABgQ3XAAECBAgQIECAAAECBAgQIECAAAECBAgQINAxAgIbHTNUOkqAAAECBAgQIECAAAECBAgQIECAAAECBAgIbLgGCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgY4RENjomKHSUQIECBAgQIAAAQIECBAgQIAAAQIECBAgQEBgwzVAgAABAgQIECBAgAABAgQIECBAgAABAgQIdIyAwEbHDJWOEiBAgAABAgQIECBAgAABAgQIECBAgAABAgIbrgECBAgQIECAAAECBAgQIECAAAECBAgQIECgYwQENjpmqHSUAAECBAgQIECAAAECBAgQIECAAAECBAgQENhwDRAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIdIyCw0TFDpaMECBAgQIAAAQIECBAgQIAAAQIECBAgQICAwIZrgAABAgQIECBAgAABAgQIECBAgAABAgQIEOgYAYGNjhkqHSVAgAABAgQIECBAgAABAgQIECBAgAABAgQENlwDBAgQIECAAAECBAgQIECAAAECBAgQIECAQMcICGx0zFDpKAECBAgQIECAAAECBAgQIECAAAECBAgQICCw4RogQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEOkZAYKNjhkpHCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAAYEN1wABAgQIECBAgAABAgQIECBAgAABAgQIECDQMQICGx0zVDpKgAABAgQIECBAgAABAgQIECBAgAABAgQICGy4BggQIECAAAECBAgQIECAAAECBAgQIECAAIGOERDY6Jih0lECBAgQIECAAAECBAgQIECAAAECBAgQIEBgyqZNmwYxECBAgAABAgQIECBAgAABAgQIECBAgAABAgQ6QWDK4OBgU4GNgYGB1NPT0/Jz67Z2+/r6Um9vL+fCAnVdV8a38MD+tXrj+9x2Nr7Gt4SA388lVEfX6f4dbVLiSF3OdbXr/i1xFY2u0/iONilxpC7nutp1/5a4ikbXaXxHm5Q4UpdzXe26f0tcRaPrNL6jTUocqcu5rnY7/f61FFWJu0CdBAgQIECAAAECBAgQIECAAAECBAgQIECAQBEBgY0irColQIAAAQIECBAgQIAAAQIECBAgQIAAAQIESggIbJRQVScBAgQIECBAgAABAgQIECBAgAABAgQIECBQREBgowirSgkQIECAAAECBAgQIECAAAECBAgQIECAAIESAgIbJVTVSYAAAQIECBAgQIAAAQIECBAgQIAAAQIECBQRENgowqpSAgQIECBAgAABAgQIECBAgAABAgQIECBAoISAwEYJVXUSIECAAAECBAgQIECAAAECBAgQIECAAAECRQQENoqwqpQAAQIECBAgQIAAAQIECBAgQIAAAQIECBAoISCwUUJVnQQIECBAgAABAgQIECBAgAABAgQIECBAgEARAYGNIqwqJUCAAAECBAgQIECAAAECBAgQIECAAAECBEoICGyUUFUnAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUERAYKMIq0oJECBAgAABAgQIECBAgAABAgQIECBAgACBEgICGyVU1UmAAAECBAgQIECAAAECBAgQIECAAAECBAgUERDYKMKqUgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCEgMBGCVV1EiBAgAABAgQIECBAgAABAgQIECBAgAABAkUEBDaKsKqUAAECBAgQIECAAAECBAgQIECAAAECBAgQKCEgsFFCVZ0ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAEQGBjSKsKiVAgAABAgQIECBAgAABAgQIECBAgAABAgRKCAhslFBVJwECBAgQIECAAAECBAgQIECAAAECBAgQIFBEQGCjCMuAx6EAACAASURBVKtKCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgRICAhslVNVJgAABAgQIECBAgAABAgQIECBAgAABAgQIFBEQ2CjCqlICBAgQIECAAAECBAgQIECAAAECBAgQIECghIDARglVdRIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJFBAQ2irCqlAABAgQIECBAgAABAgQIECBAgAABAgQIECghILBRQlWdBAgQIECAAAECBAgQIECAAAECBAgQIECAQBEBgY0irColQIAAAQIECBAgQIAAAQIECBAgQIAAAQIESggIbJRQVScBAgQIECBAgAABAgQIECBAgAABAgQIECBQRGBakVpVOmGBtWvXphtvvDH19/enWbNmTbieiRbcvHlzmjFjxkSLT7hct7VrfCd8qTRVsK7ryvg2NUwTzmx8J0zXVMG6nOtq1/3b1OUx4czGd8J0TRWsy7mudt2/TV0eE85sfCdM11TBupzratf929TlMeHMxnfCdE0VrMu5rna78f5dunRpWrx4cVPXhcwECEy+wLSBgYGma51ImaYbGaNAN7R7/fXXp9WrV49x9g4RIECAAAECBAgQIECAAAECBAgQIFC3wPz581vehW54Ljoc1fkO1yj3vpOdp/X09DQlEyfbbJmmGhgnc7e0W8dsiXHIHSZAgAABAgQIECBAgAABAgQIECBAYJhAPLtr9bPRup6LxoycVp9rUNd1vt3WbqePr6Wohv1iare3Ma3N1LZ2GxX9IUCAAAECBAgQIECAAAECBAgQ6CaBWDo+fiQCBNpHQGCjfcZiVE8iqLFy5cpRxx0gQIAAAQIECBAgQIAAAQIECBAgQKB1AgIbrbPWEoFGBKY2kkkeAgQIECBAgAABAgQIECBAgAABAgQIECBAgEA7CAhstMMo6AMBAgQIECBAgAABAgQIECBAgAABAgQIECDQkIDARkNMMhEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQLtICCw0Q6joA8ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAQwICGw0xyUSAAAECBAgQIECAAAECBAgQIECAAAECBAi0g4DARjuMgj4QIECAAAECBAgQIECAAAECBAgQIECAAAECDQkIbDTEJBMBAgQIECBAgAABAgQIECBAgAABAgQIECDQDgICG+0wCvpAgAABAgQIECBAgAABAgQIECBAgAABAgQINCQgsNEQk0wECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAOwgIbLTDKOgDAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0JCAwEZDTDIRIECAAAECBAgQIECAAAECBAgQIECAAAEC7SAgsNEOo6APBAgQIECAAAECBAgQIECAAAECBAgQIECAQEMCAhsNMclEgAABAgQIECBAgAABAgQIECBAgAABAgQItIPAtHbohD4QIECAAAECBAgQINBagfvuuy9t3LgxTZkyJe20005p7ty5aebMma3thNYIECBAgAABAgQIECAwAQGBjQmgKUKAAAECBAgQINBagfXr16cTTjghPfDAA2lgYGBE4/Fgfvbs2WnPPfdMhx12WDr22GPTfvvtNyKPDyMFFi5cmH70ox+lF7zgBWnevHlp8+bN6Sc/+Uk64IAD0nHHHZc+8IEPpOc973kjC/lEgAABAgQIECBAgACBNhGwFFWbDIRuECBAgAABAgQIjC8QD983bNiQ+vv78+yCyBmBjjvuuCPdcMMNac2aNTm4ccEFF6QFCxakj33sY+NX5pt07733ptNOOy098sgj6aabbkrr1q1Lv/rVr9KLXvSifPw1r3lNDnagIkCAAAECBAgQIECAQDsKCGy046joEwECBAgQIECAwDYFYkbBvvvumxYvXpyDHFdeeWU69dRT09NPP51nHNxyyy3brKObM/zLv/xLev7znz9E0Nvbm77+9a/nwNGNN96YVqxYMfSdNwQIECBAgAABAgQIEGgnAYGNdhoNfSFAgAABAgQIEHhWAjFjo6enJ9dx4YUXPqu6nsuFlyxZkvbaa69Rp7jddtulmK0R6Qtf+MKo7x0gQIAAAQIECBAgQIBAOwgIbLTDKOgDAQIECBAgQIDApAjMmDEjHXTQQbmuX/7yl9us86mnnkr33HPPmPmeeOKJdOutt6a1a9emhx56aMw8Yx383e9+l2K2SF9fX3rmmWfGyjJ0LPa2uO2221LMkHj88ceHjpd+c/XVV4/bRBUYinOO2S8SAQIECBAgQIAAAQIE2k1AYKPdRkR/CBAgQIAAAQIEnpVAzDqI9Oijj+bXeIgfy1VVP/fdd1/6wx/+kN773vemWbNmpRNPPHFEez/72c/y0lY77rhjevWrX51idsPLXvay9M53vjNF0GKsFAGM2Odjzpw56SUveUk65JBD0h577JG23377PDPihz/84Yhi3/rWt3Ke2Lz74IMPzn3bfffd06c+9akR+eJD7CsS+2HE5uixUXrUGcGbt7zlLaPyfu9730tHHXVUmjlzZs4by0vFeX/ta18blXe8A7/+9a/zV/vvv3+aNm3aeNkcJ0CAAAECBAgQIECAQG0CAhu10WuYAAECBAgQIECghEA1UyMe6keKAMAnP/nJvNF4zIz4xCc+kfbbb788U2L69OkjunDFFVfkfTtic+2vfvWrOajw/e9/Px1zzDHp0ksvTYceemg+NrxQBDXe8IY3pDPOOCO94hWvSN/+9rdz4OTHP/5xet/73pdnhFRBligX9b7uda9Lv/3tb9PNN9+cZ3XErJCo5+STTx4R3BgYGEj77LNPikDIZz/72fTHP/4x/eAHP0gLFy5MWwZLPvzhD6cjjjgiB2LuvvvuHISJTdRjU/Df/OY3w7u81ff3339//r5akmqrmX1JgAABAgQIECBAgACBGgT8L1g1oGuSAAECBAgQIECgjEAsAfXzn/88Vx7BhipFIKPaKDsCCOvWrUu77rprfj3llFNytnig/453vCPFTI1vfOMb+TW+iGBG/MRMhpgRcfbZZ+dASVX3qlWrcv5XvepV6Zprrhma5TB//vwUP7Ehd5Wi7Qh2DA4O5gBGlIm0aNGi9OUvfzkHJs4777z07ne/O8Xm6JdffnkOgJxzzjk5T+RdsGBBuvjii9PGjRuravPr+eefn89p+Kbfb3rTm3IwJNptJN11111pw4YNKQI+sRG7RIAAAQIECBAgQIAAgXYUMGOjHUdFnwgQIECAAAECBJoWiMDDcccdl8vFMlBVwGLLimK2RAQ1IkVg4bLLLsvvP/rRj6Ynn3wyve1tbxsKagwv+8EPfjB//NznPje0H8af/vSnFDMlIkVgYaylm2LJq5133jnnuf7661MshRVLUC1dujQfq/4TS17ttttueaZF7LsRKWaORIpyw9PUqVPTN7/5zaFDMbPjsccey2XvuOOOoePxZtmyZemkk04acWy8D3EOkSK4En2RCBAgQIAAAQIECBAg0I4CAhvtOCr6RIAAAQIECBAgsE2B9evXp5gtET8x0yKWbNq0aVOe2RBLTr3whS/cZh2RYa+99sr5YgmpSAcccEB+3fI/1abkEcyItiNdd911ORgSgYYjjzxyyyL5cywvFXtuRLr99tvza+ynETMytkyx50ekOI9IsbRVpJgJsnz58nE3MY8Nv2fPnp3zRj8if7Mpyvz3f/93DricfvrpzRaXnwABAgQIECBAgAABAi0TENhoGbWGCBAgQIAAAQIEJlMg9qiIvSniJ/aRiAf/sa9FfI7AQbOpWtopNv8eK734xS8eCkY8+OCDOUu1H8XcuXNTBDe2lR5++OGhctVm5sNfqz5s3rw554uZFvPmzcvvY6ZIbGIeQZzY4HzLVG08HhucH3300emVr3xluuSSS3LgZcu8W36OGSIxUyXKXHXVVQ2dy5Z1+EyAAAECBAgQIECAAIFWCdhjo1XS2iFAgAABAgQIEJhUgVhSqlpGajIqroIJ1V4cY9W53XbbpZixET+R+vv782scbyQ9/fTTOVvMJomAxpapOhZ7c0SKvtx6663p6quvTmvWrEk//elP8ybisZH4mWeemS644IKhKmI/jdg4PZaTivwR/HjXu96Vl8qKDcur2R9DBf76JuqMZbH+9m//Nt1www0Nz3TZsh6fCRAgQIAAAQIECBAg0CqBabEeb7NpImWabWOs/N3QbvUP6rHO3zECBAgQIECAAIFyAjNmzEjxt1jsszFWig2/q7/VYo+MSNVrzB5pJFXLY82ZMycvodVImQhuHH/88fknZoisXr06ffrTn04f+tCH8t4dwzf53nPPPXOw5zOf+UzelyM2Ko/ZLEcccUTebHzmzJkjmvzRj36Ul9CKpbK+9KUvDZ3PiEw+ECBAgAABAgQIDAnE34N1PKOso804ae0ODX3RN5yb550W6/E2kwK52TLN1D9e3m5pN/5BLREgQIAAAQIECLReIIINd911VxovSNHX15eeeeaZ3LHIGyk2KY8US0zdfffd6eUvf3n+PN5/ent781ex0flEUixFFUtOxd/jF154YbrpppvS8MBGVWdsYv76178+LVy4MM/UiKWzYjbH8P1DbrnllvTa1742vec978mzQaZMmVIV90qAAAECBAgQIDCOQDy7a/Wz0bqei8bs5Fafa7DXdb7d1m6nj++2FwIe5yZ2mAABAgQIECBAgMBzSeCoo47KpxP7dIyVYkPySLEHx7777pvfx0yIaumqs88+e6xiI44dfPDB+XNsDh77WmwrXXrppXnGxZb53vjGN+ZD1VJYjzzySLrooou2zJb7GsGNSFXeeP/d7343Lz/1n//5n3mpKkGNUXQOECBAgAABAgQIECDQxgICG208OLpGgAABAgQIECDQOoFTTjklxV4ZsSTT73//+xENP/744+m8887Lx1asWDG0ifjOO++cZzzEF7GvRSz9VO2jMaKCv35YsGBBOvTQQ/OnE044IT3wwANjZRs6tm7duvSRj3xk6HP1ptpbZJ999smHYvms008/PW05EyQCKFVAZu+99855I6jxD//wD3k2R8ziWLVq1bg/sYyVRIAAAQIECBAgQIAAgXYTsHl4u42I/hAgQIAAAQIECIwpEA/pY+mlJ554In+/YcOG9MUvfjHtv//+KR7aT5069v+zE4GGeED/1FNP5XK/+MUv8vJMu+2224gysaxUzJA46aSTUszeOOuss/LU+8ceeyxFMGPjxo0pNug++eSTR/QvNvCO2Rc333xzuvjii9Pll1+eDjrooLzs00MPPZTuvPPOdOKJJ6b3v//9uVzsf3HYYYflpaGi329/+9vzRuLRv9tvvz2tX78+z6ioGrniiitywGXJkiV5Y+/rrrsuXXLJJWnHHXfMwYwq31/+8pd0zDHHpGOPPTabxPJYcQ4R9IiAy0tf+tKc9Tvf+U7685//nDcKj83Ct5b+7u/+Ls2dO3drWXxHgAABAgQIECBAgACBlgsIbLScXIMECBAgQIAAAQLNCsRD+2qWQsxMqFLsiRE/sTTTgQceWB0e8RoBh5ilEA/3I8UD/wguLF26NMWm2cPTsmXL0rx58/LG3G9+85tTtBsplpC68sor01vf+ta05bJNO+ywQw64fP7zn8/7X0RwItqM4EHkjfpiH4sqxT4c0ec1a9bkAEUEQ6699trcl8MPPzydeeaZVda0fPnyPHvkqquuSh//+MfT9OnTc8Ak6jvttNOG9vjYZZdd0vnnn5++8pWv5GBHBElmz56d245ATHXuUfGRRx6ZAyVDjWzljaDGVnB8RYAAAQIECBAgQIBAbQJTBgcHB5tpvds2UWn1+Z577rl5KYAYk1gWYOXKlc0Mj7wECBAgQIAAAQIECBAgQIAAAQIECEyiQN3P61r9fLKi6+vrS729vdXHlr3Wdb7d1m6nj+/Y8/VbdplqiAABAgQIECBAgAABAgQIECBAgAABAgQIECDQuIDARuNWchIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQI1Cwhs1DwAmidAgAABAgQIECBAgAABAgQIECBAgAABAgQaFxDYaNxKTgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBmAYGNmgdA8wQIECBAgAABAgQIECBAgAABAgQIECBAgEDjAgIbjVvJSYAAAQIECBAgQIAAAQIECBAgQIAAAQIECNQsILBR8wBongABAgQIECBAgAABAgQIECBAgAABAgQIEGhcQGCjcSs5CRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgZoFBDZqHgDNEyBAgAABAgQIECBAgAABAgQIECBAgAABAo0LCGw0biUnAQIECBAgQIAAAQIECBAgQIAAAQIECBAgULOAwEbNA6B5AgQIECBAgAABAgQIECBAgAABAgQIECBAoHEBgY3GreQkQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEahYQ2Kh5ADRPgAABAgQIECBAgAABAgQIECBAgAABAgQINC4gsNG4lZwECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAzQICGzUPgOYJECBAgAABAgQIECBAgAABAgQIECBAgACBxgUENhq3kpMAAQIECBAgQIAAAQIECBAgQIAAAQIECBCoWUBgo+YB0DwBAgQIECBAgAABAgQIECBAgAABAgQIECDQuIDARuNWchIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQI1Cwhs1DwAmidAgAABAgQIECBAgAABAgQIECBAgAABAgQaFxDYaNxKTgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBmAYGNmgdA8wQIECBAgAABAgQIECBAgAABAgQIECBAgEDjAgIbjVvJSYAAAQIECBAgQIAAAQIECBAgQIAAAQIECNQsMK3m9jW/FYG1a9du5VtfESBAgAABAgQIECBAgAABAgQIECBQWsAzutLC6ifQvMC0gYGBpktNpEzTjYxRoBva3bx589CZxy9NvziHOLwhQIAAAQIECBAgQIAAAQIECBAgUKtAPLur4xllHW0GtHZbc7lxbt55Wk9PT1OlArnZMk01ME7mbml3xowZ4wg4TIAAAQIECBAgQIAAAQIECBAgQIBAnQLx7K7Vz0brei7a39/f8nONsa3rfLut3U4fX0tR1fmbcIy2Fy1alFatWpXiwpo1a9YYOcoeiqhzHcGVbmvX+Ja9jqva67qujG81AmVfjW9Z36r2upzratf9W4182VfjW9a3qr0u57radf9WI1/21fiW9a1qr8u5rnbdv9XIl301vmV9q9rrcq6r3W68f+PZnUSAQP0CAhv1j8GIHixevDjFT19fX+rt7R3xXSs+dFtksq7zNb6tuJrri/AbX+NbQqCu31fd1q77t8TVO7rOuq4r4zt6LEocMb4lVEfXWZdzXe26f0dfAyWOGN8SqqPrrMu5rnbdv6OvgRJHjG8J1dF11uU8uieOECAwFQEBAgQIECBAgAABAgQIECBAgAABAgQIECBAoFMEBDY6ZaT0kwABAgQIECBAgAABAgQIECBAgAABAgQIEEgCGy4CAgQIECBAgAABAgQIECBAgAABAgQIECBAoGMEBDY6Zqh0lAABAgQIECBAgAABAgQIECBAgAABAgQIEBDYcA0QIECAAAECBAgQIECAAAECBAgQIECAAAECHSMgsNExQ6WjBAgQIECAAAECBAgQIECAAAECBAgQIECAgMCGa4AAAQIECBAgQIAAAQIECBAgQIAAAQIECBDoGAGBjY4ZKh0lQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEBDZcAwQIECBAgAABAgQIECBAgAABAgQIECBAgEDHCAhsdMxQ6SgBAgQIECBAgAABAgQIECBAgAABAgQIECAgsOEaIECAAAECBAgQIECAAAECBAgQIECAAAECBDpGQGCjY4ZKRwkQIECAAAECBAgQIECAAAECBAgQIECAAAGBDdcAAQIECBAgQIAAAQIECBAgQIAAAQIECBAg0DECAhsdM1Q6SoAAAQIECBAgQIAAAQIECBAgQIAAAQIECAhsuAYIECBAgAABAgQIECBAgAABAgQIECBAgACBjhEQ2OiYodJRAgQIECBAgAABAgQIECBAgAABAgQIECBAQGDDNUCAAAECBAgQIECAAAECBAgQIECAAAECBAh0jIDARscMlY4SIECAAAECBAgQIECAAAECBAgQIECAAAECAhuuAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQKBjBAQ2OmaodJQAAQIECBAgQIAAAQIECBAgQIAAAQIECBAQ2HANECBAgAABAgQIECBAgAABAgQIECBAgAABAh0jILDRMUOlowQIECBAgAABAgQIECBAgAABAgQIECBAgIDAhmuAAAECBAgQIECAAAECBAgQIECAAAECBAgQ6BgBgY2OGSodJUCAAAECBAgQIECAAAECBAgQIECAAAECBAQ2XAMECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAxwgIbHTMUOkoAQIECBAgQIAAAQIECBAgQIAAAQIECBAgMGXTpk2DGAgQIECAAAECBAgQIECAAAECBAgQIECAAAECnSAwZXBwsKnAxsDAQOrp6Wn5uXVbu319fam3t5dzYYG6rivjW3hg/1q98X1uOxtf41tCwO/nEqqj63T/jjYpcaQu57radf+WuIpG12l8R5uUOFKXc13tun9LXEWj6zS+o01KHKnLua523b8lrqLRdRrf0SYljtTlXFe7nX7/WoqqxF2gTgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCIgMBGEVaVEiBAgAABAgQIECBAgAABAgQIECBAgAABAiUEBDZKqKqTAAECBAgQIECAAAECBAgQIECAAAECBAgQKCIgsFGEVaUECBAgQIAAAQIECBAgQIAAAQIECBAgQIBACQGBjRKq6iRAgAABAgQIECBAgAABAgQIECBAgAABAgSKCAhsFGFVKQECBAgQIECAAAECBAgQIECAAAECBAgQIFBCQGCjhKo6CRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgSICAhtFWFVKgAABAgQIECBAgAABAgQIECBAgAABAgQIlBAQ2Cihqk4CBAgQIECAAAECBAgQIECAAAECBAgQIECgiIDARhFWlRIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIlBAQ2SqiqkwABAgQIECBAgAABAgQIECBAgAABAgQIECgiILBRhFWlBAgQIECAAAECBAgQIECAAAECBAgQIECAQAkBgY0SquokQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEiggIbBRhVSkBAgQIECBAgAABAgQIECBAgAABAgQIECBQQkBgo4SqOgkQIECAAAECBAgQIECAAAECBAgQIECAAIEiAgIbRVhVSoAAAQIECBAgQIAAAQIECBAgQIAAAQIECJQQENgooapOAgQIECBAgAABAgQIECBAgAABAgQIECBAoIiAwEYRVpUSIECAAAECBAgQIECAAAECBAgQIECAAAECJQQENkqoqpMAAQIECBAgQIAAAQIECBAgQIAAAQIECBAoIiCwUYRVpQQIECBAgAABAgQIECBAgAABAgQIECBAgEAJAYGNEqrqJECAAAECBAgQIECAAAECBAgQIECAAAECBIoICGwUYVUpAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUEJAYKOEqjoJECBAgAABAgQIECBAgAABAgQIECBAgACBIgICG0VYVUqAAAECBAgQIECAAAECBAgQIECAAAECBAiUEBDYKKGqTgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCIgMBGEVaVEiBAgAABAgQIECBAgAABAgQIECBAgAABAiUEBDZKqKqTAAECBAgQIECAAAECBAgQIECAAAECBAgQKCIwrUitKp2wwNq1a9ONN96Y+vv706xZsyZcz0QLbt68Oc2YMWOixSdcrtvaNb4TvlSaKljXdWV8mxqmCWc2vhOma6pgXc51tev+berymHBm4zthuqYK1uVcV7vu36YujwlnNr4TpmuqYF3OdbXr/m3q8phwZuM7YbqmCtblXFe73Xj/Ll26NC1evLip60JmAgQmX2DawMBA07VOpEzTjYxRoBvavf7669Pq1avHOHuHCBAgQIAAAQIECBAgQIAAAQIECBCoW2D+/Pkt70I3PBcdjup8h2uUe9/JztN6enqakomTbbZMUw2Mk7lb2q1jtsQ45A4TIECAAAECBAgQIECAAAECBAgQIDBMIJ7dtfrZaF3PRWNGTqvPNajrOt9ua7fTx9dSVMN+MbXb25jWZmpbu42K/hAgQIAAAQIECBAgQIAAAQIECHSTQCwdHz8SAQLtIyCw0T5jMaonEdRYuXLlqOMOECBAgAABAgQIECBAgAABAgQIECDQOgGBjdZZa4lAIwJTG8kkDwECBAgQIECAAAECBAgQIECAAAECBAgQIECgHQQENtphFPSBAAECBAgQIECAAAECBAgQIECAAAECBAgQaEhAYKMhJpkIECBAgAABAgQIECBAgAABAgQIECBAgACBdhAQ2GiHUdAHAgQIECBAgAABAgQIECBAgAABAgQIECBAoCEBgY2GmGQiQIAAAQIECBAgQIAAAQIECBAgQIAAAQIE2kFAYKMdRkEfCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgYYEBDYaYpKJAAECBAgQIECAAAECBAgQIECAAAECBAgQaAcBgY12GAV9IECAAAECBAgQIECAAAECBAgQIECAAAECBBoSENhoiEkmAgQIECBAgAABAgQIECBAgAABAgQIECBAoB0EBDbaYRT0gQABAgQIECBAgAABAgQIECBAgAABAgQIEGhIQGCjISaZCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgXYQENhoh1HQBwIECBAgQIAAAQIECBAgQIAAAQIEUIZwmAAAIABJREFUCBAgQKAhAYGNhphkIkCAAAECBAgQIECAAAECBAgQIECAAAECBNpBYFo7dEIfCBAgQIAAAQIECBBorcAzzzyTNm3alO6///7c8K677pr23HPPNH369NZ2RGsECBAgQIAAAQIECBBoUkBgo0kw2QkQIECAAAECBFovsH79+nTCCSekBx54IA0MDIzowJQpU9Ls2bPzQ/nDDjssHXvssWm//fYbkceHkQKHH354uu2229LUqVPT/Pnz09NPP51+8pOfpOc973npLW95SzrnnHPSXnvtNbKQTwQIECBAgAABAgQIEGgTAUtRtclA6AYBAgQIECBAgMD4AvPmzUsbNmxI/f39aaeddsoZI9Bxxx13pBtuuCGtWbMmBzcuuOCCtGDBgvSxj31s/Mp8k+688860bNmy9PDDD6cf/OAH6dZbb81Bo0MOOSRdccUVaf/998+2qAgQIECAAAECBAgQINCOAgIb7Tgq+kSAAAECBAgQILBNgZhdsO+++6bFixfn2RxXXnllOvXUU/Psgw984APplltu2WYd3Zxh+fLlaebMmUMEsRTVV7/61Rwg2rx5c/o//+f/DH3nDQECBAgQIECAAAECBNpJQGCjnUZDXwgQIECAAAECBJ6VQMzY6OnpyXVceOGFz6qu53Lhv//7v08HHnjgqFN8wQtekI4++uh8PGZ1SAQIECBAgAABAgQIEGhHAYGNdhwVfSJAgAABAgQIEJiQwIwZM9JBBx2Uy/7yl7/cZh1PPfVUuueee8bM98QTT+QlmtauXZseeuihMfOMdfB3v/tdni3S19eXYoPuraWYGRF7Xdx4443p8ccf31rWSf3ummuuGXeT8Be96EW5re23335S21QZAQIECBAgQIAAAQIEJktAYGOyJNVDgAABAgQIECDQFgLbbbdd7sejjz6aX6+++uq8XFUsWRU/9913X/rDH/6Q3vve96ZZs2alE088cUS/f/azn+WlrXbcccf06le/Oi1ZsiS97GUvS+985ztTBC3GShHAiH0+5syZk17ykpek2Ktijz32SBEciE24f/jDH44o9q1vfSvniRkSBx98cO7X7rvvnj71qU+NyBcfYl+R0047LW+OHhulR50RvIlNvrdM3/ve99JRRx2Vl5iKvL29vbnur33ta1tmHfdznH+khQsXjpvHFwQIECBAgAABAgQIEKhTQGCjTn1tEyBAgAABAgQITLpANVMjHupHigDAJz/5ybwZdsyM+MQnPpH222+/PFNi+vTpI9qPjbNj345777037zcRQYXvf//76ZhjjkmXXnppOvTQQ3OgYXihCGq84Q1vSGeccUZ6xStekb797W/nwMmPf/zj9L73vS/PCKmCLFEu9rF43etel37729+mm2++Oc/qiFkhUc/JJ588IrgxMDCQ9tlnnxSBkM9+9rPpj3/8Y97sO4IOWwZLPvzhD6cjjjgiB2LuvvvuHISJTdR/9atfpd/85jfDuzzu+3Xr1qVrr702RXDo3/7t38bN5wsCBAgQIECAAAECBAjUKTCtzsa1TYAAAQIECBAgQGAyBWLD8J///Oe5ygg2VCkCGc9//vPzxwggxAP82Cw7Xk855ZR8/P7770/veMc7UszU+MY3vpFf44sIZsTPr3/96xQzIs4+++wcKKnqXrVqVc7/qle9KsUST9Om/b8/sefPn5/i5+tf/3qVNQcvItgxODiYAxhRJtKiRYvSl7/85RyYOO+889K73/3uFJujX3755TkAcs455+Q8kXfBggXp4osvThs3bhyqN96cf/75+ZxWrFgxdPxNb3pTDobEOY+VHnnkkfS///u/KYIwERCK4M28efPS5z73uTz7ZKwyjhEgQIAAAQIECBAgQKBuATM26h4B7RMgQIAAAQIECEyKQAQejjvuuFxXLANVBSy2rDxmS0RQI1IEFi677LL8/qMf/Wh68skn09ve9rahoMbwsh/84Afzx3joX+2H8ac//SnFTIlIEVioghrDy8WSVzvvvHM+dP311+elsGIJqqVLlw7Plmda7LbbbnmmRey7ESlmjkSKcsPT1KlT0ze/+c2hQzGz47HHHstl77jjjqHj8WbZsmXppJNOGnGs+hCzPl7zmtfkpa4uueSSPPMklu6K4IZEgAABAgQIECBAgACBdhUQ2GjXkdEvAgQIECBAgACBrQqsX78+xWyJ+ImZFrFk06ZNm/LMhlhy6oUvfOFWy1dfxh4YkWIJqUgHHHBAft3yP9Wm5BHMiLYjXXfddTkYEoGGI488cssi+XMsLxV7bkS6/fbb82vspxEzMrZMsedHpDiPSLG0VaSYCbJ8+fJxNzHv6elJs2fPznmjH5G/kfTGN74xzx6JfTVuuOGGtNNOO6W5c+emww47bOgcG6lHHgIECBAgQIAAAQIECLRSQGCjldraIkCAAAECBAgQmDSB2KMi9qaIn9hHIh78x5JK8TkCB82mammn2Px7rPTiF794KBjx4IMP5iyxfFWkCAZEcGNb6eGHH85Zoly1mfnw16oPmzdvzvlipkU1eyJmisQm5hHEqTb4Ht5etfF4bHB+9NFHp1e+8pUpZmHELJRtpQgKxSbpMXvlC1/4Qt5X5LWvfW2q+rut8r4nQIAAAQIECBAgQIBAKwW2/a+vVvZGWwQIECBAgAABAgQaFIglparARux98R//8R95T4sGi4/KVgUTqr04RmVIKW+qHcdj1kak2Fw8Umy23Uh6+umnc7aYTTI8oFG9jw27V65cOXQe0Zdbb701/dd//Vfaf//9c5AiNhGPoMW///u/j2gy9tOIfTIiGLLDDjvk4Me73vWunHesQMiIwsM+xFJcMVMkghqx54ZEgAABAgQIECBAgACBdhOYFuvxNpsmUqbZNsbK3w3tVv+gHuv8HSNAgAABAgQIECgnMGPGjBR/i403wyE2/K7+Vos9MiJVrzF7pJFULY81Z86cvIRWI2UiuHH88cfnn5jpsXr16vTpT386fehDH8p7d5x66qlD1ey555551sVnPvOZvC9HbFQes1mOOOKIvNn4zJkzh/Ju7U3MQIlgSLXk1tby+o4AAQIECBAg0E0C8fdgHc8o62gzxlW7rbm6OTfvPC3W420mBXKzZZqpf7y83dJu/INaIkCAAAECBAgQaL1ABBvuuuuuNF6Qoq+vLz3zzDO5Y5E3UmxSHilmN9x9993p5S9/ef483n96e3vzV7HR+URSLEUVS07F3+MXXnhhuummm9LwwEZVZ2xi/vrXvz4tXLgwz76IpbNiNkfsH3LLLbfk4M2iRYuq7KNeH3nkkXxsxx13HPWdAwQIECBAgACBbhaIZ3etfjZa13PRmJ3c6nONa6uu8+22djt9fC1F1c2/iZ07AQIECBAgQIDAkMBRRx2V38c+HWOl2JA8UuzBse++++b3MROiWrrq7LPPHqvYiGMHH3xw/hybg992220jvhvrQywFFTMutkyx6XekaimsCERcdNFFW2bLfY3gxvC8cX4xo2O8FDNWIkgT6cADDxwvm+MECBAgQIAAAQIECBCoTUBgozZ6DRMgQIAAAQIECLSTwCmnnJL3yvjSl76Ufv/734/o2uOPP57OO++8fGzFihVDm4jvvPPO6T3veU8+fvXVV6dY+qnaR2NEBX/9sGDBgnTooYfmTyeccEJ64IEHxso2dGzdunXpIx/5yNDn6k1s8h0pNv2OFMGI008/PW05EyQCKFVAZu+99855Yzmq//mf/0n33Xdf/rzlf+I8H3300Ry8iY3KJQIECBAgQIAAAQIECLSbwLR265D+ECBAgAABAgQIEBhLIB7Sx9JLTzzxRP56w4YN6Ytf/GLeVDse2k+dOvb/sxOBhpj18NRTT+Vyv/jFL/LyTLvtttuIMrGsVMyQiM23Y/bGWWedlafeP/bYYymCGRs3bkyxQffJJ588onsXXHBBnn1x8803p4svvjhdfvnl6aCDDsrLPj300EPpzjvvTCeeeGJ6//vfn8vFbInDDjssLw0V/X7729+eNxKP/t1+++15X4vvfve7Q21cccUVOeCyZMmSFHt0XHfddemSSy5JsUxUBDOq9Je//CUdc8wx6dhjj80msTxWnEMEPSLg8tKXvjRn3X777VMEamJZqmh73rx5aZdddkn33ntvDnh85zvfSUceeWSKAE8saSURIECAAAECBAgQIECg3QT8S6XdRkR/CBAgQIAAAQIERgnEQ/tqlsLwh/mxJ0b8xNJM4y2bFAGHCBTEw/1I8cA/ggtLly5NhxxyyIi2li1blh/0x8bcb37zm1O0GymWkLryyivTW9/61jRlypQRZXbYYYcccPn85z+f97+I4ES0+ec//znnjcBBNasjCsY+HNHnNWvW5ABFBEOuvfba3JfDDz88nXnmmUP1L1++PM8eueqqq9LHP/7xNH369ByQiPpOO+20oT0+IjBx/vnnp6985Ss52BFBktmzZ+dziUBMde5RcSyfFcGSCPZEMCMCMRH8iYBHBFr+9V//NdsMdcIbAgQIECBAgAABAgQItJnAlMHBwcFm+tRtm6i0+nzPPffctGrVqjwk8bpy5cpmhkdeAgQIECBAgAABAgQIECBAgAABAgQmUaDu53Wtfj5Z0fX19aXe3t7qY8te6zrfbmu308d37Pn6LbtMNUSAAAECBAgQIECAAAECBAgQIECAAAECBAgQaFxAYKNxKzkJECBAgAABAgQIECBAgAABAgQIECBAgACBmgUENmoeAM0TIECAAAECBAgQIECAAAECBAgQIECAAAECjQsIbDRuJScBAgQIECBAgAABAgQIECBAgAABAgQIECBQs4DARs0DoHkCBAgQIECAAAECBAgQIECAAAECBAgQIECgcQGBjcat5CRAgAABAgQIECBAgAABAgQIECBAgAABAgRqFhDYqHkANE+AAAECBAgQIECAAAECBAgQIECAAAECBAg0LiCw0biVnAQIECBAgAABAgQIECBAgAABAgQIECBAgEDNAgIbNQ+A5gkQIECAAAECBAgQIECAAAECBAgQIECAAIHGBQQ2GreSkwABAgQIECBAgAABAgQIECBAgAABAgQIEKhZQGCj5gHQPAECBAgQIECAAAECBAgQIECAAAECBAgQINC4gMBG41ZyEiBAgAABAgQIECBAgAABAgQIECBAgAABAjULCGzUPACaJ0CAAAECBAgQIECAAAECBAgQIECAAAECBBoXENho3EpOAgQIECBAgAABAgQIECBAgAABAgQIECBAoGYBgY2aB0DzBAgQIECAAAECBAgQIECAAAECBAgQIECAQOMCAhuNW8lJgAABAgQIECBAgAABAgQIECBAgAABAgQI1CwgsFHzAGieAAECBAgQIECAAAECBAgQIECAAAECBAgQaFxAYKNxKzkJECBAgAABAgQIECBAgAABAgQIECBAgACBmgUENmoeAM0TIECAAAECBAgQIECAAAECBAgQIECAAAECjQsIbDRuJScBAgQIECBAgAABAgQIECBAgAABAgQIECBQs4DARs0DoHkCBAgQIECAAAECBAgQIECAAAECBAgQIECgcQGBjcat5CRAgAABAgQIECBAgAABAgQIECBAgAABAgRqFphWc/ua34rA2rVrt/KtrwgQIECAAAECBAgQIECAAAECBAgQKC3gGV1pYfUTaF5g2sDAQNOlJlKm6UbGKNAN7W7evHnozOOXpl+cQxzeECBAgAABAgQIECBAgAABAgQIEKhVIJ7d1fGMso42A1q7rbncODfvPK2np6epUoHcbJmmGhgnc7e0O2PGjHEEHCZAgAABAgQIECBAgAABAgQIECBAoE6BeHbX6mejdT0X7e/vb/m5xtjWdb7d1m6nj6+lqOr8TThG24sWLUqrVq1KcWHNmjVrjBxlD0XUuY7gSre1a3zLXsdV7XVdV8a3GoGyr8a3rG9Ve13OdbXr/q1Gvuyr8S3rW9Vel3Nd7bp/q5Ev+2p8y/pWtdflXFe77t9q5Mu+Gt+yvlXtdTnX1W433r/x7E4iQKB+AYGN+sdgRA8WL16c4qevry/19vaO+K4VH7otMlnX+RrfVlzN9UX4ja/xLSFQ1++rbmvX/Vvi6h1dZ13XlfEdPRYljhjfEqqj66zLua523b+jr4ESR4xvCdXRddblXFe77t/R10CJI8a3hOroOutyHt0TRwgQmIqAAAECBAgQIECAAAECBAgQIECAAAECBAgQINApAgIbnTJS+kmAAAECBAgQIECAAAECBAgQIECAAAECBAgkgQ0XAQECBAgQIECAAAECBAgQIECAAAECBAgQINAxAgIbHTNUOkqAAAECBAgQIECAAAECBAgQIECAAAECBAgIbLgGCBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgY4RENjomKHSUQIECBAgQIAAAQIECBAgQIAAAQIECBAgQEBgwzVAgAABAgQIECBAgAABAgQIECBAgAABAgQIdIyAwEbHDJWOEiBAgAABAgQIECBAgAABAgQIECBAgAABAgIbrgECBAgQIECAAAECBAgQIECAAAECBAgQIECgYwQENjpmqHSUAAECBAgQIECAAAECBAgQIECAAAECBAgQENhwDRAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIdIyCw0TFDpaMECBAgQIAAAQIECBAgQIAAAQIECBAgQICAwIZrgAABAgQIECBAgAABAgQIECBAgAABAgQIEOgYAYGNjhkqHSVAgAABAgQIECBAgAABAgQIECBAgAABAgQENlwDBAgQIECAAAECBAgQIECAAAECBAgQIECAQMcICGx0zFDpKAECBAgQIECAAAECBAgQIECAAAECBAgQICCw4RogQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEOkZAYKNjhkpHCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAAYEN1wABAgQIECBAgAABAgQIECBAgAABAgQIECDQMQICGx0zVDpKgAABAgQIECBAgAABAgQIECBAgAABAgQICGy4BggQIECAAAECBAgQIECAAAECBAgQIECAAIGOERDY6Jih0lECBAgQIECAAAECBAgQIECAAAECBAgQIEBAYMM1QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECHSMgMBGxwyVjhIgQIAAAQIECBAgQIAAAQIECBAgQIAAAQICG64BAgQIECBAgAABAgQIECBAgAABAgQIECBAoGMEBDY6Zqh0lAABAgQIECBAgAABAgQIECBAgAABAgQIEJiyadOmQQwECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAgU4QmDI4ONhUYGNgYCD19PS0/Ny6rd2+vr7U29vLubBAXdeV8S08sH+t3vg+t52Nr/EtIeD3cwnV0XW6f0eblDhSl3Nd7bp/S1xFo+s0vqNNShypy7mudt2/Ja6i0XUa39EmJY7U5VxXu+7fElfR6DqN72iTEkfqcq6r3U6/fy1FVeIuUCcBAgQIECBAgAABAgQIECBAgAABAgQIECBQREBgowirSgkQIECAAAECBAgQIECAAAECBAgQIECAAIESAgIbJVTVSYAAAQIECBAgQIAAAQIECBAgQIAAAQIECBQRENgowqpSAgQIECBAgAABAgQIECBAgAABAgQIECBAoISAwEYJVXUSIECAAAECBAgQIECAAAECBAgQIECAAAECRQQENoqwqpQAAQIECBAgQIAAAQIECBAgQIAAAQIECBAoISCwUUJVnQQIECBAgAABAgQIECBAgAABAgQIECBAgEARAYGNIqwqJUCAAAECBAgQIECAAAECBAgQIECAAAECBEoICGyUUFUnAQIECBAgQIAAAQIECBAgQIAAAQIECBAgUERAYKMIq0oJECBAgAABAgQIECBAgAABAgQIECBAgACBEgICGyVU1UmAAAECBAgQIECAAAECBAgQIECAAAECBAgUERDYKMKqUgIECBAgQIAAAQIECBAgQIAAAQIECBAgQKCEgMBGCVV1EiBAgAABAgQIECBAgAABAgQIECBAgAABAkUEBDaKsKqUAAECBAgQIECAAAECBAgQIECAAAECBAgQKCEgsFFCVZ0ECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAEQGBjSKsKiVAgAABAgQIECBAgAABAgQIECBAgAABAgRKCAhslFBVJwECBAgQIECAAAECBAgQIECAAAECBAgQIFBEQGCjCKtKCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgRICAhslVNVJgAABAgQIECBAgAABAgQIECBAgAABAgQIFBEQ2CjCqlICBAgQIECAAAECBAgQIECAAAECBAgQIECghMC0EpWqkwABAgQIECBAgAABAgQIECBAgAABAgQIEGhvgX/+539Oe+yxR1q0aFFavHhxe3d2WO8ENoZheEuAAAECBAgQIECAAAECBAgQIECAAAECBLpFYNOmTemyyy7LpxsBjn/6p39Kvb29+bWdDQQ22nl09I0AAQIECBAgQIAAAQIECBAgQIAAAQIECLRAIIIcq1atyi2de+65Q8GNlStXtqD15pqwx0ZzXnITIECAAAECBAgQIECAAAECBAgQIECAAIHntEAV5IhAx5QpU9KSJUtSBDvaJQlstMtI6AcBAgQIECBAgAABAgQIECBAgAABAgQIEGhDgbVr1+bZHO0S5BDYaMOLRJcIECBAgAABAgQIECBAgAABAgQIECBAgEA7CgwPcsyZM6eWmRwCG+14ZegTAQIECBAgQIAAAQIECBAgQIAAAQIECBBoc4FqyaqYydHKIMeUwcHBwWZsBgYGUk9PTzNFJiXvihUr0owZMyalrmYq2bx5cy3t9vf3p1mzZjXT1UnJW9f5dlu7xndSLtdtVlLXdWV8tzk0k5LB+E4K4zYrqcu5rnbdv9u8JCYlg/GdFMZtVlKXc13tun+3eUlMSgbjOymM26ykLue62nX/bvOSmJQMxndSGLdZSV3OdbXr/t3mJTEpGYzvpDBus5K6nOtqt7p/L7vsshTBiclOe+yxR958/KSTTkrxvkqTFV+Y0t/f31Rgo+pAq1/reMjf6nPUHgECBAgQIECAAAECBAgQIECAAAECBAgQeC4J7L777un444/PP/F+MtK0ZmdfTFZEZTI6rw4CBAgQIECAAAECBAgQIECAAAECBAgQIECgfQWmTp2aV0V65JFHUgQ2mo1JjHVm08Y62I7HzjjjjFqWhKp7KlCrx6Ku8+22dqupXsa3rEBd15XxLTuuVe3Gt5Io+1qXc13tun/LXk9V7ca3kij7WpdzXe26f8teT1XtxreSKPtal3Nd7bp/y15PVe3Gt5Io+1qXc13tun/LXk//t717CZGrWOMAXqMhvulB3IjCiIJEVNSJRiXEjApqFETUuMhCg4IgbnzEBxFRN0GIgiRGNwGTjQsRFZSgQXDUjVHEV7LwFTMSnxHsQcVH1Lmc451mvHOnSE+f01Xd/Wto09PfOVV1fv86lwsf3T09unynJer9N5Vzqnmn79+6v4pq+fLlYWxsrBVe8cGJKh498xsbqT4pkmreiYmJMDIyUkXGbY2R6noHbV75trUt531wqn0l33lH1taJ8m2La94Hp3JONa/7d95bpa0T5dsW17wPTuWcal7377y3SlsnyrctrnkfnMo51bzu33lvlbZOlG9bXPM+OJVzqnndv/PeKm2dKN+2uOZ9cCrnVPNO378XXnhhGB8fn7fbzBPn+l2NmcdUdb0984mNmRfvNQECBAgQIECAAAECBAgQIECAAAECBAgQIJBOoGhkFM/iB8KLT2XM/JHwulelsVG3sPEJECBAgAABAgQIECBAgAABAgQIECBAgEAfCMxsZqxevTrZFWlsJKM3MQECBAgQIECAAAECBAgQIECAAAECBAgQyFugaGYUn8gofi8jZTNjppLGxkwNrwkQIECAAAECBAgQIECAAAECBAgQIECAwIAL5NjMmBmJxsZMDa8JECBAgAABAgQIECBAgAABAgQIECBAgMAACuTezJgZicbGTA2vCRAgQIAAAQIECBAgQIAAAQIECBAgQIDAgAgUzYzi66WmfwC8Vy5bY6NXkrJOAgQIECBAgAABAgQIECBAgAABAgQIECBQocBTTz1V4WjdG+qg7k1lJgIECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAZwIaG535OZsAAQIECBAgQIAAAQIECBAgQIAAAQIECBDoooDGRhexTUWAAAECBAgQIECAAAECBAgQIECAAAECBAh0JqCx0ZmfswkQIECAAAECBAgQIECAAAECBAgQIECAAIEuCmhsdBHbVAQIECBAgAABAgQIECBAgAABAgQIECBAgEBnAhobnfk5mwABAgQIECBAgAABAgQIECBAgAABAgQIEOiigMZGF7FNRYAAAQIECBAgQIAAAQIECBAgQIAAAQIECHQmoLHRmZ+zCRAgQIAAAQIECBAgQIAAAQIECBAgQIAAgS4KaGx0EdtUBAgQIECAAAECBAgQIECAAAECBAgQIECAQGcCGhud+TmbAAECBAgQIECAAAECBAgQIECAAAECBAgQ6KKAxkYXsU1FgAABAgQIECBAgAABAgQIECBAgAABAgQIdCagsdGZn7MJECBAgAABAgQIECBAgAABAgQIECBAgACBLgpobHQR21QECBAgQIAAAQIECBAgQIAAAQIECBAgQIBAZwIaG535OZsAAQIECBAgQIAAAQIECBAgQIAAAQIECBDoooDGRhexTUWAAAECBAgQIECAAAECBAgQIECAAAECBAh0JqCx0ZmfswkQIECAAAECBAgQIECAAAECBAgQIECAAIEuCmhsdBHbVAQIECBAgAABAgQIECBAgAABAgQIECBAgEBnAhobnfk5mwABAgQIECBAgAABAgQIECBAgAABAgQIEOiigMZGF7FNRYAAAQIECBAgQICWxrx2AAAZBklEQVQAAQIECBAgQIAAAQIECHQmMNRsNqc6G8LZdQg0m80wPDxcx9DGzEBAvhmEUOMS5FsjbgZDyzeDEGpcgnxrxM1gaPlmEEKNS5BvjbgZDC3fDEKocQnyrRE3g6Hlm0EINS5BvjXiZjC0fDMIocYl9Hq+CxqNRls8k5OTod1z2ppgjoMHbd5iY3GeYzNU+HaqfSXfCkOMDCXfCE6FpVTOqeZ1/1a4eSJDyTeCU2EplXOqed2/FW6eyFDyjeBUWErlnGpe92+FmycylHwjOBWWUjmnmtf9W+HmiQwl3whOhaVUzqnmdf9WuHkiQ8k3ghMp+SqqCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRAY2NCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRAY2NCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRAY2NCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRAY2NCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRAY2NCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRAY2NCI4SAQIECBAgQIAAAQIECBAgQIAAAQIECBAgkJeAxkZeeVgNAQIECBAgQIAAAQIECBAgQIAAAQIECBAgEBHQ2IjgKBEgQIAAAQIECBAgQIAAAQIECBAgQIAAAQJ5CWhs5JWH1RAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIRgaFmszkVqSslEmg2m2F4eDjR7KatW0C+dQunHV++af3rnl2+dQunHV++af3rnl2+dQunHV++af3rnl2+dQunHV++af3rnl2+dQunHV++af3rnl2+dQunHb/X813QaDTaEpycnAztntPWBHMcPGjzFhuL8xybocK3U+0r+VYYYmQo+UZwKiylck41r/u3ws0TGUq+EZwKS6mcU83r/q1w80SGkm8Ep8JSKudU87p/K9w8kaHkG8GpsJTKOdW87t8KN09kKPlGcCospXJONa/7t8LNExlKvhGcSMlXUUVwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAhobERwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAhobERwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAhobERwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAhobERwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAhobERwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAhobERwlAgQIECAAAECBAgQIECAAAECBAgQIECAAIG8BDQ28srDaggQIECAAAECBAgQIECAAAECBAgQIECAAIGIgMZGBEeJAAECBAgQIECAAAECBAgQIECAAAECBAgQyEtAYyOvPKyGAAECBAgQIECAAAECBAgQIECAAAECBAgQiAgM7dmzZypSVyJAgAABAgQIECBAgAABAgQIECBAgAABAgQIZCMwNDU11VZjY3JyMjQaja5fwKDNOzExEUZGRjjXLJBqX8m35mD/O7x8+9tZvvKtQ8D/PtehOntM9+9skzreSeWcal73bx27aPaY8p1tUsc7qZxTzev+rWMXzR5TvrNN6ngnlXOqed2/deyi2WPKd7ZJHe+kck41b6/fv76Kqo67wJgECBAgQIAAAQIDIbBjx47wzjvvDMS1ukgCBAgQIECAAAECBAjkIqCxkUsS1kGAAAECBAgQINA1gXXr1oWhoaF5P3/++efw2muvhfPOOy8sWbIkvPrqq11bu4kIECBAgAABAgQIECAw6AIaG4O+A1w/AQIECBAgQGBABS644IIwPj4edu/eHYpvZy2ev/32W0vj3nvvDUUD45tvvgmffvppeO+998LWrVtb9YULF7Ze7927t/XaCwIECBAgQIAAAQIECBCoV2BBvcMbnQABAgQIECBAgECeAmeffXZYvnz5nIsrPtFxxBFHlM/pgxYtWhRuuOGG8s+lS5eGbdu2hV27doVVq1ZNH+JfAgQIECBAgAABAgQIEKhZQGOjZmDDEyBAgAABAgQI5Clw0kkntb2wQw89NBxzzDGt81asWBGKpwcBAgQIECBAgAABAgQIdE9AY6N71mYiQIAAAQIECBDIRGDt2rXzXsm+ffvmfW6VJ3777bfhk08+CUceeWQYHR2tcmhjESBAgAABAgQIECBAIGsBv7GRdTwWR4AAAQIECBAgkKPAli1bwkUXXRTGxsbK5xtvvNFa5uuvv956v6jv3LkzbNq0KaxcubL8tEfxFVdnnnlm2L59e/j999/D5s2bw7Jly8Lhhx9e/pj5CSecEO66666y1hr0vy+K3wBZs2ZNOO6448Kxxx5bfpXW4sWLw/nnnx8++uij/z3c3wQIECBAgAABAgQIEOhLAY2NvozVRREgQIAAAQIECNQpsHr16vDss8+Gzz//PBSNjJmf4ih+t2Pjxo1hx44dZa34/Y233347nHrqqeGWW24Jp512Wvjggw/CZZddFs4444zwyiuvhIsvvjjcfffd4ZJLLgkTExPhkUceCevWrZt1Cddcc0149NFHw5VXXhm+//778Oeff4Zbb701vPXWW2WTo/gUhwcBAgQIECBAgAABAgT6XcBXUfV7wq6PAAECBAgQIECgFoGjjz46HHbYYf937NNPPz0cfPDBZW39+vXhuuuuax13//33h+KHy4tPWNxxxx3h5ptvbtWKF7fffnt47LHHwssvvxweeuihVu2ll14qf6z8+OOPD0888UT56Y6i+Pjjj5eNlWeeeSZs2LDh/zZEWoN4QYAAAQIECBAgQIAAgT4Q8ImNPgjRJRAgQIAAAQIECPSOwMKFC8OSJUvKBX/99dezFn7FFVeU73355Zf/qhVfWVU8rr766lZTY/qA4hMkxaNofngQIECAAAECBAgQIECg3wU0Nvo9YddHgAABAgQIECCQncBBB/3zf8NnfoXV9CIXLPjnQ9X79++ffqv899133y3/PfHEE//1fvHHUUcdVb73xRdfzKp5gwABAgQIECBAgAABAv0m4Kuo+i1R10OAAAECBAgQINAzAn///fcBr/WHH34ojy1+iPz555//13nNZrP8u/gxcg8CBAgQIECAAAECBAj0u4DGRr8n7PoIECBAgAABAgSyFWinsVH8UHjxWLRoURgdHZ11TVdddVWY/rTHrKI3CBAgQIAAAQIECBAg0EcCGht9FKZLIUCAAAECBAgQ6C2BdhoRxddN/fjjj+Haa68N119/fW9dqNUSIECAAAECBAgQIECgQgG/sVEhpqEIECBAgAABAgQItCNwyCGHHPDhIyMj5bFfffXVAZ/jQAIECBAgQIAAAQIECPSjgMZGP6bqmggQIECAAAECBHpCYGho6IDXee6555bHPv3002FqauqAz3MgAQIECBAgQIAAAQIE+k1AY6PfEnU9BAgQIECAAAECPSPQToPitttuC0UjZOfOnaF47UGAAAECBAgQIECAAIFBFdDYGNTkXTcBAgQIECBAgEBLoPjtijfffDM8+eSTrfd27NgRnnvuufDZZ5/N+oTETz/9FHbt2hV+/fXX8vjimL1795bHFe+Nj4+Hv/76q6zt3r077Nu3r3xd/Fj4nj17wnfffVf+XXytVPH39LHFcR9//HFZ279/f3j//ffL18V/ih8NX79+ffn3hg0bWn9v27YtFH+vXLmy/Ld1ghcECBAgQIAAAQIECBDoUwE/Ht6nwbosAgQIECBAgACBAxfYunVraDab5QkPPPBA68QPP/wwFM9Vq1aFk08+ufX+xo0bwx9//BFuuumm8r2imbF58+Zw+eWXl5+qKBob99xzT1mbnJwMmzZtCmvWrCmbFi+++GI466yzymdxwJYtW8Kll14aTjnllPK44r3pNbzwwgvhl19+CUuXLi3HuvPOO8PixYvDww8/HLZv3x7uu+++MDo6GpYtWxZuvPHGsGLFivI4/yFAgAABAgQIECBAgEA/C2hs9HO6ro0AAQIECBAgQOCABNr9aqe1a9dGxz3nnHNa9aKx0Wg0yr+LpkTxnOvx4IMPzlVqvT82NhaKpwcBAgQIECBAgAABAgQGVcBXUQ1q8q6bAAECBAgQIECAAAECBAgQIECAAAECBAj0oIDGRg+GZskECBAgQIAAAQIECBAgQIAAAQIECBAgQGBQBTQ2BjV5102AAAECBAgQIECAAAECBAgQIECAAAECBHpQQGOjB0OzZAIECBAgQIAAAQIECBAgQIAAAQIECBAgMKgCGhuDmrzrJkCAAAECBAgQIECAAAECBAgQIECAAAECPSigsdGDoVkyAQIECBAgQIAAAQIECBAgQIAAAQIECBAYVAGNjUFN3nUTIECAAAECBAgQIECAAAECBAgQIECAAIEeFNDY6MHQLJkAAQIECBAgQIAAAQIECBAgQIAAAQIECAyqwFCz2Zwa1IvP+bqbzWYYHh7OeYnW1oGAfDvA64FT5dsDIXWwRPl2gNcDp8q3B0LqYIny7QCvB06Vbw+E1MES5dsBXg+cKt8eCKmDJcq3A7weOFW+PRBSB0uUbwd4PXBqr+e7oNFotMU8OTkZ2j2nrQnmOHjQ5i02Fuc5NkOFb6faV/KtMMTIUPKN4FRYSuWcal73b4WbJzKUfCM4FZZSOaea1/1b4eaJDCXfCE6FpVTOqeZ1/1a4eSJDyTeCU2EplXOqed2/FW6eyFDyjeBUWErlnGpe92+FmycylHwjOJGSr6KK4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBAR0NiI4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBAR0NiI4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBAR0NiI4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBAR0NiI4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBAR0NiI4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBAR0NiI4CgRIECAAAECBAgQIECAAAECBAgQIECAAAECeQlobOSVh9UQIECAAAECBAgQIECAAAECBAgQIECAAAECEQGNjQiOEgECBAgQIECAAAECBAgQIECAAAECBAgQIJCXgMZGXnlYDQECBAgQIECAAAECBAgQIECAAAECBAgQIBARGGo2m1ORulIigWazGYaHhxPNbtq6BeRbt3Da8eWb1r/u2eVbt3Da8eWb1r/u2eVbt3Da8eWb1r/u2eVbt3Da8eWb1r/u2eVbt3Da8eWb1r/u2eVbt3Da8Xs93wWNRqMtwcnJydDuOW1NMMfBgzZvsbE4z7EZKnw71b6Sb4UhRoaSbwSnwlIq51Tzun8r3DyRoeQbwamwlMo51bzu3wo3T2Qo+UZwKiylck41r/u3ws0TGUq+EZwKS6mcU83r/q1w80SGkm8Ep8JSKudU87p/K9w8kaHkG8GJlHwVVQRHiQABAgQIECBAgAABAgQIECBAgAABAgQIEMhLQGMjrzyshgABAgQIECBAgAABAgQIECBAgAABAgQIEIgIaGxEcJQIECBAgAABAgQIECBAgAABAgQIECBAgACBvAQ0NvLKw2oIECBAgAABAgQIECBAgAABAgQIECBAgACBiIDGRgRHiQABAgQIECBAgAABAgQIECBAgAABAgQIEMhLQGMjrzyshgABAgQIECBAgAABAgQIECBAgAABAgQIEIgIaGxEcJQIECBAgAABAgQIECBAgAABAgQIECBAgACBvAQ0NvLKw2oIECBAgAABAgQIECBAgAABAgQIECBAgACBiIDGRgRHiQABAgQIECBAgAABAgQIECBAgAABAgQIEMhLQGMjrzyshgABAgQIECBAgAABAgQIECBAgAABAgQIEIgIaGxEcJQIECBAgAABAgQIECBAgAABAgQIECBAgACBvAQ0NvLKw2oIECBAgAABAgQIECBAgAABAgQIECBAgACBiIDGRgRHiQABAgQIECBAgAABAgQIECBAgAABAgQIEMhLQGMjrzyshgABAgQIECBAgAABAgQIECBAgAABAgQIEIgIaGxEcJQIECBAgAABAgQIECBAgAABAgQIECBAgACBvAQ0NvLKw2oIECBAgAABAgQIECBAgAABAgQIECBAgACBiIDGRgRHiQABAgQIECBAgAABAgQIECBAgAABAgQIEMhL4D9JKo/9kb6cvQAAAABJRU5ErkJggg==)

对比来看，

- 并发通常应用于 I/O 操作频繁的场景，比如你要从网站上下载多个文件，I/O 操作的时间可能会比 CPU 运行处理的时间长得多。
- 而并行则更多应用于 CPU heavy 的场景，比如 MapReduce 中的并行计算，为了加快运行速度，一般会用多台机器、多个处理器来完成。

### 7.2 并发编程之 Futures

#### 单线程与多线程性能比较

##### 单线程

```python
import requests
import time
 
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))
    
def download_all(sites):
    for site in sites:
        download_one(site)
 
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()
```

这种方式应该是最直接也最简单的：

- 先是遍历存储网站的列表；
- 然后对当前网站执行下载操作；
- 等到当前操作完成后，再对下一个网站进行同样的操作，一直到结束。

单线程的优点是简单明了，但是明显效率低下，因为上述程序的绝大多数时间，都浪费在了 I/O 等待上。程序每次对一个网站执行下载操作，都必须等到前一个网站下载完成后才能开始。如果放在实际生产环境中，我们需要下载的网站数量至少是以万为单位的，不难想象，这种方案根本行不通。

##### 多线程

```python
import concurrent.futures
import requests
import threading
import time
 
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))
 
 
def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)
 
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
 
if __name__ == '__main__':
    main()
```

创建了一个线程池，总共有 5 个线程可以分配使用。executer.map() 与前面所讲的 Python 内置的 map() 函数类似，表示对 sites 中的每一个元素，并发地调用函数 download_one()。

顺便提一下，在 download_one() 函数中，我们使用的 requests.get() 方法是线程安全的（thread-safe），因此在多线程的环境下，它也可以安全使用，并不会出现 race condition 的情况。

虽然线程的数量可以自己定义，但是线程数并不是越多越好，因为线程的创建、维护和删除也会有一定的开销。所以如果你设置的很大，反而可能会导致速度变慢。我们往往需要根据实际的需求做一些测试，来寻找最优的线程数量。

当然，我们也可以用并行的方式去提高程序运行效率。你只需要在 download_all() 函数中，做出下面的变化即可：

```python
with futures.ThreadPoolExecutor(workers) as executor
=>
with futures.ProcessPoolExecutor() as executor: 
```

在需要修改的这部分代码中，函数 ProcessPoolExecutor() 表示创建进程池，使用多个进程并行的执行程序。不过，这里我们通常省略参数 workers，因为**系统会自动返回 CPU 的数量作为可以调用的进程数**。

**并行的方式一般用在 CPU heavy 的场景中，因为对于 I/O heavy 的操作，多数时间都会用于等待，相比于多线程，使用多进程并不会提升效率。反而很多时候，因为 CPU 数量的限制，会导致其执行效率不如多线程版本。**

#### 到底什么是 Futures

Python 中的 Futures 模块，位于 concurrent.futures 和 asyncio 中，它们都表示带有延迟的操作。Futures 会将处于等待状态的操作包裹起来放到队列中，这些操作的状态随时可以查询，当然，它们的结果或是异常，也能够在操作完成后被获取。

通常来说，作为用户，我们不用考虑如何去创建 Futures，这些 Futures 底层都会帮我们处理好。我们要做的，实际上是去 schedule 这些 Futures 的执行。

比如，Futures 中的 Executor 类，当我们执行 executor.submit(func) 时，它便会安排里面的 func() 函数执行，并返回创建好的 future 实例，以便你之后查询调用。

这里再介绍一些常用的函数。

- Futures 中的方法 done()，表示相对应的操作是否完成——True 表示完成，False 表示没有完成。不过，要注意，done() 是 non-blocking 的，会立即返回结果。相对应的 add_done_callback(fn)，则表示 Futures 完成后，相对应的参数函数 fn，会被通知并执行调用。
- Futures 中还有一个重要的函数 result()，它表示当 future 完成后，返回其对应的结果或异常。而 as_completed(fs)，则是针对给定的 future 迭代器 fs，在其完成后，返回完成后的迭代器。

```python
import concurrent.futures
import requests
import time
 
def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))
 
def download_all(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
            
        for future in concurrent.futures.as_completed(to_do):
            future.result()
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    download_all(sites)
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
 
if __name__ == '__main__':
    main()
```

future 列表中每个 future 完成的顺序，和它在列表中的顺序并不一定完全一致。到底哪个先完成、哪个后完成，取决于系统的调度和每个 future 的执行时间。

##### 为什么多线程每次只能有一个线程执行？

同一时刻，Python 主程序只允许有一个线程执行，所以 Python 的并发，是通过多线程的切换完成的

Python 的解释器并不是线程安全的，为了解决由此带来的 race condition 等问题，Python 便引入了全局解释器锁，也就是同一时刻，只允许一个线程执行。当然，在执行 I/O 操作时，如果一个线程被 block 了，全局解释器锁便会被释放，从而让另一个线程能够继续执行。

```ad-summary
并发，通过线程和任务之间互相切换的方式实现，但同一时刻，只允许有一个线程或任务执行。
而并行，则是指多个进程完全同步同时的执行。
```

并发通常用于 I/O 操作频繁的场景，而并行则适用于 CPU heavy 的场景。

## 8. 并发编程 - Asyncio

> 多线程有诸多优点且应用广泛，但也存在一定的局限性：
>
> - 比如，多线程运行过程容易被打断，因此有可能出现 race condition 的情况；
> - 再如，线程切换本身存在一定的损耗，线程数不能无限增加，因此，如果你的 I/O 操作非常 heavy，多线程很有可能满足不了高效率、高质量的需求。
>
> 正是为了解决这些问题，Asyncio 应运而生。

### 8.1 什么是 Asyncio

#### Sync VS Async

Sync（同步）和 Async（异步）的概念。

- 所谓 Sync，是指操作一个接一个地执行，下一个操作必须等上一个操作完成后才能执行。
- 而 Async 是指不同操作间可以相互交替执行，如果其中的某个操作被 block 了，程序并不会等待，而是会找出可执行的操作继续执行。

举个简单的例子，你的老板让你做一份这个季度的报表，并且邮件发给他。

- 如果按照 Sync 的方式，你会先向软件输入这个季度的各项数据，接下来等待 5min，等报表明细生成后，再写邮件发给他。
- 但如果按照 Async 的方式，再你输完这个季度的各项数据后，便会开始写邮件。等报表明细生成后，你会暂停邮件，先去查看报表，确认后继续写邮件直到发送完毕。

### 8.2 Asyncio 工作原理

Asyncio 和其他 Python 程序一样，是单线程的，它只有一个主线程，但是可以进行多个不同的任务（task），这里的任务，就是特殊的 future 对象。这些不同的任务，被一个叫做 event loop 的对象所控制。你可以把这里的任务，类比成多线程版本里的多个线程。

假设任务只有两个状态：一是预备状态；二是等待状态。所谓的预备状态，是指任务目前空闲，但随时待命准备运行。而等待状态，是指任务已经运行，但正在等待外部的操作完成，比如 I/O 操作。

对于 Asyncio 来说，它的任务在运行时不会被外部的一些因素打断，因此 Asyncio 内的操作不会出现 race condition 的情况，这样你就不需要担心线程安全的问题了。

### 8.3 Asyncio 用法

```python
import asyncio
import aiohttp
import time
 
async def download_one(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            print('Read {} from {}'.format(resp.content_length, url))
 
async def download_all(sites):
    tasks = [asyncio.create_task(download_one(site)) for site in sites]
    await asyncio.gather(*tasks)
 
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    start_time = time.perf_counter()
    asyncio.run(download_all(sites))
    end_time = time.perf_counter()
    print('Download {} sites in {} seconds'.format(len(sites), end_time - start_time))
    
if __name__ == '__main__':
    main()
```

### 8.4 多线程还是 Asyncio

- 如果是 I/O bound，并且 I/O 操作很慢，需要很多任务 / 线程协同实现，那么使用 Asyncio 更合适。
- 如果是 I/O bound，但是 I/O 操作很快，只需要有限数量的任务 / 线程，那么使用多线程就可以了。
- 如果是 CPU bound，则需要使用多进程来提高程序运行效率。

```ad-summary
不同于多线程，Asyncio 是单线程的，但其内部 event loop 的机制，可以让它并发地运行多个不同的任务，并且比多线程享有更大的自主控制权。

Asyncio 中的任务，在运行过程中不会被打断，因此不会出现 race condition 的情况。尤其是在 I/O 操作 heavy 的场景下，Asyncio 比多线程的运行效率更高。因为 Asyncio 内部任务切换的损耗，远比线程切换的损耗要小；并且 Asyncio 可以开启的任务数量，也比多线程中的线程数量多得多。

但需要注意的是，很多情况下，使用 Asyncio 需要特定第三方库的支持，比如前面示例中的 aiohttp。而如果 I/O 操作很快，并不 heavy，那么运用多线程，也能很有效地解决问题。
```

## 9. GIL （全局解析器锁）

