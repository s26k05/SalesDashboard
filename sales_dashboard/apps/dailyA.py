import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import dash_bootstrap_components as dbc
from dash.dependencies import Output, Input
import pathlib
from app import app
import re
  
PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
df = pd.read_csv(DATA_PATH.joinpath("C:/Users/HOME/Desktop/dash/datasets/salesdaily.csv"))
df= pd.read_csv("C:/Users/HOME/Desktop/dash/datasets/salesdaily.csv")

layout = html.Div([
    html.Div(
            html.H1(children="Analyze daily sales",className="header-title",style={"fontSize": "48px", "color": "black"},),
        ),
    dbc.Container([
        dbc.Row([
            
            html.A("On which day of the week is the below selected drug most often sold?")
        ])
    ]),
    html.Div(children="Select Product",className="menu-title"),
    dcc.Dropdown(
        id='opt_product',
        options=[
           {'label':i, 'value':i}
           for i in df.columns [1: 9]
        ],
        
    ),
    html.Div(id = 'resulttt'),
    
])

@app.callback(
    Output('resulttt','children'),
    Input('opt_product', 'value')
    )

def product(opt_product):
    df= pd.read_csv("C:/Users/HOME/Desktop/dash/datasets/salesdaily.csv")
    df = df[[opt_product, 'Weekday Name']]
    result = df.groupby(['Weekday Name'], as_index=False).sum().sort_values(opt_product, ascending=False)
    resultDay = result.iloc[0,0]
    resultValue = round(result.iloc[0,1], 2)
    return html.Div([
        html.Div(children=['Product '+ format(opt_product)+' was most often sold on '+str(resultDay)+' with the volume of ' + str(resultValue)])
    ])
def update_result(opt_product):
    produc = u' {}'.format(opt_product)

    children = [
        product(produc)
    ]
    return children
