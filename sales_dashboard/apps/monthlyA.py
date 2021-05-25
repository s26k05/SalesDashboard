import dash
import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Output, Input
import pathlib
from app import app
import re
import calendar
from datetime import datetime
  
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
data = pd.read_csv(DATA_PATH.joinpath("salesmonthly.csv"))

layout = html.Div([

    html.Div(
            html.H1(children=" analyze monthly sales",className="header-title",style={"fontSize": "48px", "color": "black"},),
        ),
    dbc.Container([
        dbc.Row([
            
            html.A("Which three drugs have the highest and lowest sales in the selected month and year?")
        ])
    ]),
    html.Div(children="Select Month",className="menu-title"),
    dcc.Dropdown(
        id='opt_month',
        options=[
            
            {'label': '1','value' : '1'},
            {'label': '2','value' : '2'},
            {'label': '3','value' : '3'},
            {'label': '4','value' : '4'},
            {'label': '5','value' : '5'},
            {'label': '6','value' : '6'},
            {'label': '7','value' : '7'},
            {'label': '8','value' : '8'},
            {'label': '9','value' : '9'},
            {'label': '10','value' : '10'},
            {'label': '11','value' : '11'},
            {'label': '12','value' : '12'}
            
        ],
        value='2'
    ),
    html.Div(children="Select Year",className="menu-title"),
    dcc.Dropdown(
        id='opt_year',
        options=[
             
            {'label': '2014','value' : '2014'},
            {'label': '2015','value' : '2015'},
            {'label': '2016','value' : '2016'},
            {'label': '2017','value' : '2017'},
            {'label': '2018','value' : '2018'},
            {'label': '2019','value' : '2019'},
            
        ],
        value='2015'
    ),
    html.Div(id = 'resultt')
    
])

def lowest3byMonth(month, year):
   
    month = str(month) if (month > 9) else '0'+str(month)
    year = str(year)
    sales = data.loc[data['datum'].str.contains('^'+year+'\-'+month+'', flags=re.I, regex=True)]
    sales = sales.reset_index()
    topSales = sales[['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']]
    topSales = topSales.sort_values(by=0, ascending=True, axis=1)
    return html.Div([
        html.Div(children=['   Lowest 3 drugs by sale in '+calendar.month_name[int(month)]+' '+year]),
        html.Div(children=['    - Product: ' + format(topSales.columns.values[0]) + ', Volume sold: ' + format(str(round(topSales[topSales.columns.values[0]].iloc[0],2)))]),
        html.Div(children=['    - Product: ' + format(topSales.columns.values[1]) + ', Volume sold: ' + format(str(round(topSales[topSales.columns.values[1]].iloc[0],2)))]),
        html.Div(children=['    - Product: ' + format(topSales.columns.values[2]) + ', Volume sold: ' + format(str(round(topSales[topSales.columns.values[2]].iloc[0],2)))])
     ])
def top3byMonth(month, year):
    
    month = str(month) if (month > 9) else '0'+str(month)
    year = str(year)
    sales = data.loc[data['datum'].str.contains('^'+year+'\-'+month+'', flags=re.I, regex=True)]
    sales = sales.reset_index()
    topSales = sales[['M01AB', 'M01AE', 'N02BA', 'N02BE', 'N05B', 'N05C', 'R03', 'R06']]
    topSales = topSales.sort_values(by=0, ascending=False, axis=1)    
    return html.Div([
        html.Div(children=['   Top 3 drugs by sale in '+calendar.month_name[int(month)]+' '+year]),
        html.Div(children=['    - Product: ' + format(topSales.columns.values[0]) + ', Volume sold: ' + format(str(round(topSales[topSales.columns.values[0]].iloc[0],2)))]),
        html.Div(children=['    - Product: ' + format(topSales.columns.values[1]) + ', Volume sold: ' + format(str(round(topSales[topSales.columns.values[1]].iloc[0],2)))]),
        html.Div(children=['    - Product: ' + format(topSales.columns.values[2]) + ', Volume sold: ' + format(str(round(topSales[topSales.columns.values[2]].iloc[0],2)))])
     ])

@app.callback(
    Output('resultt','children'),
    [dash.dependencies.Input('opt_month', 'value'),dash.dependencies.Input('opt_year', 'value')],
    )
def update_result(opt_month,opt_year):
    month = u' {}'.format(opt_month)
    year = u' {}'.format(opt_year)
    children = [
        lowest3byMonth(int(month),int(year)),
        top3byMonth(int(month),int(year))
    ]
    return children
