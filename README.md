# C语言
大家需要掌握如下内容: **递归, 指针, 链表**, 并且能够独立写出正确的程序(而不是在百度上搜一个所谓的示例代码).
[南京大学 2020PA](https://www.bilibili.com/video/BV1qa4y1j7xk?)
收音不太好 配合一个网页教程
[linxu C编程一站式学习](http://akaedu.github.io/book/)
[The C programming language (2nd Edition)](http://math.ecnu.edu.cn/~jypan/Teaching/ParaComp/books/The%20C%20Programming%20Language%202nd.pdf): 真正的C语言之父是这本书的作者Dennis M. Ritchie, 而不是谭浩强
[SEI CERT C Coding Standard](https://wiki.sei.cmu.edu/confluence/display/c/SEI+CERT+C+Coding+Standard)

# missing courese
github-->https://github.com/missing-semester-cn/missing-semester-cn.github.io

[计算机科学课堂中学不到的知识 The Missing Semester of Your CS Education](https://www.bilibili.com/video/BV1x7411H7wa)
配合这个作业和教案一起看
[The Missing Semester of Your CS Education 中文版](https://missing-semester-cn.github.io/)
这种网站的制作可以弄下 github.io 的

## 命令行
https://github.com/jlevy/the-art-of-command-line

## gcc与库
gcc 参数说明 
-I 加头文件目录


### 生成静态库
linux中使用ar生成 命名 libxxx.a
windows中 libxxx.lib

准备好源文件 汇编 得到库 只要不链接
gcc * .c -c 得到一堆.o 之后 用gcc工具中的ar 对.o文件进行打包

打包 ar rcs libxxx.a *.o

发布 head.h libxxx.a 放在一个目录


### 使用静态xx
-l使用的库的名字 libxxx.a ---> -lxxx 可以有空格也可以没有
-L ./指定当前目录
gcc main.c -L . -lxxx -o test1

### 生成动态库
共享库 
linux中  libxxx.so 不同点 动态库有执行权限 静态库没有
windows中 libxxx.dll  在windows下制作工具不同得到的库文件不太一样

准备好.o  但是要加上-fpic 生成和位置无关的.o
与位置无关 相对于静态库而言 在运行空间中 没有绝对地址 不在代码区
而在动态库加载区 只有调用的时候才会被放在对应的位置

打包 gcc -shared *.o -o libxxx.so

发布 head.h libxxx.so

### 使用动态库
gcc main.c -L . -l xxx -o test2

### 解决动态库加载不到
由于动态库主程序中没有加载到代码区 所以不在同一目录会加载不到

查看动态库加载过程 ldd test2 可以用来验证链接的所有函数能否找到


加载动态库: linux动态链接器
寻找路径  可执行文件内部的DT_RPATH  --> 系统环境变量LD_LIBRARY_PATH  -->  系统动态库缓存文件 /etc/ld.so.cache --> 系统库目录 /lib /usr/lib

解决方案 
1放进系统变量 
echo $LD_LIBRARY_PATH 
LD_LIBRARY_PATH=库目录:$LD_LIBRARY_PATH 环境变量之间用:分割
但是只对当前终端有效 要对用户配置文件或者系统配置文件进行更新
用户: ~/.bashrc  最后加 export LIBRARY_PATH =$LIBRARY_PATH:库目录
标准写法是前面加个export 不写也可
终端重启后生效 或者让终端重新加载配置文件
. ~/.bashrc 第一个点是source的意思

系统: /etc/profile
加入后重启操作系统 或者. /etc/profile

2更新sudo vim /etcc/ld.so.conf
在第二行加入存储动态库的位置
然后 sudo ldconfig 完成跟新ld.so.chche
sudo ldconfig -v 查看所有更新的信息


3在lib或者/usr/lib创建软链接
sudo ln -s ...../libxxx.so /usr/lib/libxxx.so
更新的效率更高 

### 两个库的对比 
1. 静态库在程序的内部 多个拷贝将占用大量的资源
2. 静态库需要和程序一起编译 每次改变主程序需要重新编译
3. 多个进程调用同一个动态库时可以共享 动态库较慢 但现在的计算机性能可以忽略 发布程序需要提供依赖的库

当程序较小的时候 使用静态库
源文件量比较大的时候 使用动态库

## makefile



# 关于PA 应该去看一下cmu csapp