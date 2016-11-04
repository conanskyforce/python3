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
'中文'.encode('ascii')//报错
 
