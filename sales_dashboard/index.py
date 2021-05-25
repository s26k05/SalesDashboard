import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
from app import app
from apps import aboutus,dailyA,dailyV,homedaily,homehourly,homemonthly,homeweekly,home,hourlyV,monthlyA,monthlyP,monthlyV,weeklyP,weeklyV
  
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/haha"),
        dbc.DropdownMenuItem("About Us", href="/apps/aboutus"),
    ],
    nav = True,
    in_navbar = True,
    label = "Explore",
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/d.png", height="30px")),
                        dbc.Col(dbc.NavbarBrand("SALES DASH", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/apps/monthlyV':
        return monthlyV.layout
    elif pathname == '/apps/monthlyA':
        return monthlyA.layout
    elif pathname == '/apps/monthlyP':
        return monthlyP.layout
    elif pathname == '/apps/weeklyP':
        return weeklyP.layout
    elif pathname == '/apps/weeklyV':
        return weeklyV.layout
    elif pathname == '/apps/aboutus':
        return aboutus.layout
    elif pathname == '/apps/hourlyV':
        return hourlyV.layout
    elif pathname == '/apps/dailyV':
        return dailyV.layout
    elif pathname == '/apps/dailyA':
        return dailyA.layout
    elif pathname == '/apps/homedaily':
        return homedaily.layout
    elif pathname == '/apps/homemonthly':
        return homemonthly.layout
    elif pathname == '/apps/homeweekly':
        return homeweekly.layout
    elif pathname == '/apps/homehourly':
        return homehourly.layout
    else:
        return home.layout

if __name__ == '__main__':
     app.run_server(host='127.0.0.1', debug=False,dev_tools_ui=False,dev_tools_props_check=False)
