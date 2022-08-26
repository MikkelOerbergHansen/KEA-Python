# import moduler

import json
import pandas as pd

## import json med json

retailers = open('../case-2-1/gubi-retailers.json')

data = json.load(retailers)

print(data)
print(type(data))
print(type(data['retailers']))

for x in data['retailers']:
    print(x['name'] + " - " + x['city'] + ", " + x['country'] + " - " + "ID: " + x['uUID'])

## import json med pandas

df = pd.read_json('../case-2-1/gubi-retailers.json')

print(df)

## import excel med pandas

df2 = pd.read_excel('../case-2-1/GUBI_EU_Pricelist_march_2022.xlsx', sheet_name='Master data EU')

print(df2)

## import json med json (igen)

retailers1 = open('../case-2-1/gubi-retailers.json')

data1 = json.load(retailers1)

retailerList = []

for x in data1['retailers']:
    row = (x['name'], x['country'], x['city'], x['websiteLink'], x['uUID'])
    retailerList.append(tuple(row))