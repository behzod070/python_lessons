# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 10:00:33 2021

@author: User-LS
"""

son=int(input("Ixtiyoriy butun sonni kiriting\n"))
for n in range(1,10):
    if son%n==0:
        print(f"{son} {n}ga qoldiqsiz bo\'linadi")
        