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