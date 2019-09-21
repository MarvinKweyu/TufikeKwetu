# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
import pandas as pd


# read file
df = pd.read_csv('./FatalitiesMarch2018.csv')
df.head()


#%%
# filter out rows where there's -9

df["Age"] = pd.to_numeric(df["Age"]) #convert age to numeric

df = df[df.Age >0 ] # age cannot be -ve or 0
df.head()


#%%
# find out data types
df.dtypes


#%%
# gender cannot be -9
df = df[df.Gender != '-9' ]


#%%
# road user cannot be 9 or -9
df[df.Road_User!= '-9']
df[df.Road_User!= '9']

df[df.Speed_Limit > 0 ] #speed limit has to be a positive
df[df.Rigid_Truck_Involvement != '-9' ]
df.head()


#%%
# convert Time column to time data
# df['Time'] = pd.to_timedelta(df['Time'])
df['Time'] = pd.to_timedelta(df['Time'].radd('00:')) # ToDo
# df.dtypes


#%%
# save dataframe as cleaned data 
df.to_csv('data/clean_data.csv')


#%%
# plotting
# isolate dtat for two ye


