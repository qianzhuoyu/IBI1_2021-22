import os
import pandas as pd  # import the .csv file works
import matplotlib.pyplot as plt  # tools to draw plots
import numpy as np

print(os.getcwd)
print(os.listdir)
covid_data = pd.read_csv("full_data(2).csv")  # read the .csv file
print(covid_data.iloc[9:20, 0:4:2])  # show the first and third columns from rows 10-20
my_row = []
for i in range(0, 7996):  # select all rows corresponding to Afghanistan
    if covid_data.iloc[i, 1] == "Afghanistan":
        my_row.append(True)
    else:
        my_row.append(False)
print(covid_data.loc[my_row, "total_cases"])  # show "total_cases" for all rows corresponding to Afghanistan
my_row1 = []
for i in range(0, 7996):  # use the same way to select all rows corresponding to China
    if covid_data.iloc[i, 1] == "China":
        my_row1.append(True)
    else:
        my_row1.append(False)
print(covid_data.loc[my_row1, "date"])
print(covid_data.loc[my_row1, "new_cases"])
print(covid_data.loc[my_row1, "new_deaths"])
china_new_cases = covid_data.loc[my_row1, "new_cases"]
china_new_deaths = covid_data.loc[my_row1, "new_deaths"]
china_dates = covid_data.loc[my_row1, "date"]
print(np.mean(china_new_cases))  # compute the mean number of new cases in China
print(np.mean(china_new_deaths))  # compute the mean number of new deaths in China
plt.boxplot(china_new_cases,  # create a boxplot of new cases in China
            meanline=True,
            showmeans=True,
            showfliers=False)
plt.title('new cases in China')  # add a title
plt.ylabel('number')
plt.show()
plt.boxplot(china_new_deaths,  # create a boxplot of new deaths in China
            meanline=True,
            showmeans=True,
            showfliers=False)
plt.title('new deaths in China')
plt.ylabel('number')
plt.show()
plt.plot(china_dates, china_new_deaths, 'r+')  # create a plot of new deaths in China over time
plt.plot(china_dates, china_new_cases, 'bo')  # create a plot of new cases in China over time
plt.xticks(china_dates.iloc[0:len(china_dates):4], rotation=-30)  # change the X-axis annotation style
plt.xlabel('date')
plt.ylabel('number')
plt.title('new cases and new deaths in China')  # add a title
plt.legend(['china_new_cases', 'china_new_deaths'])  # add legends
plt.show()
my_row2 = []
for i in range(0, 7996):  # select all rows corresponding to Angola
    if covid_data.iloc[i, 1] == "Angola":
        my_row2.append(True)
    else:
        my_row2.append(False)
print(covid_data.loc[my_row2, "date"])
print(covid_data.loc[my_row2, "total_cases"])
print(covid_data.loc[my_row2, "total_deaths"])
Angola_total_cases = covid_data.loc[my_row2, "total_cases"]
Angola_total_deaths = covid_data.loc[my_row2, "total_deaths"]
Angola_dates = covid_data.loc[my_row2, "date"]
plt.plot(Angola_dates, Angola_total_deaths, 'ro')  # create a plot of new cases and new deaths in Angola over time
plt.plot(Angola_dates, Angola_total_cases, 'bo')
plt.xticks(Angola_dates.iloc[0:len(Angola_dates)], rotation=-30)  # change the X-axis annotation style
plt.xlabel('date')
plt.ylabel('number')
plt.title('total cases and total deaths in Angola')
plt.legend(['Angola_total_cases', 'Angola_total_deaths'])
plt.show()
