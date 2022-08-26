# import moduler

import json
import pandas as pd

## import json med json

retailers = open('Semester_2/dag1/gubi-retailers.json',  errors= "ignore")

data = json.load(retailers)

#print(data)
#print(type(data))
#print(type(data['retailers']))

#for x in data['retailers']:
#    print(x['name'] + " - " + x['city'] + ", " + x['country'] + " - " + "ID: " + x['uUID'])

## import json med pandas

df = pd.read_json('Semester_2/dag1/gubi-retailers.json')

#print(df)

## import excel med pandas

df2 = pd.read_excel('Semester_2/dag1/GUBI_EU_Pricelist_march_2022.xlsx', sheet_name='Master data EU')

#print(df2)

## import json med json (igen)

retailers1 = open('Semester_2/dag1/gubi-retailers.json',  errors= "ignore")

data1 = json.load(retailers1)

retailerList = []

for x in data1['retailers']:
    row = (x['name'], x['country'], x['city'], x['websiteLink'], x['uUID'])
    retailerList.append(tuple(row))






##### database

import sqlite3

drop_table = """DROP TABLE IF EXISTS Retailers"""

create_table = """CREATE TABLE Retailers (
                        id INTEGER PRIMARY  KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        country TEXT NOT NULL,
                        city TEXT NOT NULL,
                        websiteLink TEXT NOT NULL,
                        uuid INTEGER NOT NULL
                        );
                        """



with sqlite3.connect('Semester_2/dag1/retailers.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)



for r in retailerList:
    cur.execute("INSERT INTO retailers (name, country, city, websiteLink, uuid) VALUES (?,?,?,?,?);", 
                (r[0], r[1], r[2], r[3], r[4]))


cur.close()
connection.close()