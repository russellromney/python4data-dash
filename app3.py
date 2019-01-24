# app3
# interactive charts


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


# load data
df = pd.read_csv('Admission_Predict_Ver1.1.csv')
df.columns = [x.strip() for x in df.columns]
df['SOP_LOR'] = df.SOP+df.LOR
df['SOP_LOR_UR'] = df.SOP + df.LOR + df['University Rating']
df['LOR_UR'] = df.LOR + df['University Rating']
df['SOP_UR'] = df.SOP + df['University Rating']

#####
# data citation:
# Mohan S Acharya, Asfia Armaan, Aneeta S Antony : A Comparison 
# of Regression Models for Prediction of Graduate Admissions, 
# IEEE International Conference on Computational Intelligence 
# in Data Science 2019
#####


app = dash.Dash()

app.title = "Russell's Dash App"

app.layout = html.Div([
    html.H1('Select a variable to plot:'),
    dcc.Dropdown(
        id='column-input',
        options = [
            dict(label=col,value=col) for col in df.columns
        ],
        value='CGPA'
    ),
    dcc.Graph(
        id='the-graph',
    )
])

# take in the graph and return the graph with new column and correct title
@app.callback(
    Output('the-graph','figure'),
    [Input('column-input','value')])
def return_new_graph_figure(col_name):
    trace = go.Scatter(
        y=df['Chance of Admit'], # y column
        x=df[col_name], # x column
        mode='markers'
    )
    
    # 
    data = [trace]

    # define the layout object
    layout = go.Layout(
        title='admits'
    )

    fig = go.Figure(data,layout) # create the figure
    
    return fig


if __name__=='__main__':
    app.run_server(
        debug=True,
        port = 8002
    )

