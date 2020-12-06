import pandas as pd
import numpy as np

# load main file
original = pd.read_csv('kick_starter_final.csv')

def main_data(df):
	df = df.drop(columns=["Unnamed: 0"])
	df.category = pd.Categorical(df.category).codes
	df.state = pd.Categorical(df.state).codes
	df.city = pd.Categorical(df.city).codes
	df.subcategory = pd.Categorical(df.subcategory).codes
	df.status = pd.Categorical(df.status).codes

	return df

def project_recommendation(data):

	df_main = main_data(original)

	# print(df)
	# print(df_main)

	# print(df_main.head())
	# strings = [str(integer) for integer in data['category']]
	# cat = "".join(strings)
	# print(cat)
	# print(df_main.category)
	# print(dtype(data['category']))

	df = df_main[(df_main['category'] == data['category']) & (df_main['subcategory'] == data['subcategory']) & (df_main['state'] == data['state']) & (df_main['state'] == data['state'])]
	
	## Total Number of projects:
	project = df.status.value_counts()
	# print('Total Successful project:',project[0])
	# print('Total Failed project (%):',project[1])

	## Total goals for Projects:
	goal = df.groupby('status').goal.sum()
	# print('Successful project goal:',round(goal[1],2))
	# print('Failed project goal:',round(goal[0],2))

	## Average for project goal:
	suc_goal_avg = goal[1]/project[0]
	fail_goal_avg = goal[0]/project[1]
	# print('Successful project goal average:',round(suc_goal_avg,2))
	# print('Failed project goal average:',round(fail_goal_avg,2))

	update = pledge = df.groupby('status').updates.sum()
	suc_update_avg = update[1]/project[0]
	fail_update_avg = update[0]/project[1]
	# print('Successful project update average:',round(suc_update_avg,2))
	# print('Failed project update average:',round(fail_update_avg,2))

	duration = df.groupby('status').duration.sum()
	suc_dur_avg = duration[1]/project[0]
	fail_dur_avg = duration[0]/project[1]
	# print('Successful project duration average:',round(suc_dur_avg,2))
	# print('Failed project duration average:',round(fail_dur_avg,2))

	## Average for project reward levels:
	levels = df.groupby('status').levels.sum()
	suc_lev_avg = levels[1]/project[0]
	fail_lev_avg = levels[0]/project[1]
	# print('Successful project level average:',round(suc_lev_avg,2))
	# print('Failed project level average:',round(fail_lev_avg,2))

	return project[0], project[1], round(suc_goal_avg,2), round(suc_update_avg,2), round(suc_dur_avg,2), round(suc_lev_avg,2)




