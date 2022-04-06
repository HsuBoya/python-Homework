# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 21:35:44 2022

@author: USER
"""
'''
1
2  3
4  5  6
7  8  9  10 
11 12 13 14 15
可用串列
'''
data2 = [[1],[2,3],[4,5,6],[7,8,9,10],[11,12,13,14,15]]

for i in range(len(data2)):
    for j in range(i+1):
        print(data2[i][j],sep='',end=' ')
    print()
'''
2/1 + 3/2 + 4/3 + 5/4 + 6/5 + 7/6 + 8/7 +.........+ 21/20
求和
'''


'''
輸入三個值:a,b,c
呼叫函式，由大至小順序輸出
'''
def per(a,b,c):
    
    data = [a,b,c]
    data1 = sorted(data,reverse=True)
    print(data1)

a = int(input('number1:'))
b = int(input('number2:'))
c = int(input('number3:'))
per(a,b,c)

'''
有四個數字1,2,3,4
可以取出多少數字不重複的三位數字
'''
data4 = list()

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and j != k and i != k:
                n = '{}{}{}'.format(i,j,k)
                data4.append(n)
print(data4)
print(len(data4))
