
from statistics import mean
import pandas as pd 
def getMonth(s):
  return s.split("-")[1]
def getYear(s):
    return s.split("-")[1]
def getYearMonth(s):
  return s.split("/")[0]+"-"+s.split("/")[2]
def stand_dev(data):
    d=pd.read_csv(data)
    return d.std()
def stand_dev_col(data,col):
    d=pd.read_csv(data)
    return d[col].std()
def mean_col(data,col):
    d=pd.read_csv(data)
    return d[col].mean()
def coeff_of_variance(data,col):
    d=pd.read_csv(data)
    return d[col].std()/d[col].mean()

data="finance_data.csv"
df=pd.read_csv(data)
print(stand_dev(data))
print("Mean of Open : ",mean_col(data,'Open'))
print("Standard Deviation of Open  : ",stand_dev_col(data,'Open'))
print("Mean of High : ",mean_col(data,'High'))
print("Standard Deviation of High  : ",stand_dev_col(data,'High'))
#print("COEFF OF VAR  FOR OPEN : ",coeff_of_variance(data,'Open'))
d={}
for i in df.columns:
    if(i not in ['Date']):
        print("Coefficient of Variance of ",i," is ",coeff_of_variance(data,i))
        d[i]=coeff_of_variance(data,i)
t=(d['Open']-d['Close'])*100/d['Open']
print(t)

df1 = pd.DataFrame(df, columns = ['Date','Open','Close'])
df['Date']= pd.to_datetime(df['Date']) 
r=df.groupby([df['Date'].dt.year, df['Date'].dt.month]).agg({'Open': ['mean', 'std'],'Close': ['mean', 'std']})
print(r)
r['covar_Open']=r['Open']['std']/r['Open']['mean']
r['covar_CLose']=r['Close']['std']/r['Close']['mean']
r['per_diff']=(r['covar_CLose']-r['covar_Open'])*100/r['covar_CLose']
print(r)
print("Minimum covariance ")
print()
print(r[r['per_diff']==min(r['per_diff'])])
print()
print("Maximum Covariance ")
print()
print(r[r['per_diff']==max(r['per_diff'])])
