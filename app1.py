# app1
# basic dash dashboard

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


chuck_path='chuck.png'
encoded_chuck = base64.b64encode(open(chuck_path,'rb').read())


app = dash.Dash()

app.layout = html.Div([
    dcc.Input(
        id='message-input',
        style=dict(fontSize='50px')
    ),
    html.Div(
        children=["Hello, world!"],
        id='message-output',
        style=dict(fontSize='50px')
    ),
])




@app.callback(
    Output('message-output','children'),
    [Input('message-input','value')])
def show_new_message(message):
    if message == '' or message==None:
        return 'Hello, world!'
    if 'idaho' in message.lower():
        return html.Img(src='data:image/png;base64,{}'.format(encoded_chuck.decode()))
    return message + " -- that is what you typed!"






if __name__=='__main__':
    app.run_server(
        debug=True,
        port = 8002
    )

