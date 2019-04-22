import numpy as np
import networkx as nx
lst = ['a','b','c','d','e','f','g','h','i','j','k']
for i in range(1,12):
	filename = 'snapshots/' + str(lst[i-1]) + ".txt"
	nfilename = 'snapshots/s' + str(i) + "_graph.gpickle"
	G = nx.read_edgelist(filename, create_using=nx.Graph())
	print(G.number_of_nodes())
	nx.write_gpickle(G,nfilename)
