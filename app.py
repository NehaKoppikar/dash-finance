import dash
import dash_auth
import dash_core_components as dcc
import dash_html_components as html
#import dash_enterprise_auth as auth
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Keep this out of source code repository - save in a file or a database
VALID_USERNAME_PASSWORD_PAIRS = {
    'hello': 'world'
}



df = pd.read_csv("data.csv")

app = dash.Dash(__name__)

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

server = app.server



app.title = "Visualizing Finance Data"

app.layout = html.Div([
        dcc.Dropdown(
        id="ticker",
        options=[{"label": x, "value": x} 
                 for x in df.columns[1:]],
        value=df.columns[1],
        clearable=False,
    ),
    dcc.Graph(id="time-series-chart"),
    html.Div(
    dcc.Markdown("*Hello! You are looking at INPX Stock Prices from January 1, 2020 to January 15 2021. This is data has been collected from Yahoo Finace's Website. Feel free to watch the different versions of prices by using the DropDown Option above. Thanks!*")
)
])

# # For downloading the data in CSV format
#     html.Div([
#     dash_table.DataTable(
#     id='table',
#     columns=[{"name": i, "id": i} for i in df.columns],
#     data=df.to_dict('records'),
#     export_format='xlsx',
#     export_headers='display',
#     merge_duplicate_headers=True,
#     page_current=0,
#     page_size=10
#     )]),

@app.callback(
    Output("time-series-chart", "figure"), 
    [Input("ticker", "value")])
def display_time_series(ticker):
    fig = px.line(df, x='Date', y=ticker)
    return fig





app.run_server(debug=True)