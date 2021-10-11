# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:32:52 2021

@author: User-LS
"""

mahsulotlar=['makaron','guruch','non','tuz','choy','pomidor','bodring','mosh','tomat','pishloq']
savat=[]
bor_mahsulotlar=[]
mavjud_emas=[]
savat.append(input('1-mahsulotni tanlang\n'))
savat.append(input('2-mahsulotni tanlang\n'))
savat.append(input('3-mahsulotni tanlang\n'))
savat.append(input('4-mahsulotni tanlang\n'))
savat.append(input('5-mahsulotni tanlang\n'))
for xarid in savat:
    if xarid in mahsulotlar:
        bor_mahsulotlar.append(xarid)
    else :
        mavjud_emas.append(xarid)
if len(mavjud_emas)==0:
    print('Siz so\'ragan barcha mahsulotlar do\'konimizda bor')
else :
    print("Quyidagi mahsulotlar do\'konimizda yo\cc'q:")
    for m in mavjud_emas:
        print(m)