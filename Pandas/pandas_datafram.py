import numpy as np 
import pandas as pd 
d1=[148,"Preethi",21,12423]
d2=[111,"Srilatha",21,12423]
d3=[128,"Rohith",21,12423]
d=[d1,d2,d3]
print(pd.DataFrame(d,columns=["Rolno","Name","age","PayAmt"]))
dic1={"id":[136,137,148],"Age":[20,21,20],"Gender":['F','F','F']}
pd.DataFrame(dic1)
print(pd.DataFrame(dic1))
dic2={"id":[136,137,148],"Age":[20,21,20],"BP":[1,2,3]}
df=pd.DataFrame(dic2)
print(df)
print(df.sum(axis=1))
df["Sum"]=df.sum(axis=1)
#df['Sum1'] = df.iloc[: , [0, 1]].sum(axis=1)
print(df)
ind2=[sum(dic2['id']),sum(dic2['Age']),sum(dic2['BP'])]
df1=pd.DataFrame(dic2,ind2)
print(df1)
