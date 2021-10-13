# PROGRAM        : PLOTTING GRAPH FOR OPEN Vs CLOSE and HIGH Vs LOW USING MATPLOTLIB and Given FINANCE DATA
# PROGRAMMED BY  : KOLIPAKA PREETHI
# EMAIL ID       : b18cs148@kitsw.ac.in 
# DATE           : 13-OCT-2021
# PYTHON VERSION : 3.8
# CAVEATS        : None 
# LICENSE        : None 



from matplotlib import colors
import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

def calc_coeff1(x,y):
    X_mean = np.mean(x)
    Y_mean = np.mean(y)
    
    num = 0
    den = 0
    for i in range(len(x)):
        num += (x[i] - X_mean)*(y[i] - Y_mean)
        den += (x[i] - X_mean)**2
    m = num / den
    c = Y_mean - m*X_mean
    print("X mean:",X_mean)
    print("Standard Devaiation :  X  :",np.std(x)," Y :",np.std(y))
    return (c,m)
def calc_coeff(x,y):
    # N --> Num of Observations 
    N=np.size(x)
    # xm --> x mean ym--> y mean
    xm,ym=np.mean(x),np.mean(y)
    # Calculate standard Deviation values around x
    xystd=np.sum(y**x)-N*ym*ym 
    xxstd=np.sum(x**x)-N*xm*xm 
    # calculate regression coefficient 
    c=xystd/xxstd
    m=ym-c*xm
    return(m,c)

def calc_regression(x,y,b,xlab,ylab,title):
    plt.scatter(x,y,color="r",marker='o',s=20)
    predicted_y=b[0]+b[1]*x
    plt.title(title)
    plt.plot(x,predicted_y,color="g")
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.show()


df=pd.read_csv("finance_data.csv")
x1,y1=np.array(df['Open']),np.array(df['Close'])
x2,y2=np.array(df['High']),np.array(df['Low'])
t=calc_coeff1(x1,y1)
print("Regression Coeff for 1 st graph :",t[1])
t1=calc_coeff1(x2,y1)
print("Regression Coeff for 2 nd graph :",t1[1])
calc_regression(x1,y1,t,"Open","Close","Open Vs Close")
calc_regression(x2,y2,t1,"High","Low","High Vs Low")
