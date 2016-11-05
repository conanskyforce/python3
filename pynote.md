#This is my notes about python
***
###Python fundamental  

	print("abc")//print 必须要有(),  
	print("abc")//"abc"表示字符串abc  
	print(abc)//abc means variable  
	print(10)//10 means number  
	exit()//quit python environment
	print('a','b','c')//输出为字符串a b c，遇到逗号，会输出空格
	print('a'+'b'+'c')//输出为字符串abc  
	
####execute the py file：  
	python abc.py
####输入  
	name=input('输入提示')
	输入conan
	name='conan'
####Python基础
#开头的语句是注释，python只有单行注释，没有多行注释
当语句以冒号:结束时，缩进的语句为代码块  
坚持使用4个空格的缩进  
大小写敏感  
####数据类型
1. 整数
2. 浮点数
3. 字符串用单或双引号保卫起来的部分，转义字符\用于转义引号中内容  
为了简化，python还允许r''表示''内部的字符串默认不用进行转义
####布尔值
True和False(注意大小写)  
布尔值可以进行 and or not 运算  
and 表示 与  
or 表示 或  
not 表示 非  
####空值  
空值用None表示  
#####变量  
变量名必须是大小写英文，数字，下划线(_)的组合，而且不能用数字开头
变量被赋值：  
a = 'ABC'//计算机先是在内存中创建一个为 'ABC'的字符串，然后在内存中创建一个名为 a 的变量，并把它指向 'ABC'
####常量  
常量通常全部大写变量名称表示  
PI = 3.1415926535  
在python中有两种除法/(计算结果为浮点数)和//(地板除，计算结果为整数)
10/3 为3.33333333333  
10//3 为3   
% 取余  
10%3 为1  
####字符串和编码  
纯英文----ascii码
Unicode----所有语言  
utf-8----可变长编码Unicode  
ord()//获取字符的Unicode整数表示  
chr()//把编码转换为对应的字符  
ord("中")//20013
chr(25991)//文
知道字符的整数编码后，可以用十六进制这么写  
'\u4e2d\u6587'//'中文' 
网络传输或者保存磁盘，需要将str变为bytes  
加前缀b  
x = b'ABC'  
以Unicode表示的str可以通过encode()方法编码为制定的bytes  
'ABC'.encode('ascii')//b'ABC'
'中文'.encode('utf-8')//b'\xe4\xb8\xad\xe6\x96\x87'
'中文'.encode('ascii')//将报错
如果我们从网络上读取到了字节流，读取到的就是bytes,要将bytes变为str，就要用到decode()方法,在bytes中，无法显示为ascii的字节，用\x##表示    
b'ABC'.decode('ascii')//'ABC'
b'\xe4\xb8\xad\xe6\x96\x87'.decode('utf-8')//'中文'  
计算str包含多少个字符用len()函数  
len('ABC')//3  
len('中文')//2  
如果换成bytes，len()计算的就是字节数  
len(b'\xe4\xb8\xad\xe6\x96\x87')//6
len('中文'.encode('utf-8'))//6  
当源码包含中文时候，为了让他按utf-8编码读取，在文件开头写上  
# -*- coding:utf-8-*-  
####格式化  
用%实现  
'Hello,%s' %'world'//'Hello,world'
'Hello,%s%s,you have %d.'%('dear ','conan',10000000000)//'He-
llo,conan,you have 10000000000.'  
在字符串内部，%s表示用字符串代替，%d表示用整数代替，有几个%?占位符，后边就跟几个变量或值，顺序要对应好，如果只有一个%?，括号可以省略   
常见占位符  
%d 整数  
%f 浮点数  
%s 字符串  
%x 十六进制整数  
%如果表示普通字符，用%转义，即%%  
####list和tuple  
#####list
list(相当于array？)
mylist = ['a','b','c','d']
len(mylist)//获得mylist的长度(元素个数)  
mylist[0]//'a'  
mylist[1]//'b'  
mylist[2]//'c'  
mylist[3]//'d'  
mylist[4]//超出边界，报错  
mylist[-1]//'d'  
mylist[-2]//'c'
mylist[-5]//超出边界，报错  
append往末尾添加元素  
mylist.append('e')//mylist=['a','b','c','d','e']  
删除指定位置的元素用pop(i)，i为索引位置  
要将某个元素替换为别的元素，直接给对应位置赋值就行  
list元素的数据类型可以不同，甚至也可以包含另一个list  
#####tuple元组
tuple一旦初始化了之后，就不能修改  
mylist = ('a','b','c','d')  
现在这个tuple就不能变了，没有append()，insert()这样的方法，其他获取元素的方法和list 是一样的，也可以使用mylist[0],mylist[-1],但不能赋值为另外的元素。
定义只有一个元素的tuple元素时候，必须加一个逗号，来消除歧义  
>>>t = (1,)
>>>t
(1,)
####条件判断
sex=input("亲，请输入性别")
if sex == "男":
	print("您的性别为",sex)
	print("有意思")
else:
	print("您的性别不是男性")  
根据python的缩进规则 缩进为代码块，如果 if语句判断是True,就把缩进的两行都给执行了，如果判断为 False，则执行else下的内容  
注意不要少写冒号:
s = input("亲输入您的年龄")
age = int(s)//因为input()返回的数据类型是str,str不能直接和整数比较，必须先把 str转换成整数,int()方法将其转换为整数  
if age >= 25:
	print("大叔了")
elif age >=18:
	print("年轻有为")
elif age >=16:
	print("最好时光")
else:
	print("太嫩啦")  
if判断还能简写  
if x:
	print("meaningful")
只要x是 非零数值，非空字符串，非空list，非False，就判断为True，否则为False  
####循环  
python的循环有两种，一种 for…in 循环，以此将llist或tuple中的元素迭代出来   

	names = ['Michael', 'Bob', 'Tracy']
	for name in names:
	    print(name)
	Michael
	Bob
	Tracy
所以fox x in … 就是把每个元素带入变量x,然后执行缩进块的语句  
计算1-10整数之和，可以利用一个sum变量做累加  

	sum = 0
	for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
	    sum = sum + x
	print(sum)  
range()函数可以生成一个整数序列，再通过list()函数可以转化为list。
list(range(5))//[0,1,2,3,4]
range(101)就可以生成0-100的整数序列  

	sum = 0
	for x in range(101):
	    sum = sum + x
	print(sum)//

第二种while循环 只要满足条件，就不断循环   
计算100以内所有基数的和  

	sum = 0 
	a = 99
	while a > 0
		sum+=a
		a-=2
	print(a)  
break 提前退出循环  
continue跳出本轮循环  
Ctrl+c退出程序  
####dict 和set  
python中内置字典(JavaScript中的对象!)  
d = {'a':1,'b':2,'c':3,'d':4}
d['a']//1
d['c']//3  
通过key赋值  
d['a'] = 32//'a':32
一个key对应一个value  
如果key不存在，dict就会报错  
一是通过in方法判断key是否存在  
	
	'q' in d  
	False 
	'a' in d 
	True  
二是通过dict提供的get方法，如果key不存在，可以返回None，或者自己制定的value  
d.get('dcoasd')//返回None
d.get('dcoasd',-1)//返回 -1  
要删除一个key，用pop(key)方法，对应的value也会被删除  
d.pop('a')//d = {'b':2,'c':3,'d':4}
dict的key值必须是不可变对象，比如字符串，整数，而list不能作为list
因为dict根据key来计算value的储存位置，这种算法，也叫hash算法，如果key值为可变对象， 则报错，unhashable   
set  
set只有key值，没有value  
要创建一个set，需要提供一个list作为输入集合  
>>>s = set([1,2,3])  
>s
{1,2,3}  
注意，传入的参数是一个list,而现实的{1,2,3}只是告诉你这个set内部有1,2,3这3个元素，重复元素在set中自动被过滤  
add(key)添加元素到set中  
s.add(0)
>>>s
{1,2,3,0}
remove(key)可以删除元素  
s.remove(2)
>>>s
{1,3,0}
set可以看做数学意义上的无序和无重复元素的集合， 因此，两个set可以做数学的交集，并集等操作  

	s1 = set([1,2,3,4])  
	s2 = set([5,4,0,2,1])  
	s1&s2//{1,2}
	s1|s2//{0,1,2,3,4,5}  
	
	>>> a = 'abc'
	>>> a.replace('a', 'A')
	'Abc'
	>>> a
	'abc'  
####函数  
函数的调用  
abs(-15)//15  abs求绝对值  
max(1,2,-5,1.5)//2 返回较大的一个值  
数据类型的转换  
int('46'),将字符串转换为number  
str("24"),将数据类型转换为字符串  
bool(),转换为布尔值  
####定义函数  
	def my_abs(x):
		if x>=0:
			return x
		else:
			return -x
函数内部执行语句时候，一旦遇到return，函数就执行完毕，并返回结果。
将文件保存为abs.py  
那么久可以通过 from abs import my_abs 来导入my_abs()函数，即  
fro 文件名 import 函数名  
#####空函数  
	def nont():
		pass
定义一个函数，什么也不做(用作占位符，就是没想好函数怎么写的时候)
  
	def my_abs(x):
	    if not isinstance(x, (int, float)):
	        raise TypeError('bad operand type')
	    if x >= 0:
	        return x
	    else:
	        return -x
	return x1,x2//return 也可以返回多个值，其实是一个tuple!  
#####函数的参数  
######位置参数与默认参数  
power(x,y,z=18,a="Beijing")  
默认参数可以不提供，当提供的时候，参数按顺序赋值，或直接用等于=号赋值  
默认参数必须指向不变对象！  
######可变参数
组装一个list或tuple调用进去!!! 

	def calc(*numbers):
	    sum = 0
	    for n in numbers:
	        sum = sum + n * n
	    return sum
参数多一个*！
calc((1,2,5,7,9))简写为calc(1,2,5,7,9)!  

	>>> nums = [1, 2, 3]
	>>> calc(*nums)
	14
在list或tuple前面加一个*，把其元素变为参数传递进去  
######关键字参数  
	>>> extra = {'city': 'Beijing', 'job': 'Engineer'}
	>>> person('Jack', 24, **extra)
	name: Jack age: 24 other: {'city': 'Beijing', 'job': 'Engineer'}  
没有可变参数的情况下，用*作为分隔符  

	def person(name, age, *, city='Beijing', job):
	    print(name, age, city, job)
#####参数组合  
参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。  
	def f1(a, b, c=0, *args, **kw):
	    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
	
	def f2(a, b, c=0, *, d, **kw):
	    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
	>>> f1(1, 2)
	a = 1 b = 2 c = 0 args = () kw = {}
	>>> f1(1, 2, c=3)
	a = 1 b = 2 c = 3 args = () kw = {}
	>>> f1(1, 2, 3, 'a', 'b')
	a = 1 b = 2 c = 3 args = ('a', 'b') kw = {}
	>>> f1(1, 2, 3, 'a', 'b', x=99)
	a = 1 b = 2 c = 3 args = ('a', 'b') kw = {'x': 99}
	>>> f2(1, 2, d=99, ext=None)
	a = 1 b = 2 c = 0 d = 99 kw = {'ext': None}  

*args是可变参数，args接收的是一个tuple  
*kw是关键字参数，kw接收的是一个dict  
####递归函数  
阶乘  

	def fact(n):
	    if n==1:
	        return 1
	    return n * fact(n - 1)
尾递归是指，在函数返回的时候，调用自身本身，并且，return语句不能包含表达式。这样，编译器或者解释器就可以把尾递归做优化，使递归本身无论调用多少次，都只占用一个栈帧，不会出现栈溢出的情况。  

	def hanoi(n,x,y,z):
	    if n==1:
	        print(x,'-->',z)
	    else:
	        hanoi(n-1,x,z,y)#将前n-1个盘子从x移动到y上
	        hanoi(1,x,y,z)#将最底下的最后一个盘子从x移动到z上
	        hanoi(n-1,y,x,z)#将y上的n-1个盘子移动到z上
	n=int(input('请输入汉诺塔的层数：'))
	hanoi(n,'x','y','z')
####高级特性  
#####切片  
	创建一个0-99的数列  
	L = list(range(100))
	通过切片取出一段 
	前十个
	L[0:10]等价于L[:10]
	后十个
	L[-10:]
	前11-20个  
	L[10:20]
	前10个，每两个取一个  
	L[:10:2]
	所有数字，每五个取一个
	L[::5]
	复制一个list
	L[:]
tuple也是一种list，只是tuple不可变，操作结果仍然为tuple
字符串也是一种list，每个元素就是一个字符，因此，字符串也能进行切片操作，结果仍然是字符串  

	(1,2,3,5,7,8)[1:3]//(2,3)
	"asdasf"[-3:]//"asf"
