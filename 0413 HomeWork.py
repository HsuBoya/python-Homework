# -*- coding: utf-8 -*-
"""
Created on Wed Apr 13 20:50:48 2022

@author: User
"""
'''
請建立三個腳色的類別(以三國志Online )
武士(張飛、關羽)/warrior
軍師(孔明、龐統)/adviser
舞者(貂蟬)/dancer

每一個類別角色都要有姓名、血量、等級(請私有化)
每一個類別都有攻擊的方式 fight
每一個類別都有專屬於此類別的方法 buff
每一個類別都有專屬於此類別的必殺技 skill

由系統隨機取數去做兩個角色的互打
互打的過程需要列印出來。
EX:
關羽VS孔明
隨機取數 %2 餘數:1 ->關羽可以打孔明
隨機取數 %2 餘數:0 ->孔明可以打關羽

要印出類似於:
    關羽打孔明，孔明的血量為:XX
    關羽打孔明，孔明的血量為:XX
    關羽打孔明，孔明的血量為:XX

當血量<0，角色為Lose
假設:隨機取數當值為10 OR 20時，才可以使用必殺技，使用時，血量損失較多
'''
class warrior():
    def __init__(self,name,blood,level):
        self.__name = name
        self.blood = blood
        self.__level = level
    
    def fight(self):
        print('武士攻擊!')
    def buff(self):
        print('武士武力!')
    def skill(self):
        print('神力猛擊!')
    def display(self):
        print('{}；血量:{}，等級:{}'.format(self.__name,self.blood,self.__level))
    def __str__(self):
        return '{}'.format(self.__name)
class adviser():
    def __init__(self,name,blood,level):
        self.__name = name
        self.blood = blood
        self.__level = level
    
    def fight(self):
        print('軍師攻擊!')
    def buff(self):
        print('軍師增益!')
    def skill(self):
        print('萬紫千紅!')
    def display(self):
        print('{}；血量:{}，等級:{}'.format(self.__name,self.blood,self.__level))
    def __str__(self):
        return '{}'.format(self.__name)
class dancer():
    def __init__(self,name,blood,level):
        self.__name = name
        self.blood = blood
        self.__level = level
    
    def fight(self):
        print('舞者攻擊!')
    def buff(self):
        print('舞者魅力!')
    def skill(self):
        print('蝶舞翩翩!')
    def display(self):
        print('{}；血量:{}，等級:{}'.format(self.__name,self.blood,self.__level))
    def __str__(self):
        return '{}'.format(self.__name)

import random

wa = warrior('關羽',10,10)
ad = adviser('孔明',10,10)
da = dancer('貂蟬',10,10)

wa.display()
ad.display()
da.display()

for k in range(1):
    o = random.randint(0,3)
    if o == 0:
        player1 = wa
        player2 = ad
    elif o == 1 :
        player1 = wa
        player2 = da
    else:
        player1 = ad
        player2 = da

print(player1,'VS',player2)



fightStart = True

while fightStart :
    i = random.randint(1,51)
    # print(i)

    if i == 10:
        print(player1,'使用')
        player1.skill()
        print('攻擊',player2,'，',player2,'血量剩餘:',player2.blood-5)
        # print('{}，使用{} 攻擊{}，{}血量剩餘:{}'.format(player1,player1.skill(),player2,player2,player2.blood-5))
        
        player2.blood -= 5
    if i == 20:
        print(player2,'使用')
        player2.skill()
        print('攻擊',player1,'，',player1,'血量剩餘:',player1.blood-5)
        # print('{}，使用{} 攻擊{}，{}血量剩餘:{}'.format(player2,player2.skill(),player1,player1,player1.blood-5))
        player1.blood -= 5
    if i % 2 == 1 and i != 10:
        print(player1)
        player1.fight()
        print(player2,'，',player2,'血量剩餘:',player2.blood-1)
        # print('{}，{} 攻擊{}，{}血量剩餘:{}'.format(player1,player1.fight(),player2,player2,player2.blood-1))
        player2.blood -= 1
    if i % 2 == 0 and i != 20:
        print(player2)
        player2.fight()
        print(player1,'，',player1,'血量剩餘:',player1.blood-1)
        # print('{}，{} 攻擊{}，{}血量剩餘:{}'.format(player2,player2.fight(),player1,player1,player1.blood-1))
        player1.blood -= 1
    if player1.blood <= 0 or player2.blood <= 0:
        fightStart = False
        
    


if player1.blood <= 0:
    print(player2,'勝利!')
else:
    print(player1,'勝利!')        

