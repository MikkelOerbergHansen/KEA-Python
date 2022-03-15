## https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

## https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html


from turtle import width
import pandas as pd
import matplotlib.pyplot as plt


# open the file
xlsx = pd.read_excel("KlimaDatabase/static/Results_FINAL_20210201v4.xlsx", engine = "openpyxl", sheet_name = "Ra_500food")


df = pd.DataFrame(xlsx, columns= ['DSK Kategori', "Total kg CO2-eq/kg"])[0:500]   #  to enkelte søjler : make sure no empty cells
print(df)


print(df["Total kg CO2-eq/kg"]) ### single coloumn
#print(list(df["Total kg CO2-eq/kg"]))
CO2 = list(df["Total kg CO2-eq/kg"])  # værdierne kan hives ud i en enkelt liste

'''

print()
print("Nogle min / max / mean beregninger")
print("===============================")


print(max(CO2)) # max value
print(min(CO2)) # min  value

print(max(CO2) == df["Total kg CO2-eq/kg"].max())  ## to forskellige måder at beregne max / min  ( et tjek af at de er ens)

print(df["Total kg CO2-eq/kg"].mean())  # mean

'''

print()
print("Grouped averages")
print("===============================")



averageTable=df.groupby("DSK Kategori").mean() ### brug indeks til at subsette tabellen 

'''

print(averageTable)



print(averageTable.min())  # Grøntsager udler mindst CO2
print(averageTable.max())  # Kød/fjerkræ udleder mest CO2


'''

print(averageTable.sort_values("Total kg CO2-eq/kg")) ## sorteret liste



#####################
# PLOTS 
#####################



averageTable.plot.bar(y="Total kg CO2-eq/kg")
#plt.tight_layout() ### stopper cut of i bunden men fucker selve grafen. nogle labels er meget lange
plt.savefig('KlimaDatabase/static/barplot_AverageCO2.png')
#plt.show()    ### plottet bliver cuttet i bunden

plt.close()

# print(averageTable.index)  # måske kan man hive kategorier ud på denne måde

#######################
# PLOTS MatplotLIb
#######################

AverageCO2 = list(averageTable["Total kg CO2-eq/kg"])


##### skab liste med de 13 kategorier
KategoriListe = list(set(list(df['DSK Kategori']))) #### en lang liste med kategorier konverteres til list
                                            ### set() konverter til en mængde og finder dermed unique 
                                            ### indgange. settet konverteres tilbage til en liste



fig = plt.figure()
plt.bar(AverageCO2)
plt.show() 


