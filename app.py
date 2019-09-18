from flask import Flask, render_template, request
import pandas as pd
from bokeh.plotting import figure
from bokeh.embed import components


app = Flask(__name__)

# load dataset
fatalities = pd.read_csv('./data/cleaned_data.csv')


""" 
Items to generate:
1.Fatalities per year and how it is changing over time
2.Fatalities per state
3.Fatalities at different times of the day
4.Impact of different speed limit zones
5.Impact of different road-user roles: driver,passenger, motor_cyclist
"""
items_for_compare = ['Year', 'State', 'Month']

def create_figure(according_to):
    """Create main plot. """
    # group by category selected
    
    g = fatalities.groupby(according_to)
    groups = [name for name, unused_df in g] # list of all available years for instance
   
    # get average fatality according to classification for y-axis
    average_count = []
    for item in groups:


    plot = figure(plot_height=600, plot_width=600, title=according_to)
    plot.line(groups, )

    return plot


@app.route('/')
def index():

    # determine selected feature
    current_comparison = request.args.get("item_for_compare")
    if current_comparison == None:
        current_comparison = "Year"

    # create plot
    plot = create_figure(current_comparison)

    # embed plot to html
    script,div = components(plot)

    return render_template("index.html",script=script, div=div, the_items_for_compare = items_for_compare,current_comparison=current_comparison)


if __name__ == "__main__":
    app.run(port=5000, debug=True)
    
