# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 22:45:16 2021

@author: User-LS
"""
ismlar=['Davron','Sayxun','Shavkat']
print('Salom',ismlar[0])
print(ismlar[1],'ishlar qalay?')
print('Assalom alaykum',ismlar[2],'aka')
sonlar=[5,17,30,-20,11.8]
jami=sonlar[1]+sonlar[0]+sonlar[2]+sonlar[3]+sonlar[4]
print(jami)
print(sonlar[4]-sonlar[3])
print(sonlar[0]*sonlar[1]/sonlar[2])
sonlar[0]=10
print(sonlar)
del sonlar[3]
print(sonlar)
sonlar.remove(11.8)
print(sonlar)
sonlar.append(27)
print(sonlar)
sonlar.insert(0,93)
print(sonlar)

t_shaxslar=['Buxoriy','Termiziy','Navoiy','Zamaxshariy']
z_shaxslar=['Elon Musk','Jeff Bezos','Mark Sukerberg','Pavel Durov']
t_shaxs=t_shaxslar.pop(0)
z_shaxs=z_shaxslar.pop()
print('Men tarixiy shaxslardan',t_shaxs,'ni va zamonaviy shaxslardan',z_shaxs,'ni ko\'rishni istardim')

friends=['Safar','Begzod','Temur','Elbek','Ilyos']
friends.remove('Safar')
friends.remove('Temur')
print(friends)
friends.append('Shoxrux')
friends.insert(0,'Bobur')
friends.insert(2,'Qudrat')
print(friends)
mehmonlar=[]
mehmonlar.append(friends.pop(0))
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop())
print(mehmonlar)
print(friends)
print('Mehmonga',mehmonlar,'keldi')
print('Mehmonga',mehmonlar.pop(0),'keldi')




