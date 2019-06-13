
#%%
## TITLE:

# Intoduction
# The website is structured as below:
# The main `index.html` file is located in the root directory with the individual analysis folders in 
# a different `analysis_pages` folder.
# The analysis is a comparison between road fatality in 1989 and 2017 with bar graphs being dran to
# match the respective time periods.

## Website Overview
# Fatality comparison in months
# Fatality comparison in states
# Fatality comparison according to crash type
#%%

# import neccessay libraries
import pandas as pd
from bokeh.io import output_file
from bokeh.io import save
from bokeh.plotting import figure
from bokeh.models import FactorRange
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap


#%%

df = pd.read_csv('FatalitiesMarch2018.csv')


# get 2017 and 1989 data
df_categorized = df.groupby('Year')
df_2017 = df_categorized.get_group(2017)
df_1989 = df_categorized.get_group(1989)

#%%
# filter the results for 1989 and 2017
import csv


def compare_data(column_name):
    """Compare data from 1989 with 2017.Takes a comlumn name to compare.
    Writes summary statistics to a csv from which it creates HTML content"""



    df_2017_fatalities = df_2017.groupby(column_name)
    df_1989_fatalities = df_1989.groupby(column_name)
    # complete 1989 against data so far collected this year(2017 in this case)
    last_complete_year = df_2017[column_name].unique().tolist()

    state_fatality_2017 = []
    state_fatality_1989 = []

    for item in range(len(last_complete_year)):
        state_fatality_2017.append(
            len(df_2017_fatalities.get_group(last_complete_year[item])))
        state_fatality_1989.append(
            len(df_1989_fatalities.get_group(last_complete_year[item])))
    

    #write summary statistic on each year
    with open('./statistics/' + column_name+'_summary.csv', mode='w') as summary_file:
        summary_writer = csv.writer(summary_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        summary_writer.writerow(['2017 maximum fatality:',max(state_fatality_2017)])
        summary_writer.writerow(['1989 maximum fatality:',max(state_fatality_1989)])

    summary_stat = pd.read_csv('./statistics/'+ column_name + '_summary.csv')

    dataset = [last_complete_year, state_fatality_2017, state_fatality_1989]

    return (dataset,summary_stat)


def draw_bar_chart(specific_data,year2017,year1989, title,summary_stat):
    """Draw a bar chart for the two selected years."""

#     months = unique2017.tolist()
    years = ['1989', '2017']

    data = {
        'dataset': specific_data,
        '1989': year1989,
        '2017': year2017
    }

    # create comparison between year and item [(item,'1989'),(item,2017) ..]
    x = [(item, year) for item in specific_data for year in years]

    counts = sum(zip(data['1989'], data['2017']), ())  # like an hstack
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    p = figure(x_range=FactorRange(*x), plot_height=250, title=title)

    p.vbar(x='x', top='counts', width=0.9, source=source, line_color="white",
           fill_color=factor_cmap('x', palette=['firebrick', 'blue'], factors=years, start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.05
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None
    result = './analysis_pages/'+title + '.html'
    output_file(result)
    save(p)
    insert_statistic(result,summary_stat)
    print("Done")


def insert_statistic(result,summary_stat):
    """Add summary statistics"""
    import fileinput
    file_path = result
    go_home = """ 
    <p><a href="../index.html">Back</a></p>
    """
    custom_html = summary_stat.to_html()+ go_home
    for line in fileinput.FileInput(file_path, inplace=1):
        if "</body>" in line:
            line = line.replace(line, custom_html+"\n"+line)
        print(line)



#%%

# fatality comparison in months
dataset,summary_stat = compare_data('Month')
specific_data = dataset[0]
year2017 = dataset[1]
year1989 = dataset[2]
title = "Monthly_Fatality"
# draw chart for month
draw_bar_chart(specific_data,year2017,year1989,title,summary_stat)
#%%
# fatality comparison in state
dataset,summary_stat = compare_data('State')

specific_data = dataset[0]
year2017 = dataset[1]
year1989 = dataset[2]
title = "Fatalities_according_to_state"
# draw chart for state
draw_bar_chart(specific_data, year2017, year1989, title, summary_stat)
#%%
# Fatality comparison according to crash type
dataset, summary_stat = compare_data('Crash_Type')

specific_data = dataset[0]
year2017 = dataset[1]
year1989 = dataset[2]
title = "Fatalities_in_crash_type"
# draw chart for crash type
draw_bar_chart(specific_data, year2017, year1989, title, summary_stat)


#%%

# fatality according to road user roles

# remove the -9 on both frames
column_name = 'Road_User'
df_2017 = df_2017[df_2017[column_name] != '9']
df_1989 = df_1989[df_1989[column_name] != '9']

dataset, summary_stat = compare_data(column_name)

# specific_data = dataset[0]
# year2017 = dataset[1]
# year1989 = dataset[2]
# title = "F"


#%%
