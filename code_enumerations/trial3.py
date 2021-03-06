import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque

# X = deque(maxlen=20)
# Y = deque(maxlen=20)
X = []
Y = []
Z = []
X.append(random.uniform(50,60))
Y.append(random.uniform(50,55))
Z.append(random.uniform(50,55))

app = dash.Dash(__name__)
app.layout = html.Div([
    
    dcc.Graph(
        id='live-graph',
        animate=True
    ),

    dcc.Interval(
        id='graph-update',
        interval=1000,
        n_intervals=0
    ),
    ]
)

@app.callback(
    Output('live-graph', 'figure'),
    [Input('graph-update','n_intervals')]
)
def update_graph(n):
    global X
    global Y
    global Z
    X.append(X[-1]+(random.uniform(-5,5)))
    Y.append(Y[-1]+(random.uniform(-5,5)))
    Z.append(Z[-1]+(random.uniform(-5,5)))

    data = go.Scatter3d(
        x = list(X),
        y = list(Y),
        z = list(Z),
        name = 'Scatter',
        mode = 'lines+markers'
    )

    # return {'data':[data],
    #         'layout': go.Layout(xaxis=dict(range=[1, 100]),
    #                             yaxis=dict(range=[1, 100]),
    #                             )
    #         }

    return {'data':[data],
            'layout': go.Layout(
                margin=dict(
                    l=0,
                    r=0,
                    b=0,
                    t=0
                )
            )
            }

if __name__== '__main__':
    app.run_server(debug=True)