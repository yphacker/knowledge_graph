# coding=utf-8
# author=yphacker

import os
import numpy as np
import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher

# 连接Neo4j数据库
graph = Graph(' http://localhost:7474/db/data/', username='neo4j', password='1314')

# 读取数据
stock = pd.read_csv('stock_basic.csv')
holders = pd.read_csv('stock_holders.csv')
concept = pd.read_csv('concept.csv')
concept_details = pd.read_csv('concept_details.csv')
sh = pd.read_csv('sh.csv')
sz = pd.read_csv('sz.csv')

# 创建实体(股票、股东、概念、成分股)
node = Node('深股通', 名字='深股通')
graph.create(node)

node = Node('沪股通', 名字='沪股通')
graph.create(node)

for i in concept.values:
    a = Node('概念', 概念代码=i[1], 概念名称=i[2])
    graph.create(a)
    print('概念代码:' + str(i[1]), '概念名称:' + str(i[2]))

for i in stock.values:
    a = Node('股票', TS代码=i[1], 股票名称=i[3], 地域=i[4], 行业=i[5])
    graph.create(a)
    print('TS代码:' + str(i[1]), '股票名称:' + str(i[3]), '地域:' + str(i[4]), '行业:' + str(i[5]))

for i in holders.values:
    a = Node('股东', TS代码=i[1], 股东名称=i[4], 持股数量=i[5], 持股比例=i[6])
    graph.create(a)
    print('TS代码:' + str(i[1]), '股东名称:' + str(i[4]), '持股数量:' + str(i[5]), '持股比例:' + str(i[6]))

# 创建关系(股票-股东、股票-概念、股票-成分股票、股票-地域)
matcher = NodeMatcher(graph)
for i in holders.values:
    a = matcher.match("股票", TS代码=i[1]).first()
    b = matcher.match("股东", TS代码=i[1])
    for j in b:
        r = Relationship(j, '参股', a)
        graph.create(r)
        print('TS', str(i[1]))

for i in sh.values:
    a = matcher.match("股票", TS代码=i[0]).first()
    b = matcher.match("深股通").first()
    r = Relationship(a, '成分股属于', b)
    graph.create(r)
    print('TS代码:' + str(i[1]), '--沪股通')

for i in sz.values:
    a = matcher.match("股票", TS代码=i[0]).first()
    b = matcher.match("沪股通").first()
    r = Relationship(a, '成分股属于', b)
    graph.create(r)
    print('TS代码:' + str(i[0]), '--深股通')

for i in concept_details.values:
    a = matcher.match("股票", TS代码=i[3]).first()
    b = matcher.match("概念", TS代码=i[1]).first()
    if a == None or b == None:
        continue
    r = Relationship(a, '概念属于', b)
    graph.create(r)

# for i in stock.values:
#     a = matcher.match("股票",)
#     b = matcher.match("地域",)
