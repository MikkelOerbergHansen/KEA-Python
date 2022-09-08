






# import moduler
import pandas as pd



## import excel med pandas

df2 = pd.read_excel("Semester_2/dag1/GUBI_EU_Pricelist_march_2022.xlsx", sheet_name='Master data EU', usecols = "D")


#print(df2)
mytable = df2.values.tolist()
for i in range(0,2):
    print(mytable[i])

print(mytable)
produktNavnList= []

for i in range(0, len(mytable)):
    row = (mytable[i][0])
    produktNavnList.append(row)

print(produktNavnList[1])


#### database

import sqlite3

drop_table = """DROP TABLE IF EXISTS ProduktNavn"""

create_table = """CREATE TABLE ProduktNavn (
                        ProduktNavn_ID INTEGER PRIMARY  KEY AUTOINCREMENT,
                        ProduktNavn TEXT
                        );
                        """



with sqlite3.connect('Semester_2/dag1//ProduktNavn.db') as connection:
    cur = connection.cursor()
    cur.execute(drop_table)
    cur.execute(create_table)


    for r in produktNavnList:
            cur.execute("INSERT INTO ProduktNavn (ProduktNavn) VALUES (?);", 
                (r[0]))


cur.close()
connection.close()













































