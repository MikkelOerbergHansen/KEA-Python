


import pandas as pd

# open the file
xlsx = pd.read_excel("KlimaDatabase/static/Results_FINAL_20210201v4.xlsx", engine = "openpyxl", sheet_name = "Ra_500food")


df = pd.DataFrame(xlsx, columns= ['DSK Kategori'])[1:501]   # enkelt søjle
print (df)








