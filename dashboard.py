import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go

# Initialize the Dash app
app = dash.Dash(__name__)

# App layout
app.layout = html.Div([
    dcc.Graph(id='price-graph'),
    dcc.Interval(
        id='interval-component',
        interval=1*60000,  # Update every minute
        n_intervals=0
    )
])

# Callback to update the graph
@app.callback(
    Output('price-graph', 'figure'),
    [Input('interval-component', 'n_intervals')]
)
def update_graph(n_intervals):
    df = pd.read_csv('btc_historical_data.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    trace = go.Scatter(x=df['timestamp'], y=df['close'], mode='lines', name='BTC Price')
    layout = go.Layout(title='Bitcoin Price Over Time', xaxis={'title': 'Date'}, yaxis={'title': 'Price (USD)'})
    return {'data': [trace], 'layout': layout}

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
