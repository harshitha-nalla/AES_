# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 11:59:12 2023

@author: babun
"""

# import networkx as nx
# import matplotlib.pyplot as plt
# import operator
# import random
# g=nx.gnp_random_graph(5,0.5,directed=True)
#
# nx.draw(g,with_labels=True)
# # plt.show()
# x = random.choice([i for i in range(g.number_of_nodes())])
# dic = {}
# for i in range(g.number_of_nodes()):
#     dic[i] = 0
# dic[x] = dic[x]+1
#
# for i in range(1000):
#     list_n = list(g.neighbors(x))
#
#     if len(list_n) == 0:
#         x = random.choice([i for i in range(g.number_of_nodes())])
#         dic[x] = dic[x]+1
#     else:
#         x = random.choice(list_n)
#         dic[x] = dic[x]+1
# p = nx.pagerank(g)
# print(p)
# print(dic)
#
#
#
#
#
import networkx as nx
import matplotlib.pyplot as plt
g=nx.barbell_graph(3,5)
nx.draw(g,with_labels=True)
plt.show()






