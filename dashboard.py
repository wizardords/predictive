import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash(__name__)

app.layout = html.Div([
    dcc.Graph(id='price-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*60000,
        n_intervals=0
    )
])

@app.callback(
    Output('price-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n_intervals):
    df = pd.read_csv('btc_historical_data.csv')
    df['time'] = pd.to_datetime(df['time'])
    trace = go.Scatter(x=df['time'], y=df['close'], mode='lines', name='BTC Price')
    layout = go.Layout(title='Bitcoin Price Over Time', xaxis={'title': 'Date'}, yaxis={'title': 'Price (USD)'})
    return {'data': [trace], 'layout': layout}

if __name__ == '__main__':
    app.run_server(debug=True)
