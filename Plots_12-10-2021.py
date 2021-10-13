# PROGRAM        : WORKING WITH PLOTTING GRAPH USING MATPLOTLIB
# DESCRIPTION    : 1. Plot a Graph for STandard Deviation for India and US in the Month of Jan And Feb
#                  2. Create a Chart for Fully Vaccinated people For India Vs US
#                  3. Create a Chart for Partially Vaccinated people For India Vs US
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 12-OCT-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None


import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 
import statistics as mode
from pandas.core.frame import DataFrame 

def getMonth(s):
  return s.split("/")[0]
def getday(s):
  return s.split("/")[1]
# Data Extraction 
df=pd.read_csv("country_vaccinations.csv")

# Vaccine Combinations being used 
from collections import Counter 

country_list =df['country'].unique()
print(country_list)

vaccine_typ=df['vaccines'].unique()
print(vaccine_typ)

vaccine_used=[]
for i in country_list:
    vaccine_used.append(df[df['country']==i]['vaccines'].mode(0))

print(vaccine_used)
vaccine_used=pd.Series(vaccine_used)
print(vaccine_used)
vaccine_mode=[]

for i in range(0,101):
    vaccine_mode.append(vaccine_used[i][0])
print("Vaccine Mode")
print(vaccine_mode)
words_to_count=(word for word in vaccine_mode if word[:1].isupper())
c=Counter(words_to_count)
print(c)

# Vaccination Count 
count=[]
name_of_vacc=[]
for i in range(0,19):
    count.append(c.most_common()[i][1])
    name_of_vacc.append(c.most_common()[i][0])


'''
df1['month']= df1['date'].apply(lambda x: getMonth(x))
df2['month']= df2['date'].apply(lambda x: getMonth(x))

df1['date']= pd.to_datetime(df['date'])
df2['date']= pd.to_datetime(df['date'])
'''




# STANDARD DEVIATION FOR THE MONTH OF JANUARY FOR USA AND INDIA
# 1. Standard Deviation for the month of Jan and Feb For India 
months=['January','Febrauary']
df['date']=pd.to_datetime(df['date'])
df['month']=df['date'].dt.month
r2=df.groupby(['country','month']).total_vaccinations.std()
ind,us=r2['India'],r2['United States']
plt.title("STandard Deviation In the Month ofJan and Feb For India")
plt.bar(months,[ind[1],ind[2]])
plt.xlabel("Month")
plt.ylabel("Standard Deviation")
plt.show()



# 1. Standard Deviation for the month of Jan and Feb For US

plt.title("STandard Deviation In the Month ofJan and Feb For India")
plt.bar(months,[us[1],us[2]])
plt.xlabel("Month")
plt.ylabel("Standard Deviation")
plt.show()


df1=pd.DataFrame(df[df['country']=='India'])
df2=pd.DataFrame(df[df['country']=='United States'])


df1['date']= pd.to_datetime(df1['date'])
df2['date']= pd.to_datetime(df2['date'])

# PARTIALLY VACCINATED 



plt.plot(df1['date'],df1['people_vaccinated'],'-r',label='India')
plt.plot(df2['date'],df2['people_vaccinated'],'-g',label='United States')
plt.title("PEOPLE PARTIALLY VACCINATED FOR US AND INDIA")
plt.xticks(rotation=45)
plt.xlabel("DATES")
plt.ylabel("NO OF PEOPLE PARTIALLY VACCINATED")
plt.legend(["India","United States"])
plt.show()



#   FULLY   VACCINATED

plt.plot(df1['date'],df1['people_fully_vaccinated'],linestyle='dashed')
plt.plot(df2['date'],df2['people_fully_vaccinated'])
plt.title("PEOPLE FULLY VACCINATED FOR US AND INDIA")
plt.xticks(rotation=45)
plt.xlabel("DATES")
plt.ylabel("NO OF PEOPLE FULLY VACCINATED")
plt.legend(["India","US"])
plt.show()
