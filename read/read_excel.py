import pandas as pd
filename = '통합 문서1.xlsx'
df_excel = pd.read_excel(filename)

name = df_excel.loc[0][1]
    

