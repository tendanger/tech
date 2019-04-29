# -*- coding: utf-8 -*-
from sklearn.cluster import KMeans
from sklearn.externals import joblib
import numpy
import time
#import KMeans
import matplotlib.pyplot as plt

if __name__ == '__main__':
#step 1: 加载数据
    print("step 1: load data...")
    dataSet = []
    fileIn = open('./data-1.txt')
    for line in fileIn.readlines():
        lineArr = line.strip().split(' ')
        dataSet.append([float(lineArr[0]), float(lineArr[1])])

    #设定不同k值以运算
    for k in range(2,10):
        clf = KMeans(n_clusters=k) #设定k  ！！！！！！！！！！这里就是调用KMeans算法
        s = clf.fit(dataSet) #加载数据集合
        numSamples=len(dataSet)
        centroids = clf.labels_
        print(centroids,type(centroids)) #显示中心点
        #print( clf.inertia)#显示聚类效果
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        #画出所有样例点 属于同一分类的绘制同样的颜色
        for i in range(numSamples):
            #markIndex = int(clusterAssment[i, 0])
            plt.plot(dataSet[i][0], dataSet[i][1], mark[clf.labels_[i]]) #mark[markIndex])
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
        # 画出质点，用特殊图型
        centroids = clf.cluster_centers_
        for i in range(k):
            plt.plot(centroids[i][0], centroids[i][1], mark[i], markersize = 12)
            #print centroids[i, 0], centroids[i, 1]
        plt.show()
        print(centroids)