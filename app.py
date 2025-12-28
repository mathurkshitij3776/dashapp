import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# 1. Load the data
# We assume 'formatted_data.csv' was created in Task 2.
try:
    df = pd.read_csv('formatted_data.csv')
except FileNotFoundError:
    # Fallback/Error handling if the file isn't found
    print("Error: 'formatted_data.csv' not found. Please run the Task 2 script first.")
    exit()

# 2. Process the data
# The task requires the data to be "sorted by date".
# We must convert the 'Date' column to datetime objects to sort them chronologically.
df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by='Date')

# 3. Create the Visualization (Line Chart)
# We use Plotly Express (px) for a simple line chart.
# x-axis: Date, y-axis: Sales.
fig = px.line(
    df, 
    x='Date', 
    y='Sales', 
    title='Pink Morsel Sales Over Time'
)

# Update axis labels to be more readable (optional but recommended)
fig.update_layout(
    xaxis_title='Date',
    yaxis_title='Total Sales ($)',
    title_x=0.5 # Centers the chart title
)

# 4. Initialize the Dash App
app = dash.Dash(__name__)

# 5. Define the Layout
# The task requires: "A header which appropriately titles the visualiser"
app.layout = html.Div(children=[
    
    # The Header
    html.H1(
        children='Soul Foods Sales Visualizer',
        style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
    ),

    # The Graph
    html.Div(children=[
        dcc.Graph(
            id='sales-line-chart',
            figure=fig
        )
    ])
])

# 6. Run the App
# ... (rest of your code above remains the same)

# 6. Run the App
if __name__ == '__main__':
    # CHANGED: 'run_server' is obsolete, use 'run' instead
    app.run(debug=True)