# -*- coding: utf-8 -*-
"""
Created on Wed May 11 14:32:09 2022

@author: avidvans3
"""

import pandas as pd
import numpy as np
import os
from sklearn.model_selection import train_test_split
from sklearn import linear_model
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv('Nutrition__Physical_Activity__and_Obesity_-_Behavioral_Risk_Factor_Surveillance_System.csv')

# fig, ax = plt.subplots(figsize=(10,6))
# sns.heatmap(data.corr())
"This now applies to Alabama only. Will be extended to the rest of the US too"

data=data[data['LocationAbbr'].str.contains("PA")==True]

# data=data[data['Education'].str.contains("nan")==False]


data=data[data['Topic'].str.contains("Obesity / Weight Status")==True]
data=data[data['Question'].str.contains("Percent of adults aged 18 years and older who have obesity")==True]
data=data[data['Stratification1'].str.contains("Total")==True]


data1=data['YearStart']
data2=data['Data_Value']

data3={'col1':data1,'col2':data2}

data4=pd.DataFrame(data=data3)
m, b = np.polyfit(data4['col1'], data4['col2'], 1)

plt.scatter(data4['col1'],data4['col2']),plt.title("Obesity Rates in AL Yearwise"),plt.xlabel('Year'),plt.ylabel('Obesity rate in %')

plt.plot(data4['col1'],m*data4['col1']+b)


# data=data[data['LocationDesc'].str.contains("National")==True]
# data5=data[data['Topic'].str.contains("Obesity / Weight Status")==True]
# data6=data[data['Topic'].str.contains("Physical Activity - Behavior")==True]

# data7=data6[data6['Question'].str.contains("Percent of adults who achieve at least 150 minutes a week of moderate-intensity aerobic physical activity or 75 minutes a week of vigorous-intensity aerobic activity (or an equivalent combination)")==True]
