# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 19:43:49 2022

@author: USER
"""
'''
1.由系統自動產生6個不重複的數字(1,100)
2.由使用者自行輸入六個號碼
3.先印出系統的六個號碼，再印出使用者中了幾個
4.中2個獲得10顆蘋果，中三個獲得20顆蘋果，中4個獲得30顆蘋果，中5個獲得40顆蘋果，中6個獲得50顆蘋果
'''

import random

number1 = []
number2 = []
for i in range(6):
    n = random.randint(1,100)
    number1.append(n)
print(number1)


o = input('請輸入數字:')
count = 0

for j in range(6):
    if count == 6:
        break
else:
    o = input('請輸入數字:')
    count += 1
print(number2)



#if number1 == number2:
    


'''
data= [99,1,10,6,88,60]
請將data排序，由小到大並印出排序後結果
請將data排序，由大到小並印出排序後結果

(使用迴圈)
'''







'''
999999999
 8888888
  77777
   666
    5
   666
  77777
 8888888
999999999


(使用迴圈)
'''