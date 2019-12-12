# coding=utf-8
# author=yphacker

import pandas as pd
from py2neo import Graph, Node, Relationship, NodeMatcher
from conf import config


class Neo4jModel(object):
    def __init__(self):
        # 连接Neo4j数据库
        self.graph = Graph('http://localhost:7474/db/data/',
                           username=config.neo4j_password,
                           password=config.neo4j_username)

    def insert(self):
        pass

    def run(self, cypher_text):
        return self.graph.run(cypher_text)


def main(cypher_text):
    neo4j_model = Neo4jModel()
    neo4j_model.run(cypher_text)


if __name__ == '__main__':
    main('MATCH (n:`Person`)-[r]->(m:`Person`) return n,m,type(r)')
