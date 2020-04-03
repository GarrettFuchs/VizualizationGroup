import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Weather2014-15.csv')
df['date'] = pd.to_datetime(df['date'])
# Preparing data
trace1 = go.Scatter(x=df['date'], y=df['actual_max_temp'], mode='lines', name='actual_max_temp')
trace2 = go.Scatter(x=df['date'], y=df['actual_min_temp'], mode='lines', name='actual_min_temp')
trace3 = go.Scatter(x=df['date'], y=df['actual_mean_temp'], mode='lines', name='actual_mean_temp')
data = [trace1,trace2,trace3]
# Preparing layout
layout = go.Layout(title='Actual Max, Actual Min, and Actual Mean Temperatures for 2014-2015',
                   xaxis_title="Date",
                   yaxis_title="Max, Min, and Mean")
# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='tempmultilinechart.html')