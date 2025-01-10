## 1. 标题
# markdown file
### 三级标题

## 2. 段落和换行
段落之间需要空行分隔。
或者直接换行后再空一行  
a

b

a  
b

## 3. 字体样式
加粗：**加粗** 或 __加粗__  
斜体：*斜体* 或 _斜体_  
加粗斜体：***加粗斜体***  
删除线：~~删除线~~  


## 4. 列表 
无序列表  
使用 -、* 或 + 表示：  

Why Python?
- powerful environment for scientific computing 
  - statistical modeling
  - data science
  - machine learning
* xxx
+ xxx

有序列表  
使用数字和 . 表示

1. 项目1
2. 项目2
   1. 子项目
   2. 子项目
3. 项目3

## 5.链接和图片
[Google](https://www.google.com)
![示例图片](./CN.jpg)

## 6. 引用
使用 > 表示  

> 这是一个引用。
>> 嵌套引用。

## 7. 代码
行内代码:  
使用反引号 `：

这是 `行内代码` 示例。  
这是 `python --version` 示例。

代码块:  
使用三个反引号,或指定语言：
``` Java
    @SuppressWarnings("unchecked")
    public ArrayQueue(){
        capacity = 10;
        queue = (T[]) new Object[capacity];
        size = 0;
        front = -1;
        back = 0;
    }
```


```python
print("Hello, World!")
```
## 8. 表格
使用 `|` 和 `-` 创建表格：

| 标题1 | 标题2 | 标题3 |
|-------|-------|-------|
| 数据1 | 数据2 | 数据3 |
| 数据4 | 数据5 | 数据6 |

## 9. 分隔线
使用三个或更多的 -、* 或 _:  
A 

---
B  
***
C
___

## 10. 任务列表
使用 - [ ] 表示未完成，- [x] 表示已完成：


- [ ] 任务1
- [x] 任务2

## 11. 注释
Markdown 本身没有注释语法，可以通过 HTML 的 <!-- 注释内容 --> 添加注释：