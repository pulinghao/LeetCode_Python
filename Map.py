#!/usr/bin/env python
# _*_coding:utf-8 _*_
"""
 @Time  :2020/8/28 5:20 下午
 @Author  :pulinghao@baidu.com
 @File     :Map.py.py
 @Description :
"""

if __name__ == '__main__':
    filename = './map.txt'

    arry = list()
    with open(filename, 'r') as f1:
        list1 = f1.readlines()
        for i in range(len(list1)):

            line = list1[i]
            if 'plh log 坐标:' in line:
                # WGS84坐标系
                temp = line.split('坐标:')
                loc = temp[1]
                xy = loc.strip().split(',')
                x = xy[0]
                y = xy[1]
                xy_str = "@[@" + str(x) + ",@" + str(y) + "],"
                arry.append(xy_str)

    filenew = 'result.txt'

    with open(filenew, 'w') as file_object:
        for line in arry:
            file_object.write(line)
