# PROGRAM        : EXTRACTING TOTAL VACCINES ALONG WITH INCREASE PERCENTAGE FROM COVID VACCINATIONS 
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 04-10-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 

import pandas as pd
import numpy as np
from statistics import mode 
import dateutil

def getMonth(s):
  return s.split("/")[0]


def getYearMonth(s):
  return s.split("/")[0]+"-"+s.split("/")[2]

def getpercent(x,y):
    return ((x-y)*100)/x

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
print("---------------country------------------------")
for i in range(0,102):
    #print(vaccine_used[i][0])
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
print("Most WIDELY COMMONLY USED",mode(vaccine_mode))

print("Vaccines used in India",df[df['country']=='India']['vaccines'].mode(0)[0])

# People Vaccinated 
people_vacc=[]
for i in country_list:
    people_vacc.append(df[df['country']==i]['people_vaccinated'].sum())
countries_unvacc=[]
#print(people_vacc)
for i in range(0,102):
    if(people_vacc[i]==0):
        countries_unvacc.append(country_list[i])
print(countries_unvacc)

# Total Vaccines administered in india 
india_vacc=df[df['country']=='India']['total_vaccinations'].sum()
us_vacc=df[df['country']=='United States']['total_vaccinations'].sum()
print("VACCINE---",pd.Series(india_vacc))
print("India Vaccinated  ",india_vacc)
print("US Vaccinated ",us_vacc)

'''
#########
df['date']= pd.to_datetime(df['date']) 
print("\nYear wise Month wise ")
result = df.groupby([df['date'].dt.year, df['date'].dt.month]).agg({'total_vaccinations':sum})
print(result)'''

# Getting subset of dataframe which is india
DF=df[df['country']=='India']
Df=df[df['country']=='United States']
df1 = pd.DataFrame(DF, columns = ['date','country','total_vaccinations'])
df1['month']= df1['date'].apply(lambda x: getMonth(x))
#print(df)
df2 = pd.DataFrame(Df, columns = ['date','country','total_vaccinations'])
df2['month']= df2['date'].apply(lambda x: getMonth(x))
result1 = df1.groupby(['month']).agg({'total_vaccinations':sum})
result2 = df2.groupby(['month']).agg({'total_vaccinations':sum})
#print(df1.groupby(['month']).groups.keys())
print(result1)
print(result2)
r1,c1=result1.shape 
r2,c2=result2.shape 
print(r1,r2)

# India Vaccines count for more months
for _,i in result1.iterrows():
    for j,t in result2.iterrows():
        if(_==j):
            if(i[0]>t[0]):
                print("Month : ",_,"Percent inc in India over US ",getpercent(i[0],t[0]))
            else:
                #print(_,j,i[0],t[0])
                print("Month : ",_,"Percent inc in US over India ",getpercent(t[0],i[0]))


'''
if(r1>r2):
    for _,i in result1.iterrows():
        for j,t in result2.iterrows():
            if(_==j):
                if(i[0]>t[0]):
                    print("Month : ",_,"Percent inc in India over US ",getpercent(i[0],t[0]))
                else:
                    #print(_,j,i[0],t[0])
                    print("Month : ",_,"Percent inc in US over India ",getpercent(t[0],i[0]))

else:
    for _,i in result1.iterrows():
        for j,t in result2.iterrows():
            if(_==j):
                if(i[0]>t[0]):
                    print("Month : ",_,"Percent inc in India over US ",getpercent(i[0],t[0]))
                else:
                    #print(_,j,i[0],t[0])
                    print("Month : ",_,"Percent inc in US over India ",getpercent(t[0],i[0]))'''
