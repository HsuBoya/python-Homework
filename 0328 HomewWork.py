# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 20:46:03 2022

@author: USER
"""

'''
由使用者輸入上面其中一個地區,
程式要印出該區的所有站名、可借、可停的資料
'''
import requests
import json

url ="https://data.ntpc.gov.tw/api/datasets/71CD1490-A2DF-4198-BEF1-318479775E8A/json?page=0&size=700"
bike = requests.get(url).text

data= json.loads(bike)
area={}
for row in data:
    if not (row['sarea'] in area):
        area[row['sarea']]=[]
    area[row['sarea']].append(row)

print(area.keys())

name =input('請輸入地區:')

for i in data:
    if i['sarea'].find(name)>=0:
      print('站名:',i['sna'],'可借數量:',i['sbi'],'可停數量:',i['bemp'])    