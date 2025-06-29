import pandas as pd
path=r"D:\python\my_code\#pandas1\raw_dataset.csv"
df=pd.read_csv(path)
i=df.dropna(subset=['email'])
df=df[df['age']>0]
#df=df[df['email'].str.contains('@')& df['email'].str.contains('.')]
df = df[df['email'].str.contains(r'^[\w\.-]+@[\w\.-]+\.\w+$', na=False)]
df.drop_duplicates(inplace=True)
df['join_date']=pd.to_datetime(df['join_date'],errors='coerce')
df.dropna(subset=['join_date'],inplace=True)
df.to_csv(r"D:\python\my_code\cleaned_dataset.csv", index=False)