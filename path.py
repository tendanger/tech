import pandas as pd
import networkx as nx
import pylab
import numpy as np
d3=pd.read_csv('./edges.shp.csv',low_memory=False)
list_id_from = d3['from'].tolist()
list_id_to = d3['to'].tolist()
list_lenght = d3['length'].tolist()

#自定义网络
#row=np.array([0,0,0,1,2,3,6])
#col=np.array([1,2,3,4,5,6,7])
#value=np.array([1,2,1,8,1,3,5])
a = [str(i) for i in list_id_from]
row = a
b = [str(i) for i in list_id_to]
col = b

c = [float(i) for i in list_lenght]
value = c
print(len(row),len(col),len(value))
print(a)
print(b)
print('生成一个空的有向图')
G = nx.Graph()
for i in range(0,len(row)):
    n1 = str(row[i])
    n2 = str(col[i])
    #print(strlist[2])
    weight = float(value[i])
    #print(n1,n2,weight)

    G.add_weighted_edges_from([(n1, n2, weight)]) #G.add_edges_from([(n1, n2)])

#print('给网路设置布局...')
#pos=nx.shell_layout(G)
#print('画出网络图像：')
#nx.draw(G,pos,with_labels=True, node_color='white', edge_color='red', node_size=400, alpha=0.5 )
#pylab.title('Self_Define Net',fontsize=15)
#pylab.show()

print(1)
'''
Shortest Path with dijkstra_path
'''
print('dijkstra方法寻找最短路径：')
path=nx.dijkstra_path(G, source=str(49443530), target=str(49135195))
print('节点49217573到49479756的路径：', path)
print('dijkstra方法寻找最短距离：')
distance=nx.dijkstra_path_length(G, source= 49605185, target= 6002709)
print('节点49217573到49479756的距离为：', distance)