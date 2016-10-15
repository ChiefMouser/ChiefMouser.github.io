---
layout: post
title:  effective_java
date: 2015-06-03
category: CSE
tags: [java]   
---

effective java 的简单总结

<!-- more -->

# 通用 

## 使用静态工厂函数 vs 构造函数

### 优点
- 名称便于区别，构造函数只有一个名字。工厂函数可以自定义，包含一定意义
- 可以避免重复创建对象，引申单利模式
- 可以返回子类，自定义时对象时，比如要求一个List,可以返回一个ArrayList，但是构造函数只会创建base

### 缺点

。。。


## 单例模式 

- public的静态成员
- 静态工厂函数

## 工具类的强化不可实例化

- 不要使用abstract，这回误导，以为这是一个需要继承实现的类
- 使用private的构造函数，避免编译器修改，这也导致了不能被继承

## 避免创建重复的对象

对比：

String s = new String("hello");  
String s = "hello";

- 可以使用工厂方法，如同上面所说
- 避免自己维护对象pool，代价非常大而且出错率高

## 消除过期的对象引用
过期引用

使用数组实现一个stack，存储某个类的对象，随着pop，stack的容量减小。  
这时不应该仅仅减小下标，因为不把pop出的部分改为null，就会出现一个过期的引用，由于这个引用在程序中再也不会访问到了，但是对于垃圾回收机制，这个引用是有效的，所以pop出的对象无法被回收内存。  
而且如果以后如果有越界引用的情况出现，就会得到null，而不是悄无声息的使用上一次的对象

上面例子的本质，stack类自己管理了内存，二垃圾回收机制并不知情

如果一个calss自己管理内存就应该小心内存泄漏的问题


## 避免使用 final 函数

从一个对象变得不可access到他被真正的回收，这之间的时间是不确定的。final 函数是不可靠的
final 函数有可能根本就不执行

使用显式的终止方法，并且在trycatch的额finally块中使用

更进一步的讨论？

## 改写equals方法

需要自己的 “相等逻辑”  

实现equals的几个要求：

- 自反
- 对称
- 传递
- 一致
- 非空x 比较 null一定为 false
- 总是要修改 hashCode：“相等的对象应该具有相等散列码”，在集合类中郭勇明显
- == 用于比较对象的引用地址
- instanceof检查是否为正确类型


## 怎样修改clone

如果一个类实现了clonable接口，则clone方法(如果可以调用的话)，应该此对象的”逐域拷贝“

通常接口是用来实现某些功能，clonable接口则改变了超累中一个受保护方法的行为

进一步？


# 泛型

- 不要使用原生的类型，就是去掉尖括号的情况，会失去安全性的保护
- @suppressWarnings(" ... ")
- 协变 convariant
    - 如果Sub为Sup的子类型，那么Sub[] 也就是 Sup[]的子类型
    - 泛型是不可协变的
    - List<Object> lo = new ArrayList<Long>是错误的，变异会出错 