#Name: Kiryl Baravikou
#Course: CS113
#Date: 4/15/22
#Lab: Week 13: Network Analysis

import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

edge_data = pd.read_csv('/Users/wondamonsta/Downloads/twitter_cleaned(3).csv', encoding = 'ISO-8859-1')

print(edge_data.head())
g = nx.Graph()


g.add_node("Alice")
g.add_node("Bob")
g.add_node("Charlie")
g.add_edge("Bob", "Alice")
g.add_edge("Bob", "Charlie")

g.number_of_edges()
g.nodes()
g.edges()
list(g.nodes)
list(g.edges)
g.add_edges_from(edge_data.values)
print(g)


d = nx.degree(g)
ddict = dict(d)
#degree_data = nx.degree(g)

#degree_dict = dict(degree_data)
#Below: getting the degree data for a graph
degree_pd = pd.Series(dict(nx.degree(g)))

print(degree_pd.sort_values(ascending = False).head(10))

#Below: getting Pandas series of log base 10 of the degree distribution
np.log10(degree_pd)
data_log = np.log10(degree_pd)
x = data_log.plot(kind = 'hist', title = 'Distribution log of degrees by Kiryl Baravikou')
print(x)
#print(data_log.plot(kind = 'hist', title = 'Distribution log of degrees by Kiryl Baravikou'))
print(degree_pd.plot(kind ='hist', title = 'Unscaled Degree Distribution by Kiryl Baravikou'))

data_centrality = nx.degree_centrality(g)
centrality_pandas = pd.Series(data_centrality)
print(centrality_pandas.sort_values(ascending = False).head(10))
print(data_centrality ['James'])
      


      
      
      
      
      
      
      
      
      