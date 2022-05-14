# -*- coding: utf-8 -*-
"""
Created on Sat May 14 13:29:11 2022

@author: avidvans3
"""

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm
data=pd.read_csv('Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv')

# fig, ax = plt.subplots(figsize=(10,6))
# sns.heatmap(data.corr())
"This now applies to Alabama only. Will be extended to the rest of the US too.Examining link between education and obesity rates"

data=data[data['LocationAbbr'].str.contains("AL")==True]

data=data[data['Education'].str.contains("nan")==False]

data=data[data['Question'].str.contains("Percent of adults aged 18 years and older who have obesity")==True]



data1=data['YearStart']
data2=data['Data_Value']

data3=data['Education']

data3={'col1':data1,'col2':data2,'col3':data3}

data4=pd.DataFrame(data=data3)

data5=pd.get_dummies(data4)

from sklearn.linear_model import LinearRegression
model = LinearRegression()
data5.columns=['Year','Obesity','College grad','High school','Less than high school','Technical college']

X1=data5['College grad']
X2=data5['High school']
X3=data5['Less than high school']
X4=data5['Technical college']

X_=[X1,X2,X3,X4]

X=pd.concat(X_,axis=1)
Y=data5['Obesity']
ks = sm.OLS(Y, X)
ks_res =ks.fit()
ks_res.summary()
