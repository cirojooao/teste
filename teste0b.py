#!/usr/bin/env python
#-*- coding:utf-8 -*-

from sqlobject import *
sqlhub.processConnection = connectionForURI('sqlite:///home/alunos/banco.db')


class pessoa(SQLObject):
    nome = StringCol()
    idade = IntCol()


# pessoa.createTable()
# p1 = pessoa( nome='joao', idade=20 )   
# p2 = pessoa( nome='maria', idade=30 )  

for p in pessoa.select(pessoa.q.idade>25):
    print p



