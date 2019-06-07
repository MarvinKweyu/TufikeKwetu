
#%%
import pandas as pd
from bokeh.io import output_file
from bokeh.io import save
from bokeh.plotting import figure


#%%
df = pd.read_csv('FatalitiesMarch2018.csv')


#%%
df_categorized = df.groupby('Year')
df_categorized.first()


#%%
df_2017 = df_categorized.get_group(2017)
df_1989 = df_categorized.get_group(1989)


#%%
# get fatalities for the two years
fatality_2017 = df_2017.shape[0]
fatality_1989 = df_1989.shape[0]
print(f" fatalities  in 2017: ", fatality_2017)
print(f"fatalities in 1989: ",fatality_1989)

#%%
#get months displayed
unique2017 = df_2017['Month'].unique()
print("Unique months for 2017")
print(unique2017)
print("\nUnique months for 1989")
df_1989['Month'].unique()


#%%
# get information for the respective months
months = unique2017.tolist()

# months data for 2017
df_2017_months = df_2017.groupby('Month')
df_1989_months = df_1989.groupby('Month')
df_2017_months.first()


#%%
# len(df_2017_months.get_group(months[0])) #the fatality for December 130

# get the fatalities of the respective months starting from December backwards and place in each years list
fatality_2017 = []
fatality_1989 = []

for item in range(len(months)):
    fatality_2017.append(len(df_2017_months.get_group(months[item])))
    fatality_1989.append(len(df_1989_months.get_group(months[item])))


#%%
from bokeh.io import show
from bokeh.models import FactorRange
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap

#use monthly frequency to plot
# use the latest data to compare the monthly analysis
months = unique2017.tolist()
years = ['1989','2017']

data = {
    'months': months,
    '1989': fatality_1989,
    '2017': fatality_2017
}

# create comparison between year and month [('March','1989'),('March',2017) ..]
x = [ (month, year) for month in months for year in years ]

counts = sum(zip(data['1989'],data['2017']), ()) # like an hstack
source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250,title="Fatality Counts by month")

p.vbar(x='x', top='counts', width=0.9, source=source,line_color="white",
       fill_color=factor_cmap('x', palette=['firebrick', 'blue'], factors=years, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.05
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

output_file("Monthly_Fatality_comparison.html")
save(p)


#%%
# fatalities per Australian State
# Grouping data by state
df_2017_states = df_2017.groupby('State')
df_1989_states = df_1989.groupby('State')
df_2017_states.first()


#%%
# get state information for data collected in 2017 and use it as a reference
# i.e compare whole data with latest pool collection 
states2017 = df_2017['State'].unique().tolist()

#%%
# get the fatalities of the respective months starting from December backwards and place in each years list
state_fatality_2017 = []
state_fatality_1989 = []

for item in range(len(states2017)):
    state_fatality_2017.append(len(df_2017_states.get_group(states2017[item])))
    state_fatality_1989.append(len(df_1989_states.get_group(states2017[item])))
    
state_fatality_1989


#%%
data = {
    'state': states2017,
    '1989': state_fatality_1989,
    '2017': state_fatality_2017
}

x = [ (state, year) for state in states2017 for year in years ]

source = ColumnDataSource(data=dict(x=x, counts=counts))

p = figure(x_range=FactorRange(*x), plot_height=250,title="Fatality Counts by State")

p.vbar(x='x', top='counts', width=0.9, source=source,line_color="white",
       fill_color=factor_cmap('x', palette=['firebrick', 'blue'], factors=years, start=1, end=2))

p.y_range.start = 0
p.x_range.range_padding = 0.05
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

output_file("State_Fatality_comparison.html")
save(p)


