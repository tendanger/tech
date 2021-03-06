#coding=utf-8
from math import *
# input Lat_A 纬度A
# input Lng_A 经度A
# input Lat_B 纬度B
# input Lng_B 经度B
# output distance 距离(km)
def calcDistance(Lat_A, Lng_A, Lat_B, Lng_B):
    ra = 6378.137  # 赤道半径 (km)
    rb = 6356.752314140356  # 极半径 (km)
    flatten = (ra - rb) / ra  # 地球扁率
    #print(flatten)
    #flatten1 = 1/298.257222101
    #print(flatten1)
    rad_lat_A = radians(Lat_A)
    rad_lng_A = radians(Lng_A)
    rad_lat_B = radians(Lat_B)
    rad_lng_B = radians(Lng_B)
    pA = atan(rb / ra * tan(rad_lat_A))
    pB = atan(rb / ra * tan(rad_lat_B))
    xx = acos(sin(pA) * sin(pB) + cos(pA) * cos(pB) * cos(rad_lng_A - rad_lng_B))
    c1 = (sin(xx) - xx) * (sin(pA) + sin(pB)) ** 2 / cos(xx / 2) ** 2
    c2 = (sin(xx) + xx) * (sin(pA) - sin(pB)) ** 2 / sin(xx / 2) ** 2
    dr = flatten / 8 * (c1 - c2)
    distance = ra * (xx + dr)
    return distance

Lat_A=22.5369548317; Lng_A=114.0225501220 # 总部
Lat_B=39.9064024197; Lng_B=116.3624819407 # 北京分部
distance=calcDistance(Lat_A,Lng_A,Lat_B,Lng_B)
print('(Lat_A, Lng_A)=({0:10.3f},{1:10.3f})'.format(Lat_A,Lng_A))
print('(Lat_B, Lng_B)=({0:10.3f},{1:10.3f})'.format(Lat_B,Lng_B))
print('Distance={0:10.10f} km'.format(distance))