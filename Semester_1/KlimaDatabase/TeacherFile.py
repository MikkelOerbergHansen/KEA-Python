import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

df = pd.read_excel('Semester_1/KlimaDatabase/static/Results_FINAL_20210201v4.xlsx',engine = "openpyxl", sheet_name='Ra_500food', usecols="D,E,K,M")

print(df.groupby("DSK Category").describe())
print(df.groupby(["DSK Category"]).groups)

grouped = df.groupby(["DSK Category"])
print(grouped)

for name, group in grouped:
    print(name)
    print(group)
    print("")

print("Vegetables")
print(grouped.get_group("Vegetables"))

print("")
print("Sorted by transport")
sorted_df = df.sort_values(by="Transport", ascending=False).head(5)

print(sorted_df)

print("")
print("Sorted by total")
sorted_df2 = df.sort_values(by="Total kg CO2-eq/kg", ascending=False).head(5)

print(sorted_df2)

def sortedBy(column):
    print("")
    print("Sorted by {}".format(column))
    print("")
    sorted_frame_head = df.sort_values(by=column, ascending=False).head(5)
    print(sorted_frame_head)







def sortedByGroup(column, group1):
    print("")
    print("Sorted by {} and group {}".format(column, group1))
    print("")
    grouped_sort = df.groupby(["DSK Category"]).get_group(group1).sort_values(by=column, ascending=False)
    print(grouped_sort)

sortedBy("Transport")
sortedBy("Total kg CO2-eq/kg")

sortedByGroup("Transport", "Vegetables")
sortedByGroup("Total kg CO2-eq/kg", "Vegetables")

sortedByGroup("Transport", "Meat/poultry")
sortedByGroup("Total kg CO2-eq/kg", "Meat/poultry")

# Kategorier ind i en liste

print("\n")
print("*" * 50)
print("\n")

groupList = df.groupby(["DSK Category"]) # ["DSK Category"].apply(list)

print(groupList.groups.keys())

print(list(groupList.groups.keys()))

print("\n")
print("*" * 50)
print("\n")

for c in groupList.groups: 
    print(c)

# Fra DataFrame til List med tolist()

print("\n")
print("*" * 50)
print("\n")

ls = df.values.tolist()
print(ls)

print("\n")
print("*" * 50)
print("\n")

# list hvor hver indeks repræsenterer en kolonne
ls = []
for col in df.columns:
    # brug tolist() fra series til list
    col_ls = df[col].tolist()
    # append kolonne list til listen ls
    ls.append(col_ls)
# print listen ls
print(ls)

print("\n")
print("*" * 50)
print("\n")

# list fra en DataFrame ved at iterere gennem rækkerne
ls = []
# iterere gennem rækkerne
for i, row in df.iterrows():
    # lav en liste som repræsenterer rækkerne i dataframe
    row_ls = [row['Name'], row['DSK Category'], row['Transport'], row['Total kg CO2-eq/kg']]
    # append hver række med en liste ind i listen ls
    ls.append(row_ls)
    
print(ls)

print("\n")
print("*" * 50)
print("\n")