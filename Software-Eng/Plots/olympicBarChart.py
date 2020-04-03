import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/Olympic2016Rio.csv')


# Creating sum of medals by NOC
new_df = df.groupby(['NOC'])['Total'].sum().reset_index()

# Sorting values and select first 20 countries
new_df = new_df.sort_values(by=['Total'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['NOC'], y=new_df['Total'])]

# Preparing layout
layout = go.Layout(title='Rio Olympic Medal Totals', xaxis_title="Countries",
                   yaxis_title="Number of Medals")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='olympicbarchart.html')
