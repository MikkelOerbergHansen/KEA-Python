import sqlite3
import json
import os
from urllib import response
#
#my_dir = os.path.dirname(__file__)
#json_file_path = os.path.join(my_dir, 'static/clever-locations.json')


cleverLokationer = open('Semester_2/Clever_project_on_the_side/static/clever-locations.json', errors= "ignore")

data1 = json.load(cleverLokationer)

cleverLokationer = []

keylist = list(data1.keys())





for key in keylist:
    row = (data1[key]['address']['line1'], data1[key]['address']['line2'])
    cleverLokationer.append(row)
    

mycleverlokationer = []
for row in cleverLokationer:
    newaddress = (row[0] +"; " + row[1],)
    mycleverlokationer.append(tuple(newaddress))



##### database

drop_table = """DROP TABLE IF EXISTS cleverLokationertest"""

create_table = """CREATE TABLE cleverLokationertest (
                        id INTEGER PRIMARY  KEY AUTOINCREMENT,
                        Line1 TEXT NOT NULL
                        );
                        """


with sqlite3.connect('Semester_2/Clever_project_on_the_side/static/CleverLokationtest.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)

    for c in mycleverlokationer:
        cur.execute("INSERT INTO cleverLokationertest (Line1) VALUES (?);", 
                (c))