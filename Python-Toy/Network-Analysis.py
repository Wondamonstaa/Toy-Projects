import pandas as pd
import networkx as nx
import numpy as nan
import matplotlib.pyplot as plt

"""Opening the file for reading."""
edge_data = pd.read_csv('/Users/wondamonsta/Downloads/twitter_cleaned(3).csv', encoding = 'ISO-8859-1')

print(edge_data.head())

#Creating an empty graph g.
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

#Below: getting the degree data for a graph.
degree_data = pd.Series(degree_dict)
print(degree_data.sort_values(ascending = False).head(10))
#degree_data.plot(kind = 'hist', title = 'Unscaled Degree Distribution by Kiryl Baravikou')
#plt.plot()

#Below: getting Pandas series of log base 10 of the degree distribution.
nan.log10(degree_data)
data_log = nan.log10(degree_data)
#data_log.plot(kind = 'hist', log = True, title = 'Distribution log of degrees by Kiryl Baravikou')


#Below: calculating the centrality using the method from the lecture.
data_centrality = nx.degree_centrality(g)
centrality_pandas = pd.Series(data_centrality)

#Printing the centrality values.
print(centrality_pandas.sort_values(ascending = False).head(10))

#Centrality for James only.
print(data_centrality ['James'])







#PROJECT 6
g_cored = nx.k_core(g, 3)
cored_plot = pd.Series(dict(nx.degree(g_cored)))
print(g_cored)

cored_lbl_dict = dict(g_cored.nodes())
for key in cored_lbl_dict:
    if len(str(key)) >= 8:
        cored_lbl_dict[key] = ((key[0:7]).strip()) + "."
    else:
        cored_lbl_dict[key] = key
        
cored_plot.plot(kind = 'hist', title = '3-cored graph degree distribution by Kiryl Baravikou', color = 'green')

#Drawing a graph with node labels
plt.figure(4, figsize =[10,10])
nx.draw_networkx(g_cored, labels = cored_lbl_dict, font_size = 8, with_labels = True, font_color="black")
plt.title("A cored graph with label names for the nodes by Kiryl Baravikou")


#Second ANALYSIS

edge_data1 = pd.read_csv('/Users/wondamonsta/Downloads/comm-f2f-Resistance/network_list.csv', encoding = 'ISO-8859-1')
print(edge_data1.head())

#Creating an empty graph g1.
g1 = nx.Graph()
g1.add_edges_from(edge_data1.values)
g1.add_node(0, level=int(0)) 
g1.number_of_edges()
g1.nodes()
g1.edges()
g1.remove_edges_from(nx.selfloop_edges(g1))
 

print(g1)

d1 = nx.degree(g1)
ddict1 = dict(d1)
degree_data1 = nx.degree(g1)
degree_dict1 = dict(degree_data1)

#Below: getting the degree data for a graph.
degree_data1 = pd.Series(degree_dict1)
print(degree_data1.sort_values(ascending = False).head(10))
degree_data1.plot(kind = 'hist', title = 'Second analysis: Degree Distribution by Kiryl Baravikou')


#Below: getting Pandas series of log base 10 of the degree distribution.
nan.log10(degree_data1)
data_log1 = nan.log10(degree_data1)
data_log1.plot(kind = 'hist', log = True, title = 'Second analysis: distribution log of degrees by Kiryl Baravikou')


#Below: calculating the centrality using the method from the lecture.
data_centrality_new = nx.degree_centrality(g1)
centrality_pandas_new = pd.Series(data_centrality_new)

#Printing the centrality values.
print(centrality_pandas_new.sort_values(ascending = False).head(10))

g_cored_new = nx.k_core(g1, 1)
cored_plot1 = pd.Series(dict(nx.degree(g_cored_new)))
print(g_cored_new)

cored_lbl_dict1 = dict(g_cored_new.nodes())
for k in cored_lbl_dict1:
    if len(str(k)) >= 8:
        cored_lbl_dict1[k] = ((k[0:7]).strip()) + "."
    else:
        cored_lbl_dict1[k] = k
        
cored_plot1.plot(kind = 'hist', title = 'Second analysis: 1-cored graph degree distribution by Kiryl Baravikou')

#Drawing a graph with node labels
plt.figure(4, figsize =[10,10])
new_graph = nx.draw_networkx(g_cored_new, labels = cored_lbl_dict1, font_size = 8, with_labels = True, font_color="black")
plt.title("1-cored graph degree distribution by Kiryl Baravikou")
















