## Basic Syntaxes
### Lines and Indentation  
Unlike Java, Python does not use braces (`{}`) to indicate blocks of code for class, function or flow control. Instead of braces, you will use line indentation, which is rigidly enforced.

与Java不同，Python不使用大括号（{}）来指示类、函数或流控制的代码块。您将使用严格强制执行的线缩进代替大括号。

For example, below is a valid piece of code:
```python
if True:
   print ("True")
else:
   print ("False")
```
However, the following code will not run:
```python
if True:
print ("True")
else:
print ("False")
```

### Quotation in Python
Python accepts single (`'`), double (`"`) and triple (`'''` or `"""`) quotes to denote strings, as long as the same type of quote starts and ends these strings.

Python接受单引号（'）、双引号（“”）和三引号（“”）来表示字符串，只要相同类型的引号开始和结束这些字符串。

```python
line_1 = 'hello'
line_2 = "welcome"
line_3 = """multiple
            lines"""
```

The triple quotes are used to span the string across multiple lines. 

### Comments in Python
A hash sign (`#`) (that is not inside a string) begins a comment. All characters after the # and up to the end of a line are part of the comment, and Python interpreter ignores them.

散列符号（#）（不在字符串中）开始注释。在#之后直到行尾的所有字符都是注释的一部分，Python解释器将忽略它们。

```python
# This is a comment
# This is a second comment
```

Python does not support multi-line comments like in Java. However, triple quotes are often considered as one, even though they are strings and not ignored by Python interpreter in the same way that a # comment is.
```python
"""
This is a multiple line comment
"""
```

## The Anatomy of Python Variables
### Assigning Values to Variables

Unlike Java where you have to declare the type for each variable to determine how much space should be reserved (for example, an `int` takes 4 bytes in Java), Python variables **do not need explicit** declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign = is used to assign values to variables.

For example, you can initialize the variable `j` with the value `"man"` as follows, without having to explicitly specify that j is a string:

```python
j = "man"
```
The operand to the left of the = operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. 

One thing to note is that the type of a variable **is not fixed**. In the following example, we assigned the variable x to 3 , which is an int type. We later assigned it to "sing" , which is a str type. 

=运算符左侧的操作数是变量的名称，=运算符右侧的操作数是存储在变量中的值。  

需要注意的一点是，变量的类型不是固定的。在下面的示例中，我们将变量x赋给3，这是一个int类型。后来我们把它分配给“sing”，这是一个str类型。
```python
x = 3
print(x)
x = "sing"
print(x)
```
### Object Types
Python has various standard object types that are used to define the operations possible on them. Again, as there are no type declarations in Python, the syntax of the expressions we use determine the type of objects. Based on the way we assign the variables, Python figures out what type each variable is and keeps tracks of that internally.

Python有各种标准对象类型，用于定义对它们可能执行的操作。同样，由于Python中没有类型声明，所以我们使用的表达式的语法决定了对象的类型。根据我们分配变量的方式，Python计算出每个变量的类型，并在内部跟踪该类型。

There are a lot of object types. However, in this class, we will just focus on these important ones:

- Numeric 数值型: Object types where you can do arithmetic operations on. 可以对其执行算术运算的对象类型。

  - Integer 整数: Positive or negative whole numbers (without a fractional part). Similar to int in Java.

  - Float 浮点: Any real number with a floating point representation. Similar to double in Java.

- Boolean 布尔值: True or False (***remember they are capitalized***). Similar to boolean in Java.

- String 字符串: A collection of one or more characters put in single, double or triple quotes. Similar to string in Java.

- None: A type indicating a null variable or an object.  Similar to `null` in Java. 指示空变量或对象的类型。类似于Java中的null。

- Container 容器 (we will discuss each of the following in detail in later slides):

  - Tuple 元组: An **immutable, ordered** collection of one or more data items, not necessarily of the same type, put in parentheses (). There is no built-in Java equivalence. 不可变有序

  - List 列表: A **mutable, ordered** collection of one or more data items, not necessarily of the same type, put in square brackets []. Similar to `ArrayList` in Java. 可变有序

  - Set 集合: A **mutable, unordered** collection of data type that has no duplicate elements. Similar to `HashSet` in Java. 可变无序

  - Dictionary: A **mutable, unordered** collection of data in a key:value pair form where each key is unique. Similar to `HashMap` in Java. 可变无序

```python
# Integer
a = 5

# Float
b = 2.0

# String
c = 'hello'
my_greeting = "hello"

# Boolean
e = True

# None
f = None

# Tuple
my_tuple = (1, 3, "Yes")

# List
my_list = ["a", "b", "c"]

# Set
my_set = set([3.1, 4.7, -1.5])

# Dictionary
my_dict = {"Joe": 15, "Maria": 22}

#  Python不允许直接拼接字符串和整数,
#  str()的作用是将其他数据类型转换为字符串类型
print("a = " + str(a))
print("b = " + str(b))
print("c = " + str(c))
print("my_greeting = " + str(my_greeting))
print("e = " + str(e))
print("f = " + str(f))
```
在 Python 中，`变量名:类型 = 值` 是一种类型注解（Type Hint）的语法。它不强制类型检查，但提供了以下用途和好处：
1. 代码可读性和可维护性  
类型注解明确说明了变量的预期类型，让代码更易读和理解
1. 静态类型检查  
工具如 mypy 或 IDE（如 PyCharm、VS Code）可以根据类型注解提供静态类型检查，帮助发现潜在的错误
1. 智能提示和补全  
许多 IDE 会根据类型注解提供更好的代码提示和补全。
1. 与静态类型的工具和框架集成  
类型注解与某些框架（如 FastAPI）或工具深度集成，可以更高效地自动生成文档或执行验证。
1. 增强开发规范  
通过显式声明类型，可以帮助开发者更清楚地定义变量的用途，从而减少类型混淆和意外错误
```python
# Integer
a:int = 5

# Float
b:float = 2.0

# String
c:str = 'hello'
my_greeting:str= "hello"

# Boolean
e:bool = True

# None
f:None = None
```
## Operators
### Arithmetic Operators
```python
# Arithmetic Operators

print(5 + 4)
print(2 * 3)
print(9.0 - 4.5)
print(6 % 4)
print(5 // 2) #Integer division = 2
print(5.0 // 2) #Integer division = 2.0
print(5 / 2) #Float division = 2.5
print(2 ** 3) #Exponentiation = 2^3 = 8
```
### Assignment Operators
```python
# Assignment Operators
# x++ is invalid statement in Python
x:int = 5
print(str(x))
x += 1
print(str(x))
```
### Comparison Operators
```python
# Comparison Operators

x = 5
y = 2
# 使用 str.format() 方法
# 将布尔表达式的值插入到 {} 的位置
print("x == y = {}".format(x == y))
print("x != y = {}".format(x != y))
print("x < y = {}".format(x < y))
print("x <= y = {}".format(x <= y))
print("x > y = {}".format(x > y))
print("x >= y = {}".format(x >= y))
```
### Logical Operators
```python
# Logical Operators

x = True
y = False

print("x and y = {}".format(x and y))
print("x or y = {}".format(x or y))
print("not x = {}".format(not x))
```
## Strings
``` python
# String concatenation

x = "Hello, "
y = "world"
print(x + y)
```
```python
y = 3

# Syntax error: print("I have " + y + " cats")

# Method 1: Cast to string before print
print("I have " + str(y) + " cats")

# Method 2: Use format()
print("My name is {}. I'm {} and I have ${}.".format("Bob", 27, 3.99))

# Method 3 : f-strings
print(f"I have {y} cats and {y + 1} dogs")
```
### Reprise
```python
x = "CSE 312"

first = x[0]
length = len(x)
last = x[-1]
a = x[::2]

print("first = {}".format(first)) # first = C
print("length = {}".format(length)) # length = 7
print("last = {}".format(last)) # last = 2
print("a = {}".format(a)) # a = CE32    [Slicing ]
```

## If/Else Statements

There are no {} in Python (used like they are in Java)!  
**Indentation** is necessary and must be consistent 
```python
x:int = int(input("Enter a number: "))

if x < 0:
    print("x is a negative number")
elif x == 0:
    print("x is zero")
else:
    print("x is a positive number")
```
## Range
基本语法： 
range(start, stop[, step])  
- start（可选）：序列的起始值，默认为 0。
- stop（必填）：序列的结束值（不包括 stop）。
- step（可选）：步长，默认为 1。可以是负数来生成递减序列。

```python
range1 = range(1, 11, 2)
range2 = range(1, 5)     # default step is 1
range3 = range(6)        # default start is 0

print("Range 1")    # 1 3 5 7 9
for i in range1:
  print(i)

print("Range 2")    # 1 2 3 4
for i in range2:
  print(i)

print("Range 3")    # 0 1 2 3 4 5
for i in range3:
  print(i)          
```
## Loops
### For Loops
```python
# For Loop
for i in range(0, 5):
    print(i)
```
### While Loops
```python
# While Loop
i:int = 5
while i > 0:
    print(i)
    i -= 1
```
## Lists
###  Basics
列表：一个**可变的、有序的**一个或多个数据项的集合，不一定是同一类型的，放在方括号[]中。类似于Java中的“ArrayList”。可变有序
```python
colors = ['red', 'green', 'blue', 'pink', 'purple']

first = colors[0]
second = colors[1]
last = colors[-1]
second_last = colors[-2]
length = len(colors)

print("first = {}".format(first)) # 'red'
print("second = {}".format(second)) # 'green'
print("last = {}".format(last)) # 'purple'
print("second_last = {}".format(second_last)) # 'pik'
print("length = {}".format(length)) # 5
```
### Manipulation

list.append(data)  
list.insert(int, data)  
list.remove(data)  
del list[-n]  
list[n] = data  
list = list + [data1, data2, + ... ]

```python
colors = ['red', 'green', 'blue', 'pink', 'purple']
print("colors = {}".format(colors))
#colors = ['red', 'green', 'blue', 'pink', 'purple']

# name.append(data)
colors.append('orange')
print("\ncolors.append('orange'):\ncolors = {}".format(colors))
# colors = ['red', 'green', 'blue', 'pink', 'purple', 'orange']

# name.insert(int, data)
colors.insert(1, 'yellow')
print("\ncolors.insert(1, 'yellow'):\ncolors = {}".format(colors))
# colors = ['red', 'yellow', 'green', 'blue', 'pink', 'purple', 'orange']

# name.remove(data)
colors.remove('red')
print("\ncolors.remove('red'):\ncolors = {}".format(colors))
# colors = ['yellow', 'green', 'blue', 'pink', 'purple', 'orange']

# del name[-n]
#删除列表 colors 中倒数第n个元素
del colors[-1]
print("\ndel colors[-1]:\ncolors = {}".format(colors))
# colors = ['yellow', 'green', 'blue', 'pink', 'purple']

# name[n] = newdata
# change the data in List
colors[2] = 'indigo'
print("\ncolors[2] = 'indigo':\ncolors = {}".format(colors))
# colors = ['yellow', 'green', 'indigo', 'pink', 'purple']

# name = name + [newdata, newdata2, ...]
# Add data at the end of the List
colors = colors + ['orange', 'yellow']
print("\ncolors = colors + ['orange', 'yellow']:\ncolors = {}".format(colors))
colors = ['yellow', 'green', 'indigo', 'pink', 'purple', 'orange', 'yellow']
```
## Slicing
切片语法：`colors[start:end:step]`  
only one `:` means step is 1

```python
colors = ['red', 'green', 'blue', 'pink', 'purple']

print("colors[1:3] = {}".format(colors[1:3]))
# from colors[1] to colors [3]
# colors[1:3] = ['green', 'blue']

print("colors[1:] = {}".format(colors[1:]))
# from colors[1] to the end
# colors[1:] = ['green', 'blue', 'pink', 'purple']

print("colors[:3] = {}".format(colors[:3]))
# from colors[0] (the start) to colors [3]
# colors[:3] = ['red', 'green', 'blue']

print("colors[-2:] = {}".format(colors[-2:]))
# from the second last data to the end
# colors[-2:] = ['pink', 'purple']

print("colors[:4:2] = {}".format(colors[:4:2]))
#start=0（默认起始位置为索引 0）。
#end=4（不包括索引 4，范围是 [0, 4)）。
#step=2（步长为 2，表示跳过一个元素选择）。
#colors[:4:2] = ['red', 'blue']
```
### Generating Lists
这是一种更简洁、更具 Python 风格的方式来实现相同的功能。
```python
# 生成一个包含从 1 到 10 的平方数的列表

# Method1 for 循环
squares = []
for x in range(1, 11):
    square:int = x ** 2  # 计算 x 的平方
    squares.append(square)  # 将平方值添加到列表中
print(squares)


# Method2 使用列表推导式(list comprehension):
squares = [x ** 2 for x in range(1, 11)]
print(squares)
```
## Tuples
一个或多个数据项的**不可变、有序**集合，不一定是同一类型，放在括号（）中。没有内置的Java等价性。不可变有序

```python
# Immutable ordered list of values

t = (2, 4, 6)

# Index the same way as lists
print("t[0] = {}".format(t[0])) # t[0] = 2
print("t[1] = {}".format(t[1])) # t[1] = 4
print("t[2] = {}".format(t[2])) # t[2] = 6

# A different way to get the values of tuples
a, b, c = (2, 4, 6)
print("a = {}".format(a)) # a = 2
print("b = {}".format(b)) # b = 4
print("c = {}".format(c)) # c = 6
```
## Imports

```python
import math
x = math.sqrt(9)

print("x = {}".format(x))
```
Alias for module: 
```python
import math as m
x = m.sqrt(9)

print("x = {}".format(x))
```
Sepecific function to import:
```python
from math import sqrt
x = sqrt(9)

print("x = {}".format(x))
```

## Functions

def functionName(parameterName: parameterType) -> returnType:  

```py
# A Basic Function

def multiplier(x:int, y:int) -> int:
    return x * y

print(multiplier(4, 5)) # 20
print(multiplier(3, "hi")) # Typing not enforced! hihihi
```
### Keyword Arguments

Using keyword arguments allows you to specify which parameter an argument applies to-order doesn't
matter here!
```py
# Keyword Arguments

def divide(x:int, y:int) -> float:
  return y / x

print(divide(x = 9, y = 3)) # 0.3333333333333333
print(divide(y = 3, x = 9)) # 0.3333333333333333
```
### Default Parameters
**All the default arguments must come at the end of the function!**  

不声明就使用已有的Parameter
```py
# Default Parameters

def greet(name:str, greeting:str = "Hello"):
  print(greeting + " " + name)

greet("Bob") # Hello Bob
greet(name="Bob") # Hello Bob
greet(name="Bob", greeting="Good afternoon") # Good afternoon Bob
greet(greeting="Yo", name="Bob") # Yo Bob
```
### Passing Functions

```py
# Passing Functions

from typing import Callable

#类型提示 Callable 表示 text_func 期望是一个函数对象.
#Python 中的 Callable 用来指示该参数是一个可调用的对象
def add_lines(text_func:Callable):
  print('---------------')
  print(text_func())
  print('---------------')

def fact():
  return "the sky is blue"

add_lines(fact)
```
### Helper Functions
Inner function available only in scope of outer function  
内部函数仅在外部函数范围内可用
```py
# Helper Functions

import math as m

def getArea(radius):
  def square(r):
    return r**2
  return m.pi * square(radius)

print(getArea(1)) # 3.141592653589793
```
### Multiple Return Values
Returns multiple values as an implicit tuple
```py
# Multiple Return Values

def func():
    return 'hello', 5

x,y = func()
for i in range(y):
    print(x)
```
### Main in Python
```py
# Main Method

def main():
    print("Hello")

# calls main method when this file is run with `python file_name.py` from the terminal
if __name__ == "__main__":
    main()
```
## Sets
没有重复元素的**可变、无序**数据类型集合。类似于Java中的HashSet。  

set.add(data)  
set.remove(data)
### Collections of Unique Elements
```py
x = set()
x.add(1) # {1}
print("x.add(1): x = {}".format(x))
x.add(3) # {1, 3}
print("x.add(3): x = {}".format(x))

# Alternate notation
y = {1, 3, 3} # {1, 3} - unique elements only
print("y = {{1, 3, 3}} means y = {}".format(y))

print("1 in x = {}".format(1 in x)) # True
print("1 not in x = {}".format(1 not in x)) # False
print("len(x) = {}".format(len(x)))
x.remove(1) # len(x) = 2
print("x.remove(1): x = {}".format(x)) # {3}
```

## Dictionaries
一个**可变、无序**的数据集合，以键：值对的形式存在，其中每个键都是唯一的。类似于Java中的HashMap。


```py
x = {'Grace': 'H', 'Margaret':'Hamilton'}
print("x = {}".format(x))
#x = {'Grace': 'H', 'Margaret': 'Hamilton'}

x1 = x['Grace'] # Returns value associated with key, i.e. ‘H’
print("\nx['Grace'] = {}".format(x1))
# x['Grace'] = H

x['Grace'] = 'Hopper' # Reassigns value associated with key
print("\nx = {}".format(x))
#x = {'Grace': 'Hopper', 'Margaret': 'Hamilton'}

print(x.keys())
# dict_keys(['Grace', 'Margaret'])

if 'Grace' in x.keys(): # Returns true if in keyset
  print('yup')

print('')

# Iterate through every key first_n in dictionary x
for first_n in x:
  print(first_n + " " + x[first_n])
# Grace Hopper
# Margaret Hamilton
```
## Classes
Constructor defined with special `__init__()` function  

`self` is like `this` in Java, but must be explicitly passed as the first parameter to every function

```py
class Line:
  '''
  This class represents straight lines in slope-intercept form
  ax + b
  '''

  def __init__(self, a, b):
    # Constructor
    self.a = a
    self.b = b
  def get_slope(self):
    return self.a
  def set_intercept(self, b):
    self.b = b


my_line = Line(5, 7)
print("my_line.a = {}".format(my_line.a))
# my_line.a = 5
print("my_line.b = {}".format(my_line.b))
# my_line.b = 7

print("")

my_line.get_slope()
print("my_line.get_slope() = {}".format(my_line.get_slope()))
# my_line.get_slope() = 5

print("")

my_line.set_intercept(2)
print("my_line.a = {}".format(my_line.a))
# my_line.a = 5
print("my_line.b = {}".format(my_line.b))
# my_line.b = 2
```
## Creating Arrays in NumPy
```py
# array

import numpy as np

# Convert from list of lists to numpy array! Basically a cast.
c = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(c)
#[[1 2 3 4]
# [5 6 7 8]]
```
```py
# zeros

import numpy as np

# Creates a 3x4 matrix of 0's
a = np.zeros((3, 4))
print(a)
#[[0. 0. 0. 0.]
# [0. 0. 0. 0.]
# [0. 0. 0. 0.]]
```
```py
# ones

import numpy as np

# Creates a 2x5x3 matrix (tensor) of 1's
b = np.ones((2, 4, 3))
print(b)
#[[[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]]
```
```py
# arange

import numpy as np

# Works exactly like range() but returns a np array instead of a range object
# 3 parameters (start, end=length of list, step=1), where end/step are optional
# and have defaults
d = np.arange(1, 10, 3)
print(d)
# [1 4 7]
```
### Practice1 - Creating Numpy Arrays
```py
import numpy as np

def task1():
    # TODO: Generate and return the following array: [3, 2, 5, 6]
    return np.array([3, 2, 5, 6])
    

def task2():
    # TODO: Generate and return an array of the cubes of every integer 
    # from 3 to 9 (inclusive).
    # HINT: remember we can easily generate lists using list comprehension
    cubes = [x ** 3 for x in range(3,10)]
    return np.array(cubes)
    

def task3():
    # TODO: Generate and return an array of every 3rd number 
    # from 10 to 20 (inclusive)
    return np.array(range(10, 21, 3))
    

def main():
    print(task1())
    print(task2())
    print(task3())

if __name__ == "__main__":
    main()
```
### Reshape

```py
# Reshape

import numpy as np

e = np.arange(1, 9)
print(e)

print("")
f = e.reshape((2, 4))
print(f)

print("")
g = f.reshape((4, 2))
print(g)

print("")
f = g.reshape((8, 1))
print(f)
```
OUTPUT:
```
[1 2 3 4 5 6 7 8]

[[1 2 3 4]
 [5 6 7 8]]

[[1 2]
 [3 4]
 [5 6]
 [7 8]]

[[1]
 [2]
 [3]
 [4]
 [5]
 [6]
 [7]
 [8]]
```
### Arithmetic with Lists vs NumPy Arrays
```PY
import numpy as np

arr = np.array([1, 2, 3, 4])
li = [1, 2, 3, 4]

print(arr + 5) # [6 7 8 9]
# Error: print(li + 5)

print(arr + arr) # [2 4 6 8]
print(li + li) # [1, 2, 3, 4, 1, 2, 3, 4]

print(arr ** 3)
# Error: li ** 3

print(arr * 3) # [ 3  6  9 12]
print(li * 3) # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]

print(arr * arr) # [ 1  4  9 16]
# Error: li * li
```
### Practice2 Advanced Numpy
```py
import numpy as np

#[[3 3 3 3]
# [3 3 3 3]
# [3 3 3 3]]
def task1():
    return np.zeros((3,4), dtype=int) + 3
    
#[[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]
def task2():
    return np.arange(1, 13).reshape((3, 4))
    
#[[7 5 3 1]
# [7 5 3 1]
# [7 5 3 1]
# [7 5 3 1]
# [7 5 3 1]]
def task3():
    return np.array([7,5,3,1]*5).reshape((5,4))
    

def main():
    print(task1())
    print(task2())
    print(task3())

if __name__ == "__main__":
    main()
```
### Indexing with Arrays
```py
import numpy as np

x = np.arange(1, 13).reshape((3, 4))
print(x)
print(x[1, -1])
print(x[:1, 2:])
print(x[:, 1:3])
```
output:
```
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

8

[[3 4]]

[[ 2  3]
 [ 6  7]
 [10 11]]
```
### Aggregators
```py
import numpy as np

# 创建一个 3x4 的二维数组
arr = np.array([[1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12]])

# 打印数组
print(arr)
#[[ 1  2  3  4]
# [ 5  6  7  8]
# [ 9 10 11 12]]

# 计算数组所有元素的总和
print(np.sum(arr))
#78

# 计算数组按列(axis=0)的总和
print(np.sum(arr, axis=0))
#[15 18 21 24]

# 计算数组按行(axis=1)的总和
print(np.sum(arr, axis=1))
# [10 26 42]
```
```py
import numpy as np

# 创建一个 3x4 的二维数组
arr = np.array([[1, 3, 5, 7], 
                [2, 4, 6, 0], 
                [8, 4, 6, 5]])

# 打印数组
print(arr)
#[[1 3 5 7]
# [2 4 6 0]
# [8 4 6 5]]

# 计算数组所有元素的均值
print(np.mean(arr))
#4.25


# 计算数组按列(axis=0)的最小值
print(np.min(arr, axis=0))
#[1 3 5 0]

# 计算数组按行(axis=1)的最大值
print(np.max(arr, axis=1))
#[7 6 8]

# 找到数组按行(axis=1)的最大值的索引
print(np.argmax(arr, axis=1))
#[3 2 0]
```
## Matplotlib
`matplotlib.pyplot` 是 Python 中用于绘制图表的库，通常用于科学计算和数据分析中的可视化工作。它提供了一系列用于绘制各种类型图形（如折线图、散点图、柱状图等）的函数，类似于 MATLAB 中的绘图工具，因此也被称为 `pyplot`。

`matplotlib` 是一个强大的可视化工具，而 `pyplot` 是它的一个模块，提供了一些简单的接口来创建和显示图表。最常用的接口是 `pyplot` 中的 `plot()`、`scatter()`、`hist()` 等方法。
### 创建简单的折线图
```py
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建图形
plt.plot(x, y)

# 添加标题和标签
plt.title('Simple Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
```
### 创建散点图
```py
import matplotlib.pyplot as plt

# 数据
x = [1, 2, 3, 4, 5]
y = [1, 4, 9, 16, 25]

# 创建散点图
plt.scatter(x, y)

# 添加标题和标签
plt.title('Scatter Plot')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')

# 显示图形
plt.show()
```
### 柱状图
```py
import matplotlib.pyplot as plt

# 数据
categories = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]

# 创建柱状图
plt.bar(categories, values)

# 添加标题和标签
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# 显示图形
plt.show()
```
### 直方图
```py
import matplotlib.pyplot as plt
import numpy as np

# 数据
data = np.random.randn(1000)

# 创建直方图
plt.hist(data, bins=30)

# 添加标题和标签
plt.title('Histogram')
plt.xlabel('Value')
plt.ylabel('Frequency')

# 显示图形
plt.show()
```
### 子图
有时你可能希望在同一个窗口中显示多个图形。这时可以使用 `plt.subplot()` 来创建子图。
```py
import matplotlib.pyplot as plt

# 创建一个2x2的图形网格
plt.subplot(2, 2, 1)  # 第一子图
plt.plot([1, 2, 3], [4, 5, 6])

plt.subplot(2, 2, 2)  # 第二子图
plt.scatter([1, 2, 3], [7, 8, 9])

plt.subplot(2, 2, 3)  # 第三子图
plt.bar([1, 2, 3], [10, 20, 30])

plt.subplot(2, 2, 4)  # 第四子图
plt.hist([1, 2, 3, 4, 5, 6, 7], bins=3)

# 显示所有子图
```