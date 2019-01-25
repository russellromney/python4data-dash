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

df = pd.read_csv('Admission_Predict_Ver1.1.csv')
df.columns = [x.strip() for x in df.columns]
df['SOP_LOR'] = df.SOP+df.LOR
df['SOP_LOR_UR'] = df.SOP + df.LOR + df['University Rating']
df['LOR_UR'] = df.LOR + df['University Rating']
df['SOP_UR'] = df.SOP + df['University Rating']



app = dash.Dash()

app.layout = html.Div([
    dcc.Graph(
        id='the-graph',
        figure = go.Figure(
            data = [
                go.Scatter(
                    x = df['CGPA'],
                    y = df['Chance of Admit'],
                    mode = 'markers'
                )
            ],
            layout = go.Layout(
                title='my title'
            )
        )
    )
])

if __name__=='__main__':
    app.run_server()

