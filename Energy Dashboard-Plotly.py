#README!!!
#README!!!
#README!!!
#README!!!

#THIS DASHBOARD WAS MADE TO VISUALIZE THE EIA WEEKLY CRUDE OIL REPORT + OTHERR ENERGY DATA
#THIS MAY ALSO SERVE AS A TEMPLATE FOR OTHERS!!! HAPPY CODING!

import dash
from dash import dcc, html, Dash
import plotly.express as px
import plotly.graph_objects as go
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

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


#Crude Oil total
cl_total_data = pd.read_csv('U.S. CL Stock Ending Total Weekly.csv', parse_dates=['Date'],index_col=['Date'])

#Cl Commercial Total
cl_comm_total = pd.read_csv('U.S. CL Stock Ending Commercial excl. SPR Wkly.csv', parse_dates=['Date'], index_col=['Date'])

#CL SPR Total
cl_spr = pd.read_csv('U.S. CL Stock Ending incl. SPR Weekly.csv', parse_dates=['Date'],index_col=['Date'])


##Other Stock
#Total Motor Gasoline
motor_gas_total = pd.read_csv('U.S. Ending Total Gasoline Weekly.csv',parse_dates=['Date'], index_col = ['Date'])

#Kerosene Type Jet Fuel
kerosene_jet_fuel = pd.read_csv('U.S. Ending Total Kerosene Type Jet Fuel Weekly.csv',parse_dates=['Date'], index_col = ['Date'])

#Distillate Fuel Oil
distillate_fuel_oil = pd.read_csv('U.S. Distillate Fuel Oil Stock Ending Weekly.csv',parse_dates=['Date'], index_col = ['Date'])



#CL Supply

#Domestic Production
us_dom_prod = pd.read_csv('U.S. Domestic CL Production Weekly.csv',parse_dates=['Date'], index_col = ['Date'])

#Alaska Production
alaska_prod =  pd.read_csv('U.S. Alaska Production.csv',parse_dates = ['Date'], index_col = ['Date'])

#Lower 48 Production
lower_48_prod = pd.read_csv('U.S. Lower 48 Field Production.csv',parse_dates = ['Date'], index_col = ['Date'])

#CL Input To Refineries
cl_input = pd.read_csv('U.S. Refiner Net Input of CL.csv',parse_dates = ['Date'], index_col = ['Date'])



#CL Net Imports
cl_net_imports = pd.read_csv('U.S. Net Imports incl. SPR CL Weekly.csv', parse_dates = ['Date'],index_col= ['Date'])

#CL Imports
cl_imports = pd.read_csv('U.S. Commercial CL Imports excl. SPR.csv', parse_dates=['Date'],index_col=['Date'])

#CL Exports
cl_exports = pd.read_csv('U.S. CL ExportsWeekly.csv', parse_dates=['Date'],index_col=['Date'])

#Working Storage
wstorage_df = pd.read_csv('EIA Crude Oil Working Storage.csv', parse_dates=['Date'])

#Data Presets

comp_set = pd.DataFrame()
comp_set['Crude Oil Total Inventory'] = cl_total_data['Quantity']
comp_set['Crude Oil Commercial Total'] = cl_comm_total['Quantity']
comp_set['Crude Oil SPR'] = cl_spr['Quantity']
comp_set['Motor Gas Total'] = motor_gas_total['Quantity']
comp_set['Kerosene Jet Fuel'] = kerosene_jet_fuel['Quantity']
comp_set['Distillate Fuel Oil'] = distillate_fuel_oil['Quantity']
comp_set['US Domestic Prod.'] = us_dom_prod['Quantity']
comp_set['Alaska Production'] = alaska_prod['Quantity']
comp_set['Lower 48 Production'] = lower_48_prod['Quantity']
comp_set['Crude Oil Refinery Input'] = cl_input['Quantity']
comp_set['Crude Oil Net Imports'] = cl_net_imports['Quantity']
comp_set['Crude Oil Imports'] = cl_imports['Quantity']
comp_set['Crude Oil Exports'] = cl_exports['Quantity']

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
                        {"label": "EIA CL Total Stock", "value": 'fig'},
                        {"label": "EIA CL Commercial Stock", "value": 'fig2'},
                        {"label": "EIA CL SPR Stock", "value": 'fig3'},
                        {"label": "EIA Motor Gasoline Total", "value": 'fig4'},
                        {"label": "EIA Kerosene Type Jet Fuel", "value": 'fig5'},
                        {"label": "EIA Distillate Fuel Oil", "value": 'fig6'},
                        {"label": "EIA US Domestic Production", "value": 'fig7'},
                        {"label": "EIA US Lower 48 Production", "value": 'fig8'},
                        {"label": "EIA US Alaska Production", "value": 'fig9'},
                        {"label": "EIA CL Input to Refineries", "value": 'fig10'},
                        {"label": "EIA US CL Net Imports", "value": 'fig11'},
                        {"label": "EIA US CL Imports", "value": 'fig12'},
                        {"label": "EIA US CL Exports", "value": 'fig13'},
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
                        {"label": "EIA CL Total Stock", "value": 'fig'},
                        {"label": "EIA CL Commercial Stock", "value": 'fig2'},
                        {"label": "EIA CL SPR Stock", "value": 'fig3'},
                        {"label": "EIA Motor Gasoline Total", "value": 'fig4'},
                        {"label": "EIA Kerosene Type Jet Fuel", "value": 'fig5'},
                        {"label": "EIA Distillate Fuel Oil", "value": 'fig6'},
                        {"label": "EIA US Domestic Production", "value": 'fig7'},
                        {"label": "EIA US Lower 48 Production", "value": 'fig8'},
                        {"label": "EIA US Alaska Production", "value": 'fig9'},
                        {"label": "EIA CL Input to Refineries", "value": 'fig10'},
                        {"label": "EIA US CL Net Imports", "value": 'fig11'},
                        {"label": "EIA US CL Imports", "value": 'fig12'},
                        {"label": "EIA US CL Exports", "value": 'fig13'},
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
                {'label':'EIA CL Storage Capacity','value':'other_fig'},
                {'label':'US Big 3','value':'other_fig2'},
                {'label':'US Big 4','value':'other_fig3'},
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
                {'label': s, 'value':s} for s in comp_set.columns
                    ],
            multi = True,
            value = 'Crude Oil Total Inventory',
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
    chart_title = None
    r_data_p = pd.DataFrame()
    data_p_index = None
    data_p_columns = None
    r_data_p_index = None
    r_data_p_columns = None
    xx = None
    yy = None

    
    if value == 'fig':
        data = cl_total_data
        chart_title = 'CL Stock Complete'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig2':
        data = cl_comm_total
        chart_title = 'CL Commercial Stock'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig3':
        data = cl_spr
        chart_title = 'CL SPR Stock'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig4':
        data = motor_gas_total
        chart_title = 'Motor Gas Stock Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig5':
        data = kerosene_jet_fuel
        chart_title = 'Kerosene Jet Fuel Stock Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig6':
        data = distillate_fuel_oil
        chart_title = 'Distillate Fuel Oil Stock Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig7':
        data = us_dom_prod
        chart_title = 'US CL Production Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig8':
        data = lower_48_prod
        chart_title = 'US Lower 48 Production Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig9':
        data = alaska_prod
        chart_title = 'US Alaska Production Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig10':
        data = cl_input
        chart_title = 'US CL Input to Refineries'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig11':
        data = cl_net_imports
        chart_title = 'US CL Net Imports Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig12':
        data = cl_imports
        chart_title = 'US CL Imports Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig13':
        data = cl_exports
        chart_title = 'US CL Exports Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')



    try:
        xx = data.index
        yy = data['Quantity']
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

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
        data = cl_total_data
        chart_title = 'CL Stock Complete'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig2':
        data = cl_comm_total
        chart_title = 'CL Commercial Stock'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig3':
        data = cl_spr
        chart_title = 'CL SPR Stock'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')
 
    if value == 'fig4':
        data = motor_gas_total
        chart_title = 'Motor Gas Stock Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig5':
        data = kerosene_jet_fuel
        chart_title = 'Kerosene Jet Fuel Stock Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig6':
        data = distillate_fuel_oil
        chart_title = 'Distillate Fuel Oil Stock Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig7':
        data = us_dom_prod
        chart_title = 'US CL Production Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig8':
        data = lower_48_prod
        chart_title = 'US Lower 48 Production Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig9':
        data = alaska_prod
        chart_title = 'US Alaska Production Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig10':
        data = cl_input
        chart_title = 'US CL Input to Refineries'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig11':
        data = cl_net_imports
        chart_title = 'US CL Net Imports Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig12':
        data = cl_imports
        chart_title = 'US CL Imports Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    if value == 'fig13':
        data = cl_exports
        chart_title = 'US CL Exports Total'
        data_p = pd.pivot_table(data, index = data.index.isocalendar().week , columns = data.index.year, values = 'Quantity')

    try:
        xx = data.index
        yy = data['Quantity']
        data_p_index = data_p.index
        data_p_columns = data_p.columns
        r_data_p = data_p.copy()
        r_data_p_index = r_data_p.index
        r_data_p_columns = r_data_p.columns

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
        data = wstorage_df
        fig = go.Figure()
        fig.add_trace(go.Bar(name='Working Storage Capacity', x=data['Date'],
                            y=data['Working Storage Capacity']))
        fig.add_trace(go.Bar(name='Net CL Stock', x=data['Date'], 
                            y=data['Net Stock (Refinery & Tank Farms)'],
                            hovertext=data['Utilization Rate']
                            ))
        fig.update_layout(plot_bgcolor = 'Black',
        paper_bgcolor = 'Black',
        font_color = 'White',
        title_font_color = 'White'
        )
        return fig

    if value == 'other_fig2':
        data = cl_comm_total + motor_gas_total + distillate_fuel_oil
        chart_title = 'US Big 3 (CL + Gas + Dist)'

    if value == 'other_fig3':
        data = cl_comm_total + motor_gas_total + distillate_fuel_oil + kerosene_jet_fuel
        chart_title = 'US Big 4 (CL + Gas + Dist + K. Jet)'
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
        df[x] = comp_set[x]
    
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
