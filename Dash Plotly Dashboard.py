#Read Description
#Read Description
#Read Description
#Read Description

import dash
from dash import dcc, html, Dash
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import pandas as pd
from pandas.core.common import flatten
import numpy as np

#Presets

tabs_styles = {
    'height': '44px'
}
tab_style = {
    'borderBottom': '1px solid #d6d6d6',
    'padding': '6px',
    'fontWeight': 'bold',
    'backgroundColor':'black',
    'color':'white'
}

tab_selected_style = {
    'borderTop': '1px solid #d6d6d6',
    'borderBottom': '1px solid #d6d6d6',
    'backgroundColor': 'black',
    'color': 'white',
    'padding': '6px'
}



data_set1 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set2 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set3 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set4 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set5 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set6 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set7 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set8 =  pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set9 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set10 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set11 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set12 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set13 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])
data_set14 = pd.read_csv('DATA DIRECTORY', parse_dates=['Date'],index_col=['Date'])

#Data Presets

data_frame1 = pd.DataFrame()
data_frame1['Column Title'] = data_set1['Quantity']
data_frame1['Column Title'] = data_set2['Quantity']
data_frame1['Column Title'] = data_set3['Quantity']
data_frame1['Column Title'] = data_set4['Quantity']
data_frame1['Column Title'] = data_set5['Quantity']
data_frame1['Column Title'] = data_set6['Quantity']
data_frame1['Column Title'] = data_set7['Quantity']
data_frame1['Column Title'] = data_set8['Quantity']
data_frame1['Column Title'] = data_set9['Quantity']
data_frame1['Column Title'] = data_set10['Quantity']
data_frame1['Column Title'] = data_set11['Quantity']
data_frame1['Column Title'] = data_set12['Quantity']
data_frame1['Column Title'] = data_set13['Quantity']

app = dash.Dash(__name__,assets_folder='assets')



app.layout = html.Div([

    html.H1('Energy Trading Dashboard',style={'textAlign': 'center','color':'white','backgroundColor':'Black'}),
dcc.Tabs(id = 'main_tabs', 
    value = 'main_tab_comp',
        children = [
    dcc.Tab(label = 'Main Data', style = tab_style, selected_style = tab_selected_style,
            children = [
    html.Div([
        html.Div([
            html.H3('Column 1'),
            dcc.Dropdown(id='Select_Data',
               options=[
                        {"label": "Data Dropdown", "value": 'fig'},
                        {"label": "Data Dropdown", "value": 'fig2'},
                        {"label": "Data Dropdown", "value": 'fig3'},
                        {"label": "Data Dropdown", "value": 'fig4'},
                        {"label": "Data Dropdown", "value": 'fig5'},
                        {"label": "Data Dropdown", "value": 'fig6'},
                        {"label": "Data Dropdown", "value": 'fig7'},
                        {"label": "Data Dropdown", "value": 'fig8'},
                        {"label": "Data Dropdown", "value": 'fig9'},
                        {"label": "Data Dropdown", "value": 'fig10'},
                        {"label": "Data Dropdown", "value": 'fig11'},
                        {"label": "Data Dropdown", "value": 'fig12'},
                        {"label": "Data Dropdown", "value": 'fig13'},
                        ],
                multi=False,
                value='Default',
                style={'width': "60%"} 
                ),
    dcc.Graph(id = 'main_chart', figure = {}),
    dcc.Graph(id = 'second_chart', figure = {}),
    dcc.Graph(id = 'third_chart', figure = {})
    ], style={'display': 'inline-block','margin-left':'6em',"background": "black"}),


        html.Div([
            html.H3('Column 2'),
            dcc.Dropdown(id='Select_Data_2',
               options=[
                        {"label": "Data Dropdown", "value": 'fig'},
                        {"label": "Data Dropdown", "value": 'fig2'},
                        {"label": "Data Dropdown", "value": 'fig3'},
                        {"label": "Data Dropdown", "value": 'fig4'},
                        {"label": "Data Dropdown", "value": 'fig5'},
                        {"label": "Data Dropdown", "value": 'fig6'},
                        {"label": "Data Dropdown", "value": 'fig7'},
                        {"label": "Data Dropdown", "value": 'fig8'},
                        {"label": "Data Dropdown", "value": 'fig9'},
                        {"label": "Data Dropdown", "value": 'fig10'},
                        {"label": "Data Dropdown", "value": 'fig11'},
                        {"label": "Data Dropdown", "value": 'fig12'},
                        {"label": "Data Dropdown", "value": 'fig13'},
                        ],
                multi=False,
                value='Default', 
                style={'width': "60%"} 
                ),


    dcc.Graph(id = 'main_chart_2', figure = {}),
    dcc.Graph(id = 'second_chart_2', figure = {}),
    dcc.Graph(id = 'third_chart_2', figure = {})
    ], style={'display': 'inline-block','margin-left':'7em',"background": "black"}),

    ],style={'width':'100%', 'display':'inline-block',"background": "black"})
    ]),
    dcc.Tab(label = 'Other Data',
        style = tab_style,
        selected_style = tab_selected_style,
        children = [
    html.Div([
        dcc.Dropdown(id = 'Select Data Chart',
            options=[
                {'label':'Data Dropdown Tab 2','value':'other_fig'},
                {'label':'Data Dropdown Tab 2','value':'other_fig2'},
                {'label':'Data Dropdown Tab 2','value':'other_fig3'},
                ],
                multi=False,
                value='Default',
                style = {'width':'40%'}
                ),
        dcc.Graph(id = 'other_main', figure = {})
    ], style={'background':'black',
                'textAlign':'center',
                                    }
                )
    ]),
    dcc.Tab(label = 'Comparison Charts',
        style = tab_style,
        selected_style = tab_selected_style,
        children=[
                html.Div([
        dcc.Dropdown(id = 'main_comparison',
            options=[
                {'label': s, 'value':s} for s in data_frame1.columns
                    ],
            multi = True,
            value = 'First Data set',
            style = {'width':'50%'}
            ),
        dcc.Graph(id = 'compare_main', figure = {})
        ])
        ]
        
        )
        ], style=tabs_styles),

])



@app.callback(
    [Output('main_chart', 'figure'),
    Output('second_chart', 'figure'),
    Output('third_chart', 'figure')],
    Input('Select_Data', 'value')
)
def output_value(value):
    data = None
    data_p = None
    r_data_p = pd.DataFrame()
    data_p_index = None
    data_p_columns = None
    r_data_p_index = None
    r_data_p_columns = None
    xx = None
    yy = None
    chart_title = None
    
    if value == 'fig':
        data = data_set1
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig2':
        data = data_set2
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    if value == 'fig3':
        data = data_set3
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

 
    if value == 'fig4':
        data = data_set4
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig5':
        data = data_set5
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    if value == 'fig6':
        data = data_set6
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig7':
        data = data_set7
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig8':
        data = data_set9
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig9':
        data = data_set8
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig10':
        data = data_set10
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig11':
        data = data_set11
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig12':
        data = data_set12
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    if value == 'fig13':
        data = data_set13
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    try:
        data_p[2021] = data.loc['2021'].Quantity.values
        data_p[2016] = data.loc['2016'].Quantity.values
        data_p[2010] = data.loc['2010'].Quantity.values
        data_p[2004] = data.loc['2004'].Quantity.values
        data_p[1999] = data.loc['1999'].Quantity.values
        data_p[1993] = data.loc['1993'].Quantity.values
        data_p[1988] = data.loc['1988'].Quantity.values
        r_data_p = data_p.copy()
    except:
        pass



    for i in r_data_p.columns:

        r_data_p[i] = r_data_p[i]/r_data_p[i].iloc[0] * 100

    fig = px.line(data,x = xx, y = yy)

    fig.update_layout(
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text': chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    ),
    fig.update_traces(line_color = '#FFA500'),

    fig2 = px.line(data_p, x=data_p_index, y=data_p_columns)

    fig2.update_layout(
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text' : chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

    fig3 = px.line(r_data_p, x=r_data_p_index, y=r_data_p_columns)

    fig3.update_layout(
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text': chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )


    return fig, fig2, fig3


@app.callback(
    [Output('main_chart_2', 'figure'),
    Output('second_chart_2', 'figure'),
    Output('third_chart_2', 'figure')],
    Input('Select_Data_2', 'value')
)
def output_value(value):
    data = None
    data_p = None
    r_data_p = pd.DataFrame()
    data_p_index = None
    data_p_columns = None
    r_data_p_index = None
    r_data_p_columns = None
    xx = None
    yy = None
    chart_title = None
    
    if value == 'fig':
        data = data_set1
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig2':
        data = data_set2
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    if value == 'fig3':
        data = data_set3
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

 
    if value == 'fig4':
        data = data_set4
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig5':
        data = data_set5
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    if value == 'fig6':
        data = data_set6
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig7':
        data = data_set7
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig8':
        data = data_set9
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig9':
        data = data_set8
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig10':
        data = data_set10
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns



    if value == 'fig11':
        data = data_set11
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns


    if value == 'fig12':
        data = data_set12
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    if value == 'fig13':
        data = data_set13
        chart_title = 'Chart Title'
        xx = data.index
        yy = data['Quantity']
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

    try:
        data_p[2021] = data.loc['2021'].Quantity.values
        data_p[2016] = data.loc['2016'].Quantity.values
        data_p[2010] = data.loc['2010'].Quantity.values
        data_p[2004] = data.loc['2004'].Quantity.values
        data_p[1999] = data.loc['1999'].Quantity.values
        data_p[1993] = data.loc['1993'].Quantity.values
        data_p[1988] = data.loc['1988'].Quantity.values
        r_data_p = data_p.copy()
    except:
        pass

    for i in r_data_p.columns:

        r_data_p[i] = r_data_p[i]/r_data_p[i].iloc[0] * 100


    fig = px.line(data,x = xx, y = yy)

    fig.update_layout(
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text': chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    ),
    fig.update_traces(line_color = '#FFA500'),

    fig2 = px.line(data_p, x=data_p_index, y=data_p_columns)

    fig2.update_layout(
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text' : chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )

    fig3 = px.line(r_data_p, x=r_data_p_index, y=r_data_p_columns)

    fig3.update_layout(
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        width=800,
        height=800,
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text': chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )


    return fig, fig2, fig3

@app.callback(
    Output('other_main', 'figure'),
    Input('Select Data Chart', 'value')
    
)
def output_single(value):
    data = pd.DataFrame()
    chart_title = None
    if value == 'other_fig':
        data = data_set14
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Chart Title', x=data['Date'],
                            y=data['Column Name']))
        fig.add_trace(go.Bar(name='Chart Title', x=data['Date'], 
                            y=data['Net Stock (Refinery & Tank Farms)'],
                            hovertext=data['Column Name']
                            ))
        fig.update_layout(plot_bgcolor = 'Black',
        paper_bgcolor = 'Black',
        font_color = 'White',
        title_font_color = 'White'
        )
        return fig

    if value == 'other_fig2':
        data = data_set2 + data_set4 + data_set6
        chart_title = 'Chart Title'

    if value == 'other_fig3':
        data = data_set2 + data_set4 + data_set6 + data_set5
        chart_title = 'Chart Title'
    combo_list = []
    try:
        for x in np.arange(1990,2023):    
            combo_list.append(data.loc[f'{x}'].values - data.loc[f'{x}'].iloc[0].values)
    except:
        pass

    big4_values = list(flatten(combo_list))
    big_df = data.loc['1990':].copy()

    big_df['Quantity'] = big4_values

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=big_df.index, y=big_df['Quantity'], fill='tozeroy'))

    fig.update_layout(
        autosize=True,
        font_color = 'White',
        title_font_color = 'White',
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor = 'Black',
        title={
        'text': chart_title,
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    fig.add_hline(y=0)
    fig.update_traces(line_color = '#FFA500')

    return fig

@app.callback(
    Output('compare_main','figure'),
    Input('main_comparison','value'),
)

def display_graph(*value):
    df = pd.DataFrame()
    for x in value:
        df[x] = data_frame1[x]
    
    fig = px.line(df)

    fig.update_layout(
        xaxis_title = 'Date',
        yaxis_title = 'Quantity',
        autosize=True,
        font_color='White',
        title_font_color = 'White',
        margin=dict(l=50, r=50, b=100, t=100, pad=4),
        paper_bgcolor="Black",
        plot_bgcolor='Black',
        title={
        'text': 'Comparison Charts',
        'y':0.96,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'}
    )
    
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
