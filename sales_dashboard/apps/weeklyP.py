import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.svm import SVR
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Output, Input
import pathlib
from app import app

PATH = pathlib.Path(__file__).parent
DATA_PATH = PATH.joinpath("../datasets").resolve()
data = pd.read_csv(DATA_PATH.joinpath("salesweekly.csv"))
df = pd.read_csv("C:/Users/HOME/Desktop/dash/datasets/salesweekly.csv")
  
layout = html.Div(
    children=[
        html.Div(
            html.H1(children=" WEEKLY PREDICTION",className="header-title",style={"fontSize": "48px", "color": "black"},),
        ),
        html.Div(children="Select how many weeks ahead you want to predict",className="menu-title"),
            dcc.Dropdown(
                id='opt_weeks_ahead',
                options=[
                    {'label': '1','value' : '1'},
                    {'label': '2','value' : '2'},
                    {'label': '3','value' : '3'},
                    {'label': '4','value' : '4'},
                   
                ],
                value='2'
            ),
        html.Div(children="Select the product",className="menu-title"),
            dcc.Dropdown(
                id='opt_product_for_week',
                options = [
                    {'label':i,'value':i}
                    for i in df.columns[1:]
                ]
                
            ),
        html.Div(id = 'result_week')
    ],
    className="menu-title",
) 

@app.callback(
    Output("result_week", "children"),
    [Input("opt_weeks_ahead", "value"),
    Input("opt_product_for_week", "value")])

def resulto(opt_weeks_ahead,opt_product_for_week):
    def predictSVR(X_train, y_train, X_test, y_test):
        y_train = y_train.reshape(-1, 1)
        y_test = y_test.reshape(-1, 1)
        
        svr_regressor = SVR(kernel='rbf', gamma='auto')
        svr_regressor.fit(X_train, y_train.ravel())
        
        y_predict_svr = svr_regressor.predict(X_test)
        
        svr_predict = svr_regressor.predict([[predictFor]])
       
        accuracy = svr_regressor.score(X_train, y_train)
    
    product = opt_product_for_week
    
    df = pd.read_csv("C:/Users/HOME/Desktop/dash/datasets/salesweekly.csv")
    df = df.loc[df['datum'].str.contains("2014") | df['datum'].str.contains("2015") | df['datum'].str.contains("2016") | df['datum'].str.contains("2017") | df['datum'].str.contains("2018") | df['datum'].str.contains("2019")]
    df = df.reset_index()
    df['datumNumber'] = 1
    for index, row in df.iterrows():
        df.loc[index, 'datumNumber'] = index+1
    df.drop(df.head(1).index,inplace=True)
    df.drop(df.tail(1).index,inplace=True)
    df = df[df[product] != 0]
    
    a=int (u' {}'.format(opt_weeks_ahead)) 
    predictFor = len(df)+ a
    
    dfSplit = df[['datumNumber', product]]
    
    train, test = train_test_split(dfSplit, test_size=3/10, random_state=0)
    trainSorted = train.sort_values('datumNumber', ascending=True)
    testSorted = test.sort_values('datumNumber', ascending=True)

    X_train = trainSorted[['datumNumber']].values
    y_train = trainSorted[product].values
    X_test = testSorted[['datumNumber']].values
    y_test = testSorted[product].values
    y_train = y_train.reshape(-1, 1)
    y_test = y_test.reshape(-1, 1)
        
    svr_regressor = SVR(kernel='rbf', gamma='auto')
    svr_regressor.fit(X_train, y_train.ravel())
        
    y_predict_svr = svr_regressor.predict(X_test)
    svr_predict = svr_regressor.predict([[predictFor]])
    return html.Div([
        html.Div(children=['Predictions for the product ' + str(product) + ' sales ' + str(svr_predict)])
    ])
