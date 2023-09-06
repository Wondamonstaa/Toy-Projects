#Name: Kiryl Baravikou
#Course: CS113
#Date: 4/15/22
#Lab: Week 13: Network Analysis

import pandas as pd
import networkx as nx
import numpy as nan
import matplotlib.pyplot as plt

"""Opening the file for reading."""
edge_data = pd.read_csv('/Users/wondamonsta/Downloads/twitter_cleaned(3).csv', encoding = 'ISO-8859-1')

print(edge_data.head())

"""Creating an empty graph g."""
g = nx.Graph()
g.add_edges_from(edge_data.values)

g.number_of_edges()
g.nodes()
g.edges()

print(g)

d = nx.degree(g)
ddict = dict(d)
degree_data = nx.degree(g)
degree_dict = dict(degree_data)

"""Below: getting the degree data for a graph."""
degree_data = pd.Series(degree_dict)
print(degree_data .sort_values(ascending = False).head(10))
#degree_data.plot(kind = 'hist', title = 'Unscaled Degree Distribution by Kiryl Baravikou')
#plt.plot()

"""Below: getting Pandas series of log base 10 of the degree distribution."""
nan.log10(degree_data)
data_log = nan.log10(degree_data)
#data_log.plot(kind = 'hist', log = True, title = 'Distribution log of degrees by Kiryl Baravikou')
plt.plot()

"""Below: calculating the centrality using the method from the lecture."""
data_centrality = nx.degree_centrality(g)
centrality_pandas = pd.Series(data_centrality)

"""Printing the centrality values."""
print(centrality_pandas.sort_values(ascending = False).head(10))

"""Centrality for James only."""
print(data_centrality ['James'])


#PROJECT 6
g_cored = nx.k_core(g, 5)
print(g_cored)
cored_plot = pd.Series(dict(nx.degree(g_cored)))
cored_plot.plot(kind = 'hist', title = '3-cored graph degree distribution by Kiryl Baravikou')

plt.figure(4, figsize =[10,10])
nx.draw_networkx(g_cored, font_size = 8, with_labels = True)

new_dict = dict(g.nodes())
str_dict = str(new_dict)
final_dict = eval(str_dict)
ex_final_dict = dict(final_dict)

nodes = g_cored.nodes()
labels_dict = {}
for key in nodes:
    if len(str(key)) <= 8:
        labels_dict[key] = key
    else:
        labels_dict[key] = key[0:7] + "."

#labels_dict = dict(g_cored_nodes)
nx.draw_networkx(g_cored, labels = labels_dict, with_labels = True)

#for x in labels_dict:
#   if type(x) == str:
#        if len(x)>8:
#            labels_dict[x] = x[:7] + "."
#        else:
            
    
     
g = nx.Graph()
g.add_edges_from(edge_data.values)
g.remove_edges_from(nx.selfloop_edges(g))
g_cored = nx.k_core (g,3)
edgelist = g_cored.edges
e_dict = nx.betweenness_centrality(g_cored)
#dictionary for use in defining edge importance
n_dict = nx.betweenness_centrality(g_cored)
#dictionary for node color
#centrality may be different from e_dict
#nx.draw(g, with_labels=True,font_weight='bold')
#nx.draw(g)      
#degree_data = pd.Series(dict(nx.degree(g)))
#log_degree = np.log10(degree_data)

#log_degree.plot(kind='hist', log=True,title="Log Log Histogram of Degree Distribution")