#!/usr/bin/python3
#-*-coding:utf-8-*-

data_file_name = 'data/1_Poisy-ParcDesGlaisins.txt'
data_file_name = 'data/2_Piscine-Patinoire_Campus.txt'


def dates2dic(dates):
    dic = {}
    splitted_dates = dates.split("\n")
    #print(splitted_dates)
    for stop_dates in splitted_dates:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic

