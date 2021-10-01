import numpy as np 
import pandas as pd 

ind=['Rollno','Name','Age','Gender']
a=['B18CS101','Avanthika',20,'F']
b=['B18CS148','Kolipaka Preethi',21,'F']
np_array1=np.array(a)
np_array2=np.array(b)
pd1=pd.Series(np_array1,index=ind)
pd2=pd.Series(np_array2,index=ind)
#pd.concat([pd1, pd2], axis=1)
print(pd.concat([pd1, pd2], axis=1))
print(pd.concat([pd1, pd2], axis=1).reset_index())
#print(pd.concat([pd1, pd2], axis=0))
pd3=pd.DataFrame([ind,a,b])
print(pd3)

# Coverting Dictionary to pandas series
d={"id":148,"name":"Preethi","age":20,"status":True}
print(pd.Series(d))
print(d["status"])
#print(d["age"]+d["id"])