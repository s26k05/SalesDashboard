import dash_html_components as html
import dash_bootstrap_components as dbc

layout = html.Div([
    html.Div(
            html.H1(children=" about us",className="header-title",style={"fontSize": "48px", "color": "black"},),
        ),
    dbc.Container([
        dbc.Row([
              
            html.A("This is the SALES PREDICTION OF A PHARMACEUTICAL DISTRIBUTION COMPANY. It contains the data of hourly, daily, weekly and monthly sales of the medicines in grams. The data has been visualized and analyzed for the easy understanding of sales record. We've also predicted the sales of the medicines in the near future so as to help in the planning process of the inventory.The dataset is built from the initial dataset consisted of 600000 transactional data collected in 6 years (period 2014-2019), indicating date and time of sale, pharmaceutical drug brand name and sold quantity, exported from Point-of-Sale system in the individual pharmacy. Selected group of drugs from the dataset (57 drugs) is classified to the following Anatomical Therapeutic Chemical (ATC) Classification System categories:M01AB - Anti-inflammatory and antirheumatic products, non-steroids, Acetic acid derivatives and related substances; M01AE - Anti-inflammatory and antirheumatic products, non-steroids, Propionic acid derivatives; N02BA - Other analgesics and antipyretics, Salicylic acid and derivatives; N02BE/B - Other analgesics and antipyretics, Pyrazolones and AnilidesN05B - Psycholeptics drugs, Anxiolytic drugs; N05C - Psycholeptics drugs, Hypnotics and sedatives drugs; R03 - Drugs for obstructive airway diseases; R06 - Antihistamines for systemic use")
        ])
    ])
],style={'textAlign':'center'})
