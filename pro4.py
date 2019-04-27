#-*- coding:utf8-*-
#讲文本转化为.net文件
#import networkx as nx
import networkx as nx
import numpy as np
import pylab
### read edge list to networkx ###/Users/kun/Desktop/
# the format of each line: (src dst whole_duration/total_duration total_duration)
G = nx.Graph()
#for line in open("C://2017/2017_f", encoding='UTF-8'):
#for line in open("/Users/kun/Desktop/", encoding='UTF-8'):
for line in open("./2", encoding='UTF-8'):
    strlist = line.split(" ")
    #print(strlist)
    n1 = str(strlist[0])
    n2 = str(strlist[1])
    #print(strlist[2])
    weight = float(strlist[2])
    print(type(n1))

    G.add_weighted_edges_from([(n1, n2, weight)]) #G.add_edges_from([(n1, n2)])

import matplotlib.pyplot as plt
#assign node ID as nodes' label. G.nodes return a list of nodes, convert list to dict
print(1)
print('给网路设置布局...')
pos=nx.shell_layout(G)
print('画出网络图像：')
#nx.draw(G,pos,with_labels=True, node_color='white', edge_color='red', node_size=400, alpha=0.5 )
#pylab.title('Self_Define Net',fontsize=15)
#pylab.show()
#nx.draw(G)
#numpy保存权重邻接矩阵到文件
#G_matrix=nx.to_numpy_matrix(G)
#print(G_matrix)
#np.savetxt('./2.txt',G_matrix,fmt='%d',newline='\n')
#np.savetxt('/Users/kun/Desktop/2017_f3.txt',G_matrix,fmt='%s',newline='\n')
print('dijkstra方法寻找最短路径：')
path=nx.dijkstra_path(G, source=str(5717326552), target=str(49358974))
print('节点间的路径：', path)
print('dijkstra方法寻找最短距离：')
distance=nx.dijkstra_path_length(G, source=str(5717326552), target=str(49358974))
print('节点间的距离为：', distance)

#nx.write_pajek(G, "/Users/kun/Desktop/2017_f3.net", encoding='UTF-8')
#nx.write_gexf(G, "./f.gexf", encoding='UTF-8')
#labels = dict((i,i) for i in G.nodes())
#print(1)
#print(labels)
#nx.draw_networkx_labels(G, pos=nx.spring_layout(G), labels = labels)
#plt.savefig(filename)

#plt.show()