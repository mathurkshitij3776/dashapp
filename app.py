# import dash
# from dash import html, dcc
# import plotly.express as px
# import pandas as pd

# # 1. Load the data
# # We assume 'formatted_data.csv' was created in Task 2.
# try:
#     df = pd.read_csv('formatted_data.csv')
# except FileNotFoundError:
#     # Fallback/Error handling if the file isn't found
#     print("Error: 'formatted_data.csv' not found. Please run the Task 2 script first.")
#     exit()

# # 2. Process the data
# # The task requires the data to be "sorted by date".
# # We must convert the 'Date' column to datetime objects to sort them chronologically.
# df['Date'] = pd.to_datetime(df['Date'])
# df = df.sort_values(by='Date')

# # 3. Create the Visualization (Line Chart)
# # We use Plotly Express (px) for a simple line chart.
# # x-axis: Date, y-axis: Sales.
# fig = px.line(
#     df, 
#     x='Date', 
#     y='Sales', 
#     title='Pink Morsel Sales Over Time'
# )

# # Update axis labels to be more readable (optional but recommended)
# fig.update_layout(
#     xaxis_title='Date',
#     yaxis_title='Total Sales ($)',
#     title_x=0.5 # Centers the chart title
# )

# # 4. Initialize the Dash App
# app = dash.Dash(__name__)

# # 5. Define the Layout
# # The task requires: "A header which appropriately titles the visualiser"
# app.layout = html.Div(children=[
    
#     # The Header
#     html.H1(
#         children='Soul Foods Sales Visualizer',
#         style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}
#     ),

#     # The Graph
#     html.Div(children=[
#         dcc.Graph(
#             id='sales-line-chart',
#             figure=fig
#         )
#     ])
# ])

# # 6. Run the App
# # ... (rest of your code above remains the same)

# # 6. Run the App
# if __name__ == '__main__':
#     # CHANGED: 'run_server' is obsolete, use 'run' instead
#     app.run(debug=True)
import dash
from dash import html, dcc, Input, Output
import plotly.express as px
import pandas as pd

# 1. Load and Pre-process Data
try:
    df = pd.read_csv('formatted_data.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    df = df.sort_values(by='Date')
except FileNotFoundError:
    print("Error: 'formatted_data.csv' not found. Make sure you ran Task 2 successfully.")
    exit()

# 2. Initialize App
app = dash.Dash(__name__)

# --- STYLING CONFIGURATION ---
# We define colors here to keep the design consistent
colors = {
    'background': '#F5F7FA',   # Light grey-blue for the whole page
    'text': '#333333',         # Dark grey for text (easier on eyes than pure black)
    'header': '#503D36',       # The Soul Foods brand color
    'card': '#FFFFFF',         # White background for the graph area
    'accent': '#007BFF'        # Blue accent for active elements
}

# 3. App Layout (The Visual Structure)
app.layout = html.Div(style={'backgroundColor': colors['background'], 'fontFamily': 'sans-serif', 'minHeight': '100vh', 'padding': '40px'}, children=[
    
    # HEADER SECTION
    html.H1(
        children='Soul Foods Sales Visualizer',
        style={
            'textAlign': 'center', 
            'color': colors['header'], 
            'fontSize': '48px',
            'marginBottom': '20px'
        }
    ),
    html.P(
        "Explore sales trends for Pink Morsels across different regions.",
        style={'textAlign': 'center', 'color': '#666', 'fontSize': '18px', 'marginBottom': '40px'}
    ),

    # CONTROL SECTION (Radio Button)
    html.Div(style={'display': 'flex', 'justifyContent': 'center', 'marginBottom': '30px'}, children=[
        html.Div(style={'backgroundColor': colors['card'], 'padding': '15px 30px', 'borderRadius': '50px', 'boxShadow': '0 2px 5px rgba(0,0,0,0.1)'}, children=[
            html.Label("Select Region: ", style={'fontWeight': 'bold', 'marginRight': '15px', 'color': colors['text']}),
            dcc.RadioItems(
                id='region-selector',
                options=[
                    {'label': 'All Regions', 'value': 'all'},
                    {'label': 'North', 'value': 'north'},
                    {'label': 'East', 'value': 'east'},
                    {'label': 'South', 'value': 'south'},
                    {'label': 'West', 'value': 'west'}
                ],
                value='all',    # Default selection
                inline=True,    # Layout options horizontally
                labelStyle={'marginRight': '20px', 'cursor': 'pointer'} # Space out the buttons
            )
        ])
    ]),

    # GRAPH SECTION
    html.Div(
        style={
            'backgroundColor': colors['card'], 
            'padding': '30px', 
            'borderRadius': '15px', 
            'boxShadow': '0 4px 15px rgba(0,0,0,0.1)' # Creates a "floating card" effect
        },
        children=[
            dcc.Graph(id='sales-line-chart')
        ]
    )
])

# 4. The Callback (The Logic)
@app.callback(
    Output('sales-line-chart', 'figure'),
    Input('region-selector', 'value')
)
def update_graph(selected_region):
    # Logic: Filter the dataframe based on selection
    if selected_region == 'all':
        filtered_df = df
        title_text = "Daily Sales: All Regions"
    else:
        filtered_df = df[df['Region'] == selected_region]
        title_text = f"Daily Sales: {selected_region.capitalize()} Region"

    # Create the figure with the filtered data
    fig = px.line(
        filtered_df, 
        x='Date', 
        y='Sales', 
        title=title_text
    )

    # Style the chart itself to match the app theme
    fig.update_layout(
        plot_bgcolor=colors['card'],
        paper_bgcolor=colors['card'],
        font_color=colors['text'],
        title_x=0.5, # Center the chart title
        xaxis=dict(showgrid=False), # Clean up the grid
        yaxis=dict(showgrid=True, gridcolor='#eee')
    )
    
    return fig

# 5. Run the App
if __name__ == '__main__':
    app.run(debug=True)