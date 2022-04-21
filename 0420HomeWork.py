# -*- coding: utf-8 -*-
"""
Created on Wed Apr 20 21:37:54 2022

@author: User
"""

'''
把資料抓回來後寫進EXCEL
台南市OPENDATA

http://tbike-data.tainan.gov.tw/Service/StationStatus/Json
OBIKE資料，將抓到的資料寫入EXCEL表中

工作表名稱 :obike
工作表的欄位標題有:
    站名、地址、總數量、可借、可停、經度、緯度
'''
import requests
import json
import openpyxl

url ="http://tbike-data.tainan.gov.tw/Service/StationStatus/Json"
bike = requests.get(url).text

data= json.loads(bike)


wb = openpyxl.Workbook()
ws = wb.active

title = ['站名','地址','總數量','可借','可停','經度','緯度']
ws.title = 'obike'
ws.append(title)


for row in data:
    ws.append([row['Id'],row['Address'],row['Capacity'],row['AvaliableBikeCount'],row['AvaliableSpaceCount'],row['Latitude'],row['Longitude']])


wb.save('0420HomeWork.xlsx')