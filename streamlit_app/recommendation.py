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
	

	try:
		df = df_main[(df_main['category'] == data['category']) & (df_main['subcategory'] == data['subcategory']) & (df_main['state'] == data['state']) & (df_main['state'] == data['state'])]
		counter = 0 
		## Total Number of projects:
		project = df.status.value_counts()

		## Average goal for sucessfull project:
		goal = df.groupby('status').goal.sum()
		suc_goal_avg = goal[1]/project[0]

		## Average updates for sucessfull project:
		update = pledge = df.groupby('status').updates.sum()
		suc_update_avg = update[1]/project[0]

		## Average duration for sucessfull project:
		duration = df.groupby('status').duration.sum()
		suc_dur_avg = duration[1]/project[0]

		## Average levels for sucessfull project:
		levels = df.groupby('status').levels.sum()
		suc_lev_avg = levels[1]/project[0]

	except:
		df = df_main[(df_main['category'] == data['category']) & (df_main['subcategory'] == data['subcategory'])]
		counter = 1
		## Total Number of projects:
		project = df.status.value_counts()

		## Average goal for sucessfull project:
		goal = df.groupby('status').goal.sum()
		suc_goal_avg = goal[1]/project[0]

		## Average updates for sucessfull project:
		update = pledge = df.groupby('status').updates.sum()
		suc_update_avg = update[1]/project[0]

		## Average duration for sucessfull project:
		duration = df.groupby('status').duration.sum()
		suc_dur_avg = duration[1]/project[0]

		## Average levels for sucessfull project:
		levels = df.groupby('status').levels.sum()
		suc_lev_avg = levels[1]/project[0]

		return project[0], project[1], round(suc_goal_avg,2), round(suc_update_avg,2), round(suc_dur_avg,2), round(suc_lev_avg,2), counter

	return project[0], project[1], round(suc_goal_avg,2), round(suc_update_avg,2), round(suc_dur_avg,2), round(suc_lev_avg,2), counter




