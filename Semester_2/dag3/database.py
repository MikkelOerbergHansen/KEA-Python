import sqlite3
import json
import os
from urllib import response
#
#my_dir = os.path.dirname(__file__)
#json_file_path = os.path.join(my_dir, 'static/clever-locations.json')


cleverLokationer = open('Semester_2/dag3/static/clever-locations.json', errors= "ignore")

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


with sqlite3.connect('Semester_2/dag3/static/CleverLokationtest.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)

    for c in mycleverlokationer:
        cur.execute("INSERT INTO cleverLokationertest (Line1) VALUES (?);", 
                (c))




    #En INSERT INTO funktion til at tilføje en ny ladestanders postion
    cur.execute("INSERT INTO cleverLokationertest (Line1) VALUES (?);",
                (tuple(("min vej; min by",))))

    #En SELECT med WHERE hvor man henter data fra databasen med et givent id
    minladestander = cur.execute("SELECT * From cleverLokationertest WHERE id=1012;")

for d in minladestander:
    print(d[0])
    print(d[1])


# for at updatere en række i databasen med id nummer
with sqlite3.connect('Semester_2/dag3/static/CleverLokationtest.db') as connection:
    cur = connection.cursor()

    cur.execute("UPDATE cleverLokationertest SET Line1 = 'min vej2; min by2' WHERE id=1012;")
    
    #En SELECT med WHERE hvor man henter data fra databasen med et givent id
    minladestander2 = cur.execute("SELECT * From cleverLokationertest WHERE id=1012;")

for d in minladestander2:
    print(d[0])
    print(d[1])


with sqlite3.connect('Semester_2/dag3/static/CleverLokationtest.db') as connection:
    cur = connection.cursor()

    #En måde at slette en ladestander med et givent id
    cur.execute("DELETE FROM cleverLokationertest WHERE id=1012;")















