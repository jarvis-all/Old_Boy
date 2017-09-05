#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author: William Fu

### 集合是用大括号包围，没有重复数据，集合是无序的

list_1 = [1,2,3,3,4,5,6,7]
list_1 = set(list_1)
list_2 = set([2,4,7,9,0])

print(list_1,list_2)

# 列表 intersection 方法用于提取交集
print(list_1.intersection(list_2))
print("++++++++++++")
print(list_1 & list_2)

# 列表 union 方法用于提取并集
print(list_1.union(list_2))
print("++++++++++++")
print(list_1 | list_2)
# 列表 difference 方法用于提取差集，列表一存在列表二不存在的值
print(list_1.difference(list_2))
print("++++++++++++")
print(list_1 - list_2)
# 列表 issubset 方法用于提取子集，列表一是否是列表二的子集
print(list_1.issubset(list_2))#--子集
print(list_1.issuperset(list_2))#--父集

# 列表  symmetric_difference 方法用于提取对称差集-----双方互相都没有的值
print(list_1.symmetric_difference(list_2))
print("++++++++++++")
print(list_1 ^ list_2)
print("------------")

# 判断两个列表中是否存在交集，没有则返回True否则为False
print(list_2.isdisjoint(list_1))

print("......................................")
list_1.add(888)# 添加一项
list_1.update([99,777,555])# 添加多项
print(list_1)
list_1.remove(99)# 删除一项
print(list_1)
print(len(list_1))
