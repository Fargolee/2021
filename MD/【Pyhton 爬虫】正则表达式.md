<!--
 * @Author: Lee
 * @Descripttion: RTMart
 * @Date: 2022-03-04 18:24:41
-->
 [【Pyhton 爬虫】正则表达式_Riding the snail chase missiles ~-CSDN博客](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec '文章目录1、正则表达式基础2、正则表达式的基本符号2.1 点号 `“.”`2.2 星号 `“*”`2.3 问号 `“?”`2.4 反斜杠 `“\”`2.5 数字 `“\d”`2.6 小括号 `“()”`3、Python中使用正则表达式3.1 findall3.2 serach3.3 “.* ” 和 “.*?” 的区别4、正则表达式提取技巧4.1 不需使用 compile4.2 先抓大再抓小4.3 括号内和括号外在爬虫的开发中，需要把有用的信息从一大段文本中提取出来，正则表达式是提取信息的方法之一。..')
### 文章目录

- [1、正则表达式基础](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#1_8)
- [2、正则表达式的基本符号](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#2_18)
- - [2.1 点号 `“.”`](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#21___19)
    - [2.2 星号 `“*”`](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#22___22)
    - [2.3 问号 `“?”`](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#23___25)
    - [2.4 反斜杠 `“\”`](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#24___28)
    - [2.5 数字 `“\d”`](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#25__d_33)
    - [2.6 小括号 `“()”`](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#26___37)
- [3、Python中使用正则表达式](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#3Python_42)
- - [3.1 findall](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#31_findall_50)
    - [3.2 serach](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#32_serach_114)
    - [3.3 “.\* ” 和 “.\*?” 的区别](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#33______132)
- [4、正则表达式提取技巧](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#4_150)
- - [4.1 不需使用 compile](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#41__compile_151)
    - [4.2 先抓大再抓小](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#42__173)
    - [4.3 括号内和括号外](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#43__194)





* * *


> **在爬虫的开发中，需要把有用的信息从一大段文本中提取出来，`正则表达式`是提取信息的方法之一。**


* * *

# 1、[正则表达式](https://so.csdn.net/so/search?q=%E6%AD%A3%E5%88%99%E8%A1%A8%E8%BE%BE%E5%BC%8F&amp;spm=1001.2101.3001.7020)基础

**正则表达式（`Regular Expression`）是一段字符串，它可以表示一段有规律的信息。Python自带一个正则表达式模块 - `re`，通过这个模块可以查找、提取、替换一段有规律的信息。在程序开发中，要让计算机程序从一大段文本中找到需要的内容，就可以使用正则表达式来实现。**

**使用正则表达式有如下步骤：**
**（1）`寻找规律`**
**（2）`使用正则符号表示规律`**
**（3）`提取信息`**

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

# 2、正则表达式的基本符号

## 2.1 点号 `“.”`

**一个点号可以代替除了换行符以外的任何一个字符，包括但不限于英文字母、数字、汉字、英文标点符号和中文标点符号。**

* * *

## 2.2 星号 `“*”`

**一个星号可以表示它前面的一个子表达式（普通字符、另一个或几个正则表达式符号）0次到无限次。**

* * *

## 2.3 问号 `“?”`

**一个问号可以表示它前面的子表达式0次或者1次。注意，这里的问号是英文问号。**

* * *

## 2.4 [反斜杠](https://so.csdn.net/so/search?q=%E5%8F%8D%E6%96%9C%E6%9D%A0&amp;spm=1001.2101.3001.7020) `“\”`

**反斜杠在正则表达式里面不能单独使用，甚至在整个 Python 里都不能单独使用。反斜杠需要和其他的字符配合使用来把特殊符号变成普通符号，把普通符号变成特殊符号：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/1dad1275a8f94d199629b5732078e01e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

* * *

## 2.5 数字 `“\d”`

**正则表达式里面使用 “\d” 来表示一位数字。为什么要用字母d呢？因为d是英文“digital（数字）”的首字母。强调一下，“\d”虽然是由反斜杠和字母d构成的，但是要把“\d”看成一个正则表达式符号整体。**

* * *

## 2.6 小括号 `“()”`

**小括号可以把括号里面的内容提取出来。**

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

# 3、[Python](https://so.csdn.net/so/search?q=Python&amp;spm=1001.2101.3001.7020)中使用正则表达式

**Python 已经自带了一个功能非常强大的正则表达式模块。使用这个模块可以非常方便地通过正则表达式来从一大段文字中提取有规律的信息。Python的正则表达式模块名字为“re”，也就是“regularexpression”的首字母缩写。在Python中需要首先导入这个模块再进行使用。导入的语句为：**


```python
import re # pycharm 如果报错 Alt+Enter 自动导入即可
1
```

* * *

**下面我们来介绍一下常用的API：**

## 3.1 findall

**Python的正则表达式模块包含一个findall方法，它能够以列表的形式返回所有满足要求的字符串。**


```python
def findall(pattern, string, flags=0):
    """Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""
    return _compile(pattern, flags).findall(string)
123456789
```

**`pattern`表示正则表达式，`string`表示原来的字符串，`flags`表示一些特殊功能的标志。**
**`findall` 的结果是一个列表，包含了所有的匹配到的结果。如果没有匹配到结果，就会返回空列表：**


```python
content = '我的电脑密码是：123456，我的手机密码是：888888，我的家门密码是：000000，勿忘！'

pwd_list = re.findall('是：(.*?)，', content)
machine_list = re.findall('我的(.*?)密码是：', content)
name_list = re.findall('名字是(.*?),', content)
print('所有密码为：{}'.format(pwd_list))
print('所属为：{}'.format(machine_list))
print('用户姓名为：{}'.format(name_list))
12345678
```

**结果中很明显没有匹配到结果的为空 List 。这里还有一个变化：在匹配密码的时候，如左图会少一个。原因就出在匹配上面，我的匹配规则为：`'是：(.*?)，'`，必须严格满足这个格式的文本的中间密码部分才能被提取出来，重点就是后面的 `，` ，如右图加上了 `，勿忘！` 就使得前面的文本满足匹配规则，从而进行提取：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/23b9dfdeacc142dca3ceaa39366d9c1a.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
**当需要提取某些内容的时候，使用小括号将这些内容括起来，这样才不会得到不相干的信息。如果`包含多个` `“(.*?)”` 如下图所示，`返回的仍然是一个列表，但是列表里面的元素变为了元组`，元组里面的第1个元素是账号，第2个元素为密码：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/218daf8a736943adbcb5d6626e6802e5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
**函数原型中有一个`flags`参数。这个参数是可以省略的；当不省略的时候，具有一些辅助功能，例如`忽略大小写`、`忽略换行符`等。这里以忽略换行符为例来进行说明：**
![在这里插入图片描述](https://img-blog.csdnimg.cn/78954ada6f0d41fd95d83cd84207a5c7.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_18,color_FFFFFF,t_70,g_se,x_16#pic_center)
**常用的参数：**


```handlebars
re.I
    IGNORECASE
    忽略字母大小写

re.L
    LOCALE
    影响 “w, “W, “b, 和 “B，这取决于当前的本地化设置。

re.M
    MULTILINE
    使用本标志后，‘^’和‘$’匹配行首和行尾时，会增加换行符之前和之后的位置。

re.S
    DOTALL
    使 “.” 特殊字符完全匹配任何字符，包括换行；没有这个标志， “.” 匹配除了换行符外的任何字符。

re.X
    VERBOSE
    当该标志被指定时，在 RE 字符串中的空白符被忽略，除非该空白符在字符类中或在反斜杠之后。
    它也可以允许你将注释写入 RE，这些注释会被引擎忽略；
    注释用 “#”号 来标识，不过该符号不能在字符串或反斜杠之后。
123456789101112131415161718192021
```

***参考：[Python 正则表达式 flags 参数](https://blog.csdn.net/Yellow_python/article/details/80543937?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522164593201116780264025915%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&amp;request_id=164593201116780264025915&amp;biz_id=0&amp;utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-80543937.pc_search_result_cache&amp;utm_term=findall%E7%9A%84flags&amp;spm=1018.2226.3001.4187)***

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

## 3.2 serach

**`search()` 的用法和 `findall()` 的用法一样，但是 search() 只会返回第1个满足要求的字符串。一旦找到符合要求的内容，它就会停止查找。对于从超级大的文本里面只找第1个数据特别有用，可以大大提高程序的运行效率。**


```python
def search(pattern, string, flags=0):
    """Scan through string looking for a match to the pattern, returning
    a Match object, or None if no match was found."""
    return _compile(pattern, flags).search(string)
1234
```

**对于结果，如果匹配成功，则是一个`正则表达式的对象`，要得到匹配到的结果，则需要通过`.group()`这个方法来获取里面的值；如果没有匹配到任何数据，就是 `None`：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/a17459bdd29546b8a29e824a5c9612c5.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
**只有在`.group()`里面的参数为`1`的时候，才会把正则表达式里面的括号中的结果打印出来。**
**`.group()`的参数最大不能超过正则表达式里面括号的个数。参数为1表示读取第1个括号中的内容，参数为2表示读取第2个括号中的内容，以此类推：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/087a682685834e98bbec2f58ea448331.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

## 3.3 “.\* ” 和 “.\*?” 的区别

**在爬虫开发中，`.*?` 这3个符号大多数情况下一起使用。**

- **点号表示任意非换行符的字符，星号表示匹配它前面的字符0次或者任意多次。所以`“.*”表示匹配一串任意长度的字符串任意次`。**
- **这个时候必须在“.\*”的前后加其他的符号来限定范围，否则得到的结果就是原来的整个字符串。**
- **如果在`“.*”`的后面加一个问号，变成 `“.*?”`，那么可以得到什么样的结果呢？问号表示匹配它前面的符号0次或者1次。于是 `“.*?” 的意思就是匹配一个能满足要求的最短字符串`。**


![在这里插入图片描述](https://img-blog.csdnimg.cn/538fe8f232864c38b83f4e4641013113.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)

**使用`“(.*)”`得到的是只有一个元素的列表，里面是一个很长的字符串。**
**使用`“(.*?)”`得到的结果是包含3个元素的列表，每个元素直接对应原来文本中的每个密码。**

**总结:**

- **①`“.*”：贪婪模式，获取最长的满足条件的字符串`。**
- **②`“.*?”：非贪婪模式，获取最短的能满足条件的字符串`。**


[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

# 4、正则表达式提取技巧

## 4.1 不需使用 compile


```python
def findall(pattern, string, flags=0):
    """Return a list of all non-overlapping matches in the string.

    If one or more capturing groups are present in the pattern, return
    a list of groups; this will be a list of tuples if the pattern
    has more than one group.

    Empty matches are included in the result."""
    return _compile(pattern, flags).findall(string)

def compile(pattern, flags=0):
    "Compile a regular expression pattern, returning a Pattern object."
    return _compile(pattern, flags)
12345678910111213
```

**使用`re.compile()`的时候，程序内部调用的是`_compile()`方法；当使用`re.finall()`的时候，在模块内部自动先调用了`_compile()`方法，再调用`findall()`方法。`re.findall()`自带`re.compile()`的功能，所以没有必要使用`re.compile()`。**

[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

## 4.2 先抓大再抓小

**一些无效内容和有效内容可能具有相同的规则。这种情况下很容易把有效内容和无效内容混在一起，如下面这段文字：**


```python
有效用户:
姓名: 张三
姓名: 李四
姓名: 王五
无效用户:
姓名: 不知名的小虾米
姓名: 隐身的张大侠
1234567
```

**有效用户和无效用户的名字前面都以“姓名: ”开头，如果使用`“姓名: (.*?)\n”`来进行匹配，就会把有效信息和无效信息混在一起，难以区分：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/cadf8077c2b147f0ba589fab8933453b.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
**要解决这个问题，就需要使用先抓大再抓小的技巧。先把有效用户这个整体匹配出来，再从有效用户里面匹配出人名：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/507d6f74f97548d8b591cc1665c66c04.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
[**返回顶部**](https://blog.csdn.net/qq_45797116/article/details/123160308?spm=1000.2115.3001.6382&amp;utm_medium=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec&amp;depth_1-utm_source=distribute.pc_feed_v2.none-task-blog-hot_rank_bottoming-8.pc_personrec#0)

* * *

## 4.3 括号内和括号外

**在上面的例子中，`括号`和`“.*?”`都是一起使用的，因此可能会有读者认为括号内只能有这3种字符，不能有其他普通的字符。但实际上，括号内也可以有其他字符，对匹配结果的影响结果如下：**

![在这里插入图片描述](https://img-blog.csdnimg.cn/164c9a893f8d4182b9bc26427ac91a81.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBA6aqR552A6JyX54mb44Gy6L-95a-85by5Jw==,size_20,color_FFFFFF,t_70,g_se,x_16#pic_center)
**其实不难理解，只需要记住："`按照匹配规则查找，括号内的被提取`" 就可以了！**