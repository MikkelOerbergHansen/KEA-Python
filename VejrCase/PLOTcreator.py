
from ExcelReader import ExcelReader
from matplotlib import pyplot as plt
from Målinger import Måling



################################################################################################################
################################################################################################################
##########
##########
##########                               PLots For KØBENHAVN
##########
##########
################################################################################################################
################################################################################################################
ExcelFilData = ExcelReader()
dataframe = ExcelFilData.prepareData("VejrCase/VejrDataKøbenhavn.csv")
del dataframe[0]

MålingerKBH =[]
for i in range(1, len(dataframe)):
        MålingerKBH.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

Tidspunkt = []
GlobalStråling = []
Rel_Fugtighed = []
Temperatur = []
Vindretning = []
Vindhastighed = []

# for loop for at fylde tomme lister op med data
for måling in MålingerKBH:
    Tidspunkt.append(måling.getAllMåling()[0])
    GlobalStråling.append(måling.getAllMåling()[1])
    Rel_Fugtighed.append(måling.getAllMåling()[2])
    Temperatur.append(måling.getAllMåling()[3])
    Vindretning.append(måling.getAllMåling()[4])
    Vindhastighed.append(måling.getAllMåling()[5])

for i in range(0, len(GlobalStråling)):
    GlobalStråling[i] = int(GlobalStråling[i])

for i in range(0, len(Rel_Fugtighed)):
    Rel_Fugtighed[i] = int(Rel_Fugtighed[i])

for i in range(0, len(Temperatur)):
    Temperatur[i] = Temperatur[i].replace(',', '.')
    Temperatur[i] = float(Temperatur[i])

for i in range(0, len(Vindretning)):
    Vindretning[i] = int(Vindretning[i])

for i in range(0, len(Vindhastighed)):
    Vindhastighed[i] = Vindhastighed[i].replace(',', '.')
    Vindhastighed[i] = float(Vindhastighed[i])



f, ax = plt.subplots(1)
ax.plot(Tidspunkt, GlobalStråling)
ax.set_ylim(ymin=0-5, ymax=max(GlobalStråling)+10)
ax.set_ylabel('GlobalStråling')
ax.set_xlabel('Tid')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(GlobalStråling), 200 ,max(GlobalStråling)]) 
ax.set_yticklabels([min(GlobalStråling), 200 ,max(GlobalStråling)]) 
ax.set_xticks(["22-02-2022 07:30:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 07:30:00", "24-01-2022 00:00:00"])                                   
plt.title("KBH Globalstråling")
plt.savefig('VejrCase/static/KBH_Globalstråling')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Rel_Fugtighed)
ax.set_ylim(ymin=0, ymax=max(Rel_Fugtighed)+10)
ax.set_ylabel('Relativ Fugtighed')
ax.set_xlabel('Tid')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Rel_Fugtighed) ,max(Rel_Fugtighed)]) 
ax.set_yticklabels([min(Rel_Fugtighed) ,max(Rel_Fugtighed)]) 
ax.set_xticks(["22-02-2022 07:30:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 07:30:00", "24-01-2022 00:00:00"])   
plt.title("KBH Rel_Fugtighed")
plt.savefig('VejrCase/static/KBH_Rel_Fugtighed')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Temperatur)
ax.set_ylim(ymin=min(Temperatur)-5, ymax=max(Temperatur)+10)
ax.set_ylabel('Temperatur')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Temperatur) ,max(Temperatur)]) 
ax.set_yticklabels([min(Temperatur) ,max(Temperatur)]) 
ax.set_xticks(["22-02-2022 07:30:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 07:30:00", "24-01-2022 00:00:00"])  
plt.title("KBH Temperatur")
plt.savefig('VejrCase/static/KBH_Temperatur')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Vindretning)
ax.set_ylim(ymin=min(Vindretning)-10, ymax=max(Vindretning)+10)
ax.set_ylabel('Vindretning')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Vindretning) ,max(Vindretning)]) 
ax.set_yticklabels([min(Vindretning) ,max(Vindretning)]) 
ax.set_xticks(["22-02-2022 07:30:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 07:30:00", "24-01-2022 00:00:00"])  
plt.title("KBH Vindretning")
plt.savefig('VejrCase/static/KBH_Vindretning')
plt.close()





f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Vindhastighed)
ax.set_ylim(ymin=min(Vindhastighed)-5, ymax=max(Vindhastighed)+10)
ax.set_ylabel('Vindhastighed')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Vindhastighed) ,max(Vindhastighed)]) 
ax.set_yticklabels([min(Vindhastighed) ,max(Vindhastighed)]) 
ax.set_xticks(["22-02-2022 07:30:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 07:30:00", "24-01-2022 00:00:00"]) 
plt.title("KBH Vindhastighed")
plt.savefig('VejrCase/static/KBH_Vindhastighed')
plt.close()






##########################################################################################################################
##########################################################################################################################
##
##
##                                               PLot for Odense
##
##
##########################################################################################################################
##########################################################################################################################


ExcelFilData = ExcelReader()
dataframe = ExcelFilData.prepareData("VejrCase/VejrDataOdense.csv")
del dataframe[0]



MålingerOD =[]
for i in range(1, len(dataframe)):
        MålingerOD.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

Tidspunkt = []
GlobalStråling = []
Rel_Fugtighed = []
Temperatur = []
Vindretning = []
Vindhastighed = []

# for loop for at fylde tomme lister op med data
for måling in MålingerOD:
    Tidspunkt.append(måling.getAllMåling()[0])
    GlobalStråling.append(måling.getAllMåling()[1])
    Rel_Fugtighed.append(måling.getAllMåling()[2])
    Temperatur.append(måling.getAllMåling()[3])
    Vindretning.append(måling.getAllMåling()[4])
    Vindhastighed.append(måling.getAllMåling()[5])


for i in range(0, len(GlobalStråling)):
    GlobalStråling[i] = int(GlobalStråling[i])

for i in range(0, len(Rel_Fugtighed)):
    Rel_Fugtighed[i] = int(Rel_Fugtighed[i])

for i in range(0, len(Temperatur)):
    Temperatur[i] = Temperatur[i].replace(',', '.')
    Temperatur[i] = float(Temperatur[i])

for i in range(0, len(Vindretning)):
    Vindretning[i] = int(Vindretning[i])

for i in range(0, len(Vindhastighed)):
    Vindhastighed[i] = Vindhastighed[i].replace(',', '.')
    Vindhastighed[i] = float(Vindhastighed[i])





f, ax = plt.subplots(1)
ax.plot(Tidspunkt, GlobalStråling)
ax.set_ylim(ymin=0-5, ymax=max(GlobalStråling)+10)
ax.set_ylabel('GlobalStråling')
ax.set_xlabel('Tid')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(GlobalStråling), 200 ,max(GlobalStråling)]) 
ax.set_yticklabels([min(GlobalStråling), 200 ,max(GlobalStråling)]) 
ax.set_xticks(["22-02-2022 10:00", "24-01-2022 00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00", "24-01-2022 00:00"])                                   
plt.title("Odense Globalstråling")
plt.savefig('VejrCase/static/OD_Globalstråling')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Rel_Fugtighed)
ax.set_ylim(ymin=0, ymax=max(Rel_Fugtighed)+10)
ax.set_ylabel('Relativ Fugtighed')
ax.set_xlabel('Tid')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Rel_Fugtighed) ,max(Rel_Fugtighed)]) 
ax.set_yticklabels([min(Rel_Fugtighed) ,max(Rel_Fugtighed)]) 
ax.set_xticks(["22-02-2022 10:00", "24-01-2022 00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00", "24-01-2022 00:00"])   
plt.title("Odense Rel_Fugtighed")
plt.savefig('VejrCase/static/OD_Rel_Fugtighed')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Temperatur)
ax.set_ylim(ymin=min(Temperatur)-5, ymax=max(Temperatur)+10)
ax.set_ylabel('Temperatur')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Temperatur) ,max(Temperatur)]) 
ax.set_yticklabels([min(Temperatur) ,max(Temperatur)]) 
ax.set_xticks(["22-02-2022 10:00", "24-01-2022 00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00", "24-01-2022 00:00"])  
plt.title("Odense Temperatur")
plt.savefig('VejrCase/static/OD_Temperatur')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Vindretning)
ax.set_ylim(ymin=min(Vindretning)-10, ymax=max(Vindretning)+10)
ax.set_ylabel('Vindretning')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Vindretning) ,max(Vindretning)]) 
ax.set_yticklabels([min(Vindretning) ,max(Vindretning)]) 
ax.set_xticks(["22-02-2022 10:00", "24-01-2022 00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00", "24-01-2022 00:00"])  
plt.title("Odense Vindretning")
plt.savefig('VejrCase/static/OD_Vindretning')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Vindhastighed)
ax.set_ylim(ymin=min(Vindhastighed)-5, ymax=max(Vindhastighed)+10)
ax.set_ylabel('Vindhastighed')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Vindhastighed) ,max(Vindhastighed)]) 
ax.set_yticklabels([min(Vindhastighed) ,max(Vindhastighed)]) 
ax.set_xticks(["22-02-2022 10:00", "24-01-2022 00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00", "24-01-2022 00:00"]) 
plt.title("Odense Vindhastighed")
plt.savefig('VejrCase/static/OD_Vindhastighed')
plt.close()


###############################################################################################################################
###############################################################################################################################
##
##
##                                                  PLOTS for Aalborg
##
##
###############################################################################################################################
###############################################################################################################################



ExcelFilData = ExcelReader()
dataframe = ExcelFilData.prepareData("VejrCase/VejrDataAalborg.csv")
del dataframe[0]



MålingerAA =[]
for i in range(1, len(dataframe)):
        MålingerAA.append(Måling(dataframe[i][0],dataframe[i][1],dataframe[i][2],dataframe[i][3],dataframe[i][4], dataframe[i][5]))

Tidspunkt = []
GlobalStråling = []
Rel_Fugtighed = []
Temperatur = []
Vindretning = []
Vindhastighed = []

# for loop for at fylde tomme lister op med data
for måling in MålingerAA:
    Tidspunkt.append(måling.getAllMåling()[0])
    GlobalStråling.append(måling.getAllMåling()[1])
    Rel_Fugtighed.append(måling.getAllMåling()[2])
    Temperatur.append(måling.getAllMåling()[3])
    Vindretning.append(måling.getAllMåling()[4])
    Vindhastighed.append(måling.getAllMåling()[5])


for i in range(0, len(GlobalStråling)):
    GlobalStråling[i] = int(GlobalStråling[i])

for i in range(0, len(Rel_Fugtighed)):
    Rel_Fugtighed[i] = int(Rel_Fugtighed[i])

for i in range(0, len(Temperatur)):
    Temperatur[i] = Temperatur[i].replace(',', '.')
    Temperatur[i] = float(Temperatur[i])

for i in range(0, len(Vindretning)):
    Vindretning[i] = int(Vindretning[i])

for i in range(0, len(Vindhastighed)):
    Vindhastighed[i] = Vindhastighed[i].replace(',', '.')
    Vindhastighed[i] = float(Vindhastighed[i])



f, ax = plt.subplots(1)
ax.plot(Tidspunkt, GlobalStråling)
ax.set_ylim(ymin=0-5, ymax=max(GlobalStråling)+10)
ax.set_ylabel('GlobalStråling')
ax.set_xlabel('Tid')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(GlobalStråling), 200 ,max(GlobalStråling)]) 
ax.set_yticklabels([min(GlobalStråling), 200 ,max(GlobalStråling)]) 
ax.set_xticks(["22-02-2022 10:00:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00:00", "24-01-2022 00:00:00"])                                   
plt.title("Aalborg Globalstråling")
plt.savefig('VejrCase/static/AA_Globalstråling')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Rel_Fugtighed)
ax.set_ylim(ymin=0, ymax=max(Rel_Fugtighed)+10)
ax.set_ylabel('Relativ Fugtighed')
ax.set_xlabel('Tid')
# Turn off tick labels
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Rel_Fugtighed) ,max(Rel_Fugtighed)]) 
ax.set_yticklabels([min(Rel_Fugtighed) ,max(Rel_Fugtighed)]) 
ax.set_xticks(["22-02-2022 10:00:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00:00", "24-01-2022 00:00:00"])   
plt.title("Aalborg Rel_Fugtighed")
plt.savefig('VejrCase/static/AA_Rel_Fugtighed')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Temperatur)
ax.set_ylim(ymin=min(Temperatur)-5, ymax=max(Temperatur)+10)
ax.set_ylabel('Temperatur')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Temperatur) ,max(Temperatur)]) 
ax.set_yticklabels([min(Temperatur) ,max(Temperatur)]) 
ax.set_xticks(["22-02-2022 10:00:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00:00", "24-01-2022 00:00:00"])  
plt.title("Aalborg Temperatur")
plt.savefig('VejrCase/static/AA_Temperatur')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Vindretning)
ax.set_ylim(ymin=min(Vindretning)-10, ymax=max(Vindretning)+10)
ax.set_ylabel('Vindretning')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Vindretning) ,max(Vindretning)]) 
ax.set_yticklabels([min(Vindretning) ,max(Vindretning)]) 
ax.set_xticks(["22-02-2022 10:00:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00:00", "24-01-2022 00:00:00"])  
plt.title("AalborgVindretning")
plt.savefig('VejrCase/static/AA_Vindretning')
plt.close()


f, ax = plt.subplots(1)
ax.plot(Tidspunkt, Vindhastighed)
ax.set_ylim(ymin=min(Vindhastighed)-5, ymax=max(Vindhastighed)+10)
ax.set_ylabel('Vindhastighed')
ax.set_xlabel('Tid')
ax.set_yticklabels([])
ax.set_xticklabels([]) 
ax.set_yticks([min(Vindhastighed) ,max(Vindhastighed)]) 
ax.set_yticklabels([min(Vindhastighed) ,max(Vindhastighed)]) 
ax.set_xticks(["22-02-2022 10:00:00", "24-01-2022 00:00:00"]) 
ax.set_xticklabels(["22-02-2022 10:00:00", "24-01-2022 00:00:00"]) 
plt.title("Aalborg Vindhastighed")
plt.savefig('VejrCase/static/AA_Vindhastighed')
plt.close()











