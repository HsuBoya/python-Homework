# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 19:54:37 2022

@author: USER
"""
# 九九乘法表
for a in range(1,10):
    
    for b in range(2,10):
        print(b,'x',a,'=',a*b,sep='',end='\t')
    print()

print()

# 
for i in range(5,0,-1):
    for c in range(i):
        print(i,sep='',end='')
    print()
    
print()

# 1-100之間質數有哪些 (質數=只能被1及自己整除)
        
for d in range(2,101):
    for e in range(2,d-1):
        if d%e ==0:
            break
    else:
        print(d,end=',')

        
        


        



        
    

   
