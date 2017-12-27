#!/usr/bin/env python
# -*- coding: utf-8 -*-
# sort dictionary data w.r.t. keys and balues

score = ["A","B","C","D","E","F","G","H","I", "J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

f = open('text.txt')
name = f.read()
f.close()
names = name.split(",")

names_list = []
for i in range(0,len(names)):
    names_list.append(names[i].replace('"',''))
names_list.sort()

total_score = 0
str_list = []

def calculate_list_score(name):
    name_score = 0
    str_list = list(name)
    for i in range(0,len(str_list)):
        for j in range(0,len(score)):
            if str_list[i] == score[j]:
                name_score += (j+1)
    return(name_score)
                
for i in range(0,len(names_list)):
    single_score = calculate_list_score(names_list[i])
    total_score += (i + 1) * single_score
print(total_score)
