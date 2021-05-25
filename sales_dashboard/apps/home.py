import dash_html_components as html
import dash_bootstrap_components as dbc
  
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("Welcome to the sales dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='We help you talk to your data... You only need to click, watch and learn '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(dbc.Card(children=[html.H3(children='hourly sales',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Click here", href="/apps/homehourly",
                                                                   color="primary"),
                                                        className="mt-1"),
                                                        ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-1"),

            dbc.Col(dbc.Card(children=[html.H3(children='daily sales',
                                               className="text-center"),
                                         dbc.Row([dbc.Col(dbc.Button("Click here", href="/apps/homedaily",
                                                                   color="primary"),
                                                        className="mt-1"),
                                                        ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-1"),

            dbc.Col(dbc.Card(children=[html.H3(children='weekly sales',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Click here", href="/apps/homeweekly",
                                                                   color="primary"),
                                                        className="mt-1"),
                                                        ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-1"),
            dbc.Col(dbc.Card(children=[html.H3(children='monthly sales',
                                               className="text-center"),
                                       dbc.Row([dbc.Col(dbc.Button("Click here", href="/apps/homemonthly",
                                                                   color="primary"),
                                                        className="mt-1"),
                                                        ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=6, className="mb-1"),
        ], className="mb-4"),

        
    ])

])
