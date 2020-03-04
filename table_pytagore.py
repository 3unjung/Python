# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 00:26:58 2019

@author: Eunjung
"""

list = [0] * 20
 
for i in range(1, 21) :
    for j in range(1, 21) :
        list[j - 1] = i * j
    for indice in range(20) :
        print(list[indice], end = " ")
    print()