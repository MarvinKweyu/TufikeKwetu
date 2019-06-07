
#%%
import pandas as pd
from bokeh.io import output_notebook
from bokeh.plotting import figure


#%%
df = pd.read_csv('FatalitiesMarch2018.csv')
df_categorized = df.groupby('Year')

#%%
df_2017 = df_categorized.get_group(2017)
df_1989 = df_categorized.get_group(1989)

#%%
from bokeh.io import output_file
from bokeh.io import show
from bokeh.models import FactorRange
from bokeh.models import ColumnDataSource
from bokeh.transform import factor_cmap


# create function to draw bar chart

def draw_bar_chart(dataset,title="Fatality count",colors = ['firebrick','blue']):
    """Draw a bar chart for the two selected years."""
    
    # output_file = ('sample.html')
    
#     months = unique2017.tolist()
    years = ['1989','2017']
    dataset_try = dataset[0]
    data = {
        'dataset':dataset_try,
        '1989': dataset[2],
        '2017': dataset[1]
    }

    # create comparison between year and item [(item,'1989'),(item,2017) ..]
    x = [ (item, year) for item in dataset_try[0] for year in years ]

    counts = sum(zip(data['1989'],data['2017']), ()) # like an hstack
    source = ColumnDataSource(data=dict(x=x, counts=counts))

    p = figure(x_range=FactorRange(*x), plot_height=250,title=title)

    p.vbar(x='x', top='counts', width=0.9, source=source,line_color="white",
           fill_color=factor_cmap('x', palette=colors, factors=years, start=1, end=2))

    p.y_range.start = 0
    p.x_range.range_padding = 0.05
    p.xaxis.major_label_orientation = 1
    p.xgrid.grid_line_color = None

    output_file('sample.html')
    # show(p)
    



def compare_data(column_name):
    """Compare data from 1989 with 2017.Takes a comlumn name to compare."""
#     df_categorized = df.groupby('Year')
#     df_2017 = df_categorized.get_group(2017)
#     df_1989 = df_categorized.get_group(1989)
    
    df_2017_fatalities = df_2017.groupby(column_name)
    df_1989_fatalities = df_1989.groupby(column_name)
    # complete 1989 against data so far collected this year(2017 in this case)
    last_complete_year = df_2017[column_name].unique().tolist() #
    
    state_fatality_2017 = []
    state_fatality_1989 = []

    for item in range(len(last_complete_year)):
        state_fatality_2017.append(len(df_2017_fatalities.get_group(last_complete_year[item])))
        state_fatality_1989.append(len(df_1989_fatalities.get_group(last_complete_year[item])))
    
    dataset = [last_complete_year,state_fatality_2017,state_fatality_1989]
    
    return dataset
    


#%%

dataset = compare_data('State')
draw_bar_chart(dataset)

#%%
