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
check =True
count1 = 0
count2 = 0

while count1 <6: 
    c = random.randint(1,100)
    if c not in number1:    
        number1.append(c)
        count1 +=1
    if count1 == 6:
        break
print(number1)
while check:
    
    if count2 < 6 :
        a = int(input('請輸入數字:'))
        if a not in number2 and 0 < a < 101:
            number2.append(a)
            count2 += 1
        else:
            print('請輸入1-100且不重複的數字:')
    if count2 == 6 :
        check = False

print('您選的號碼是:',number2)
print('系統號碼為:',number1)

score = 0

for x in range(6):
     if number2.count(number2[x]) == number1.count(number2[x]):
         score +=1
print('您中了:',score,'個')

if score == 6:
    print('您獲得50顆蘋果')
elif score == 5:
    print('您獲得40顆蘋果')
elif score == 4:
    print('您獲得30顆蘋果')
elif score == 3:
    print('您獲得20顆蘋果')
elif score == 2:
    print('您獲得10顆蘋果')
else:
    print('很可惜!您沒中獎!')
    
'''
data= [99,1,10,6,88,60]
請將data排序，由小到大並印出排序後結果
請將data排序，由大到小並印出排序後結果
[1,6,10,60,88,99]
(使用迴圈)
'''
data1= [99,1,10,6,88,60]
for i in range(len(data1)-1):
    for j in range(len(data1)-1):
        if data1[j]>data1[j+1]:
            data1[j],data1[j+1] = data1[j+1],data1[j]
print(data1)

data2= [99,1,10,6,88,60]
for k in range(len(data2)-1):
    for l in range(len(data2)-1):
        if data2[l]<data2[l+1]:
            data2[l],data2[l+1] = data2[l+1],data2[l]
print(data2)
