# app4
# interactive charts with regression


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
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

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
    html.H1('Select a variable to plot and do regression:'),    
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
    X = np.array(df[col_name]).reshape(-1,1)
    Y = df['Chance of Admit']
    x_train,x_test,y_train,y_test = train_test_split(X,Y,test_size=.35)
    lr = LinearRegression()
    lr.fit(x_train,y_train)
    pred = lr.predict(x_test)
    r_squared = r2_score(y_test,pred)
    r_squared = round(r_squared,3)
    coef = lr.coef_[0]
    coef = round(coef,3)

    def data_to_plotly(x):
        k = []
        for i in range(0, len(x)):
            k.append(x[i][0])
        return k

    trace1 = go.Scatter(
        y=y_test, # y column
        x=data_to_plotly(x_test), # x column
        mode='markers',
        name='actual'
    )
    trace2 = go.Scatter(
        x = data_to_plotly(x_test),
        y = pred,
        mode='lines',
        name = 'predicted'
    )
    
    # 
    data = [trace1,trace2]

    # define the layout object
    layout = go.Layout(
        title='Admits vs {}'.format(col_name),
        annotations = [
            dict(
                x=.5,
                y=.1,
                xref='paper',
                yref='y',
                text="R^2: {}".format(r_squared),
                showarrow=False,
            ),
            dict(
                x=.5,
                y=.2,
                xref='paper',
                yref='y',
                text = 'Coefficient: {}'.format(coef),
                showarrow=False
            )
        ]
    )

    fig = go.Figure(data,layout) # create the figure
    
    return fig


if __name__=='__main__':
    app.run_server(
        debug=True,
        port = 8002
    )

