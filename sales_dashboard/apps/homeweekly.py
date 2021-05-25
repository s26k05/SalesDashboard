import dash_html_components as html
import dash_bootstrap_components as dbc
  
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H5(children='Which operation do you want to perform?  '
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([

            dbc.Col(dbc.Card(children=[html.H3(children='Weekly data',
                                               className="text-center"),
                                         dbc.Row([dbc.Col(dbc.Button("visualize", href="/apps/weeklyV",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                dbc.Col(dbc.Button("predict", href="/apps/weeklyP",
                                                                   color="primary"),
                                                        className="mt-3"),
                                                        ], justify="center")
                                       ],
                             body=True, color="dark", outline=True)
                    , width=10, className="mb-4"),
        ], className="mb-5"),

    ])

])
