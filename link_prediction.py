import numpy as np
from sklearn import metrics
from sklearn.model_selection import train_test_split
import networkx as nx
from keras.models import Model, Sequential, load_model
import matplotlib.pyplot as plt


file_prefix = 'snapshots/s'
graph_file = file_prefix + str(7) + '_graph.gpickle'
g = nx.read_gpickle(graph_file)
N = g.number_of_nodes()

test_ratio = 0.15
train_set, test_edges = train_test_split(g.edges(), test_size=test_ratio)
g.remove_edges_from(test_edges)

final_model = load_model("models/prev_model_7.h5")

adj_mat = nx.adjacency_matrix(g).toarray()

reconstructed_adj = final_model.predict(adj_mat)

# reconstructed_adj = np.reshape(reconstructed_adj, (-1, 2))
# adj_mat = np.reshape(adj_mat, (-1, 2))

rows = adj_mat.shape[0]
cols = adj_mat.shape[1]
y_act = []

for x in range(0, rows):
    for y in range(0, cols):
        y_act.append(adj_mat[x,y])

pred =  []   
for x in range(0, rows):
    for y in range(0, cols):
        pred.append(reconstructed_adj[x,y])


fpr, tpr, thresholds = metrics.roc_curve(y_act, pred)
print(metrics.auc(fpr, tpr))
roc_auc = metrics.auc(fpr, tpr)


#Plotting

plt.title('Receiver Operating Characteristic')
plt.plot(fpr, tpr, 'b', label = 'AUC = %0.2f' % roc_auc)
plt.legend(loc = 'lower right')
plt.plot([0, 1], [0, 1],'r--')
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.ylabel('True Positive Rate')
plt.xlabel('False Positive Rate')
plt.show()
