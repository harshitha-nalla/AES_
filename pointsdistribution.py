import networkx as nx
import random
import matplotlib.pyplot as plt
g=nx.gnp_random_graph(5,0.5,directed=True)
nx.draw(g,with_labels=True)
def assign(g):
    for i in range(g.nodes()):

