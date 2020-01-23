import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
import numpy as np

import graphics

layout = html.Div(className='root', children=[

    html.Div(className='header', id='header', children=[
        html.Div([
            html.H1([
                'Empresas Abertas, Ativas e Fechadas'
            ])
        ])
    ]),

    html.Div(className='box', id='box', children=[

        html.Div(className='div1', id='div1', children=[

            html.Div(className='div1-1', id='div1-1', children=[
                html.Div(className='graphic1', id='graphic1', children=[
                    dcc.Graph(
                        figure=graphics.fig1
                    )
                ])
            ]),

            html.Div(className='div1-2', id='div1-2', children=[
                html.Div(className='graphic2', id='graphic2', children=[
                    dcc.Graph(
                        figure=graphics.fig2
                    )
                ])
            ])

        ]),

        html.Div(className='div2', id='div2', children=[
            
            html.Div(className='div2-1', id='div2-1', children=[

            ]),

            html.Div(className='div2-2', id='div2-2', children=[

                html.Div(className='div2-2-1', id='div2-2-1', children=[

                ]),

                html.Div(className='div2-2-2', id='2-2-2', children=[

                ])

            ])

        ])

    ])

])