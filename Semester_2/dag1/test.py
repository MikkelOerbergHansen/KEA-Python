import pandas as pd


####
#### open csv file with python
####

xlsx = pd.read_excel("Semester_2/dag1/GUBI_EU_Pricelist_march_2022.xlsx", engine = "openpyxl", sheet_name = "Master data EU")
#print(xlsx)

mylist = []  ## mylist indeholder alle rækker fra excel filen som en liste af lister

df = pd.DataFrame(xlsx)
#print(df)

df = df.reset_index()  # make sure indexes pair with number of rows

for index, row in df.iterrows():
    mylist.append(row)

#print(mylist)

mylist2 = []            ### mylist2 indeholder 1 række fra excel filen
for i in range(0,1):
    for j in range(0,len(mylist[i])):
        mylist2.append(mylist[i][j])


#print(mylist2)




##### json fil
#####
import json

df = pd.read_json("Semester_2/dag1/gubi-retailers.json")

#print(df)


retailers1 = open("Semester_2/dag1/gubi-retailers.json", errors= "ignore")

data1 = json.load(retailers1)



retailerlist = []

for x in data1['retailers']:
    row = (x['name'], x['country'], x['city'], x['websiteLink'], x['uUID'])
    retailerlist.append(tuple(row))

print(retailerlist)



