import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Output, Input
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
data = pd.read_csv(DATA_PATH.joinpath("salesweekly.csv"))

#data = pd.read_csv("C:/Users/HOME/Desktop/dash2/dash/datasets/salesweekly.csv")
  
features = data.columns[1:-1]
opts = [{'label' : i, 'value' : i} for i in features]

data['datum'] = pd.to_datetime(data.datum)
dates = ['2014-01-31', '2015-08-31', '2015-04-30', '2015-12-31',
         '2016-09-30', '2017-05-31', '2018-01-31', '2018-09-30',  
         '2019-05-31']

trace_1 = go.Scatter(x = data.datum, y = data['M01AB'],
                    name = 'M01AB',
                    line = dict(width = 2,
                                color = 'rgb(229, 151, 50)'))
layout_weekly = go.Layout(title = 'Time Series Plot',
                   hovermode = 'closest')
fig = go.Figure(data = trace_1, layout = layout_weekly)

layout = html.Div(
    children=[
        html.Div(
            html.H1(children="weekly DATA VISUALIZATION",className="header-title",style={"fontSize": "48px", "color": "black"},),
        ),
        
        html.Div(
            children=[
                html.Div(children="Select Date Range",className="menu-title"),
                    dcc.RangeSlider(id = 'slider',
                                    marks = {i : dates[i] for i in range(0, 9)},
                                    min = 0,
                                    max = 8,
                                    value = [1, 7]),     
                html.Div(children="Select medicines",className="menu-title"),
                    dcc.Dropdown(
                        id='opt',options = opts,
                        value=features[0],
                                      
                    )
            ],
            className="menu-title",
        ),
        dcc.Graph(id = 'plot_weekly', figure = fig),
        html.Div(
        children=[
            html.Div(
                children=dcc.Graph(
                    id='price-chart_weekly', config={"displayModeBar": False}
                ),
                className="card",
            ),
           
        ],
        className="wrapper",
        ), 
    ],
    className="menu-title",
)

@app.callback(
    [Output("plot_weekly","figure"),Output("price-chart_weekly","figure")],
    [Input("opt", "value"),
     Input("slider", "value")])
def update_charts(input1, input2):
    
    data2 = data[(data.datum > dates[input2[0]]) & (data.datum < dates[input2[1]])]
    
    trace_1 = go.Scatter(x = data2.datum, y = data2['M01AB'],
                        name = 'M01AB',
                        line = dict(width = 2,
                                    color = 'rgb(129, 151, 50)')) 
                        
    trace_2 = go.Scatter(x = data2.datum, y = data2[input1],
                        name = input1,
                        line = dict(width = 2,
                                    color = 'rgb(106, 181, 135)'))
    
    
    fig = go.Figure(data = [trace_1, trace_2], layout = layout_weekly)
    
    figure =go.Figure(
        data= [
            go.Bar(
                    name = "M01AB",
                    x= data2.datum,
                    y= data2['M01AB'],
                   
                
            ),
            go.Bar(
                    name = input1,
                    x= data2.datum,
                    
                    y= data2[input1],
                       
            ),
        ],
        layout=go.Layout(
        title="Bar Plot",
        xaxis_title="Date Range",
        yaxis_title="Sales"
        )
    )
        
    return fig,figure
