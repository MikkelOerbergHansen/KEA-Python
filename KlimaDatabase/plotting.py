## https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html

## https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.bar.html



import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import figure


'''
# open the file
xlsx = pd.read_excel("KlimaDatabase/static/Results_FINAL_20210201v4.xlsx", engine = "openpyxl", sheet_name = "Ra_500food")


df = pd.DataFrame(xlsx, columns= ['DSK Kategori', "Total kg CO2-eq/kg"])[0:500]   #  to enkelte søjler : make sure no empty cells
print(df)


print(df["Total kg CO2-eq/kg"]) ### single coloumn
#print(list(df["Total kg CO2-eq/kg"]))
CO2 = list(df["Total kg CO2-eq/kg"])  # værdierne kan hives ud i en enkelt liste

'''

#############################################################################################################


'''

print()
print("Nogle min / max / mean beregninger")
print("===============================")


print(max(CO2)) # max value
print(min(CO2)) # min  value

print(max(CO2) == df["Total kg CO2-eq/kg"].max())  ## to forskellige måder at beregne max / min  ( et tjek af at de er ens)

print(df["Total kg CO2-eq/kg"].mean())  # mean

'''
##############################################################################################################

'''
print()
print("Grouped averages")
print("===============================")



averageTable=df.groupby("DSK Kategori").mean() ### brug indeks til at subsette tabellen 
'''

################################################################################################################



'''

print(averageTable)



print(averageTable.min())  # Grøntsager udler mindst CO2
print(averageTable.max())  # Kød/fjerkræ udleder mest CO2


'''

#print(averageTable.sort_values("Total kg CO2-eq/kg")) ## sorteret liste



#####################
# PLOTS 
#####################

'''

averageTable.plot.bar(y="Total kg CO2-eq/kg")
#plt.tight_layout() ### stopper cut of i bunden men fucker selve grafen. nogle labels er meget lange
plt.savefig('KlimaDatabase/static/barplot_AverageCO2.png')
#plt.show()    ### plottet bliver cuttet i bunden

#plt.close()

# print(averageTable.index)  # måske kan man hive kategorier ud på denne måde

'''

#######################
# PLOTS MatplotLIb
#######################

'''

AverageCO2 = list(averageTable["Total kg CO2-eq/kg"])


##### skab liste med de 13 kategorier
KategoriListe = list(averageTable.index)

f, ax = plt.subplots(1)
plt.bar(KategoriListe, AverageCO2)
plt.xticks(rotation=90)
plt.tight_layout()



f, ax = plt.subplots(1)
plt.barh(KategoriListe, AverageCO2) ## barh laver et vertical bar plot istedet for bar der laver et horizontalt
plt.tight_layout()
plt.show() 
plt.close()

'''


####################################################################
##
## bar plot indenfor en enket kategori 
##
####################################################################

xlsx = pd.read_excel("KlimaDatabase/static/Results_FINAL_20210201v4.xlsx", engine = "openpyxl", sheet_name = "Ra_500food")


df = pd.DataFrame(xlsx, columns= ['DSK Kategori', "Navn", "Total kg CO2-eq/kg"])[0:500]   #  tre enkelte søjler : make sure no empty cells
print(df)

### create subset så vi kun kigger på kød 
køddf = df.loc[df["DSK Kategori"]=="Kød/fjerkræ"]
køddf20= køddf.loc[køddf["Total kg CO2-eq/kg"] >= 20]
print(køddf20)


KødAverage = køddf.groupby("Navn").mean()   #### kiges der på antal rækker ser det ud som om at der kun er en enkelt observation for hvert navn
print(KødAverage)                             ## det giver derfor ikke rigtig mening at tage average                   

køddf20Average = køddf20.groupby("Navn").mean()

mitplot = køddf20Average.sort_values("Total kg CO2-eq/kg").plot.barh(y="Total kg CO2-eq/kg")
plt.setp(mitplot.get_yticklabels(), horizontalalignment='right', fontsize=8)
plt.tight_layout()
plt.show() 

#averageTable=df.groupby(["DSK Kategori", "Navn"]).mean()  # average b multiple groups
#with pd.option_context('display.max_rows', None, 'display.max_columns', None): ####viser hele tabellen
    #print(averageTable)


