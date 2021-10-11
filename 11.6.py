# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 10:51:31 2021

@author: User-LS
"""

users=['Davron','Shavkat','Anvar','Sayxun','Davlat']
user=input("Login tanlang\n")
for login in users:
   if user.lower()==login.lower():
       print('Bu login band,iltimos boshqa login tanlang')
   else:
       print ('Xush kelibsiz')
    