## Import Required library
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn import metrics
import matplotlib.pyplot as plt
import seaborn as sns
from wcmatch import fnmatch

## Working Directory
cwd = os.getcwd()
print(cwd)

## Reading the csv file
df = pd.DataFrame()
df = pd.read_csv('DSI_kickstarterscrape_dataset1.csv')
print(df.head())

## Dimension
print(df.shape)
print(df.dtypes)

## Removing unwanted rows:
print(df.status.value_counts())

df.drop(df.loc[df['status']=='live'].index, inplace=True)
df.drop(df.loc[df['status']=='canceled'].index, inplace=True)
df.drop(df.loc[df['status']=='suspended'].index, inplace=True)

## Spliting the column into two:
new = df["location"].str.split(", ", n = 1, expand = True)
df["city"]= new[0]
df["state"]= new[1]
df.drop(columns =["location"], inplace = True)

print(df.shape)

##Filtering states
for each in df.state:
    if (fnmatch.fnmatch(str(each),'??')) == False:
        df.drop(df.loc[df['state']== each].index, inplace=True)

print(df.shape)

## Checking for missing values:
print(df.isnull().sum())
df = df.dropna()
print(df.isnull().sum())

print(df.shape)

df.to_csv('Final_123.csv')

## Finding Main Category, Sub Category and number of states:
print(len(df.category.unique()), "Main categories\n")
print(df.category.value_counts())
print(len(df.subcategory.unique()), "sub categories\n")
print(df.subcategory.value_counts())
print(len(df.state.unique()), "Number of states\n")
print(df.state.value_counts())

### Data Visualisation:

## Exploratory Data Analysis:

## Total Number of projects:
project = df.status.value_counts()
print('Total Successful project (%):',project[0])
print('Total Failed project (%):',project[1])

## Projects ratio in %
suc_porp = project[0]/(project[0]+project[1])
fail_prop = project[1]/(project[0]+project[1])
print('Successful project (%):',suc_porp*100)
print('Failed project (%):',fail_prop*100)

## Total goals for Projects:
goal = df.groupby('status').goal.sum()
print('Successful project goal:',goal[1])
print('Failed project goal:',goal[0])

## Average for project goal:
suc_goal_avg = goal[1]/project[0]
fail_goal_avg = goal[0]/project[1]
print('Successful project goal average:',suc_goal_avg)
print('Failed project goal average:',fail_goal_avg)

## Total Pledge for Project:
pledge = df.groupby('status').pledged.sum()
print('Successful project pledge:',pledge[1])
print('Failed project pledge:',pledge[0])

## Average for project pledge:
suc_pledge_avg = pledge[1]/project[0]
fail_pledge_avg = pledge[0]/project[1]
print('Successful project pledge average:',suc_pledge_avg)
print('Failed project pledge average:',fail_pledge_avg)

## Goal vs Pledge in %
suc_gp = suc_pledge_avg/suc_goal_avg
fail_gp = fail_pledge_avg /fail_goal_avg
print('Successful project pledge average:',suc_gp*100)
print('Failed project pledge average:',fail_gp*100)

## Average for project updates:
update = pledge = df.groupby('status').updates.sum()
suc_update_avg = update[1]/project[0]
fail_update_avg = update[0]/project[1]
print('Successful project update average:',suc_update_avg)
print('Failed project update average:',fail_update_avg)

## Average for project duration:
duration = pledge = df.groupby('status').duration.sum()
suc_dur_avg = duration[1]/project[0]
fail_dur_avg = duration[0]/project[1]
print('Successful project duration average:',suc_dur_avg)
print('Failed project duration average:',fail_dur_avg)

## Average for project backers:
backers = pledge = df.groupby('status').backers.sum()
suc_bac_avg = backers[1]/project[0]
fail_bac_avg = backers[0]/project[1]
print('Successful project backer average:',suc_bac_avg)
print('Failed project backer average:',fail_bac_avg)

## Average for project reward levels:
levels = pledge = df.groupby('status').levels.sum()
suc_lev_avg = levels[1]/project[0]
fail_lev_avg = levels[0]/project[1]
print('Successful project level average:',suc_lev_avg)
print('Failed project level average:',fail_lev_avg)

## Average duration box plot for projects:

sns.boxplot(x= df.status, y= df.duration)
plt.xlabel('Status')
plt.ylabel('Average Duration')
plt.title("Visualizing Status vs Duration")
plt.show()