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

df2 = pd.read_excel('Semester_2/dag1/GUBI_EU_Pricelist_march_2022.xlsx', sheet_name='Master data EU', usecols = "A, C, D, L, BJ")


#print(df2)
mytable = df2.values.tolist()
for i in range(0,2):
    print(mytable[i])

productList= []

for i in range(0, len(mytable)):
    row = (mytable[i][0], mytable[i][1], mytable[i][2], mytable[i][3], mytable[i][4] )
    productList.append(tuple(row))

print(productList[1])




#### database

import sqlite3

drop_table = """DROP TABLE IF EXISTS Products"""

create_table = """CREATE TABLE Products (
                        id INTEGER PRIMARY  KEY AUTOINCREMENT,
                        itemNO INTEGER NOT NULL,
                        modelNO INTEGER NOT NULL,
                        name TEXT NOT NULL,
                        category TEXT NOT NULL,
                        pris TEXT NOT NULL
                        );
                        """



with sqlite3.connect('Semester_2/dag1/Products.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)



    for r in productList:
        cur.execute("INSERT INTO Products (itemNO, modelNO, name, category, pris) VALUES (?,?,?,?,?);", 
                (r[0], r[1], r[2], r[3], r[4]))


cur.close()
connection.close()














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





class Retailers:
    def __init__(self, uid, name, country, city, websiteLink, uuid):
        self.uid = uid
        self.name = name
        self.country = country
        self.city = city
        self.websiteLink = websiteLink
        self.uuid = uuid



with sqlite3.connect("Semester_2/dag1/retailers.db") as connection:
    cursor = connection.cursor()
    query = "SELECT * FROM retailers;"
    retailers = cursor.execute(query)

retailObjects = []
for d in retailers:
    retailer = Retailers(d[0], d[1], d[2], d[3], d[4], d[5])
    retailObjects.append(retailer)

#print(retailObjects)
'''
for i in range(0,len(retailObjects)):
    print("===================")
    print("{} {} {} {} {} {}".format(retailObjects[i].uid, retailObjects[i].name, retailObjects[i].country, retailObjects[i].city,
                                    retailObjects[i].websiteLink, retailObjects[i].uuid))

'''