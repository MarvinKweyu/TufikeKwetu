#%%
# read the csv
import pandas as pd
from bokeh.plotting import figure
from bokeh.models.sources import ColumnDataSource

df = pd.read_csv('./data/clean_data.csv', parse_dates=['Year'])
df.head()


#%%
group = df.groupby('Year')
list_of_groups = [name for name, unused_df in group]
print(list_of_groups)


#%%
source = ColumnDataSource(group)
x_values = [x for x in range(5)]
y_values = [y for y in range(5,11)]

plot  = figure()
plot.line(x=x_values, y=y_values, source=source)

#%%
# find fatality for that group.

fatalities = [] # the y_axis
for year in list_of_groups:
    fatalities.append(len(group.get_group(year))) # find len of that year

print(fatalities)

len(fatalities) == len(list_of_groups)
#%%
from bokeh.plotting import show

source = ColumnDataSource(group)
x_values = list_of_groups
y_values = fatalities

plot = figure()
plot.line(x=x_values,y=y_values)
show(plot)


#%%
#* for bar chart

# df.Year = df.Year.astype(str)
group = df.groupby('Year')
# group.describe()
source = ColumnDataSource(group) #? would columndatasource work for vbar

plot = figure(plot_height=600,plot_width=900,x_range=group,title="Sample")
plot.vbar(x='Year',top='Age_count',width=0.8, source=source)
# plot.y_range.start = 0
show(plot)

#%%
# for line graph
from bokeh.plotting import show

df.Year = df.Year.astype(str)
group = df.groupby('Year')
source = ColumnDataSource(group)
plot = figure(plot_height=600, plot_width=900, x_range=group, title="Sample")
plot.line(x='Year', y='Age_count', line_width=3,source=source)

show(plot)



#%%
