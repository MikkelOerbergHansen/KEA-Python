## https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html


import pandas as pd

# open the file
xlsx = pd.read_excel("KlimaDatabase/static/Results_FINAL_20210201v4.xlsx", engine = "openpyxl", sheet_name = "Ra_500food")


df = pd.DataFrame(xlsx, columns= ['DSK Kategori', "Total kg CO2-eq/kg"])[1:500]   #  to enkelte søjler : make sure no empty cells
#print(df)


print(df["Total kg CO2-eq/kg"]) ### single coloumn
#print(list(df["Total kg CO2-eq/kg"]))
CO2 = list(df["Total kg CO2-eq/kg"])  # værdierne kan hives ud i en enkelt liste

print(max(CO2)) # max value
print(min(CO2)) # min  value

print(max(CO2) == df["Total kg CO2-eq/kg"].max())  ## to forskellige måder at beregne max / min  ( et tjek af at de er ens)

print(df["Total kg CO2-eq/kg"].mean())  # mean

averageTable=df.groupby("DSK Kategori").mean()[1:14] ### brug indeks til at subsette tabellen 

print(averageTable)

print(averageTable.min())  # Grøntsager udler mindst CO2
print(averageTable.max())  # Kød/fjerkræ udleder mest CO2

print(averageTable.sort_values("Total kg CO2-eq/kg")) ## sorteret liste