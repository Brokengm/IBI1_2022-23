#help from https://www.runoob.com/matplotlib/matplotlib-line.html
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C:/Users/dyq37/Desktop")
covid_data = pd.read_csv("full_data.csv")
print(covid_data.iloc[0:1000:100,1])
boolean=list()
for i in covid_data.loc[:,"location"]:
    if i == "Afghanistan":
        boolean.append(True)
    else:
        boolean.append(False)
print(covid_data.loc[boolean,"total_cases"])
boolean=list()
for i in covid_data.loc[:,"date"]:
    if i == "2020-03-31":
        boolean.append(True)
    else:
        boolean.append(False)
a=covid_data.loc[boolean,"new_cases"]
b=covid_data.loc[boolean,"new_deaths"]
print(np.mean(a))
print(np.mean(b))
world_dates=covid_data.loc[:,"date"]
world_new_cases=covid_data.loc[:,"new_cases"]
world_new_deaths=covid_data.loc[:,"new_deaths"]
plt.plot(world_dates, world_new_cases, 'bo')

plt.plot(world_dates, world_new_deaths,'r+')
plt.xticks(world_dates.iloc[0:len(world_dates):4],fontsize=5,rotation=-90)
plt.show()
boolean=list()
for i in covid_data.loc[:,"location"]:  # here the code starts
    if i == "United Kingdom":
        boolean.append(True)
    else:
        boolean.append(False)
u=covid_data.loc[boolean,"new_cases"]
k=covid_data.loc[boolean,"total_cases"]
uk_dates=covid_data.loc[boolean,"date"]
plt.plot(uk_dates,u,'ro')
plt.plot(uk_dates,k,'b+')
plt.xticks(uk_dates,fontsize=5,rotation=-90)
plt.show()
