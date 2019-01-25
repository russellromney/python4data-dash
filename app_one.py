import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.exceptions import PreventUpdate
from dash.dependencies import Output,Input,State
import pandas as pd
import numpy as np
import base64
import plotly.plotly as py
import plotly.graph_objs as go
from datetime import date,timedelta


chuck_path = 'chuck.png'
encoded_chuck = base64.b64encode(open(chuck_path,'rb').read())


# make our dash app
app = dash.Dash()

# app layout
app.layout = html.Div(children=[
    dcc.Input(
        id='input',
        style=dict(width="100%",fontSize='25px')
    ),
    html.Div(id='output-div')
])

@app.callback(output=Output('output-div','children'),inputs=[Input('input','value')])
def return_output(message):
    if 'chuck' in message:
        return html.Img(
            src='data:image/png;base64,{}'.format(encoded_chuck.decode())
        )
    
    return message 



if __name__ == "__main__":
    app.run_server()