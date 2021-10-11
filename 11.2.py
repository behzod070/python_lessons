# -*- coding: utf-8 -*-
"""
Created on Sun Oct  3 17:44:47 2021

@author: User-LS
"""

yosh=int(input('Yoshingiz nechada?\n'))
if yosh<4 or yosh>60:
    price="bepul"
elif yosh<18:
    price=10000
elif yosh>18:
    price=20000
print(f"Sizga kirish narxi {price}")

