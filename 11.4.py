# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:13:12 2021

@author: User-LS
"""

mahsulotlar=['makaron','guruch','non','tuz','choy','pomidor','bodring','mosh','tomat''pishloq']
savat=[]
savat.append(input('1-mahsulotni tanlang\n'))
savat.append(input('2-mahsulotni tanlang\n'))
savat.append(input('3-mahsulotni tanlang\n'))
savat.append(input('4-mahsulotni tanlang\n'))
savat.append(input('5-mahsulotni tanlang\n'))
for xarid in savat:
    if xarid in mahsulotlar:
        print(f"Do\'konimizda {xarid} bor")
    else :
        print(f"Do\'konimizda {xarid} yo\'q")
            

