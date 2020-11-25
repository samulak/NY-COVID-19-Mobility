import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
from urllib.request import urlopen
import datetime
from datetime import datetime, timedelta, date
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
    counties = json.load(response)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.FLATLY])
server = app.server
# --------------------------------Data Load------------------------------------
data_frame = pd.read_csv('New_York_State_Statewide_COVID-19_Testing_FIPS_3_Day.csv')
copy_data_frame = data_frame.copy()

mobility_data_frame = pd.read_csv("2020_US_Region_Mobility_Report.csv")

New_York_Mobility_Data = mobility_data_frame[mobility_data_frame['sub_region_1'] == 'New York']
New_York_Mobility_Data_Frame_None = New_York_Mobility_Data.where(pd.notnull(New_York_Mobility_Data), None)
# ------------------------------------------------------------------------------

#-------------------------------Helper Code-------------------------------------
start_date = date(2020, 3, 1) #Start Date
end_date = date(2020, 11, 5) #End Date
delta = timedelta(days=1)
temp_start = date(2020, 3, 1)

A_week_list = []
while start_date <= end_date:
    A_week_list.append(str(start_date))
    start_date += delta
# ------------------------------------------------------------------------------

#-----------------------------Cards---------------------------------------------

#-----------------------------Introduction Tab----------------------------------

tab_card = dbc.Card([dbc.Tabs(
            [
                dbc.Tab(label="Introduction", label_style={"color": "#18BC9C"},tab_id="tab-1", children = [
                dbc.Card([dbc.CardBody([dbc.Col(html.H1("Effects of Transportation on COVID-19 Cases", className="card-title"), width = {'size': 7, 'offset': 3}),
                                        dbc.Col(html.H5("Team members: Brandon Lao, Gareth Petterson, Javed Rafiuddin, Adam Samulak", className="card-title"), width = {'size': 7, 'offset': 4})
                        ]),
                ]),


                dbc.Card([dbc.CardBody([dbc.Row([dbc.Col(html.H2("Summary:", className="card-title"),width = {'size': 8, 'offset': 0}),
                                        dbc.Col(html.H4("In a world that continues to be affected by COVID-19, it’s important to know the effects of various approaches to resisting its spread and effect on the populace. Our study examines transit data from New York State and New York City to determine the effectiveness of travel restrictions imposed in these areas. The main method of examination used is a map of the state divided into counties, which can be individually examined to compare the frequency of travel within the state against the number of infections. In the end, we found that reduced frequency of travel correlated strongly with a decrease in the rate of new infections, once the delay in the onset of symptoms and time to receive a positive result is considered. We believe that this solidifies the common idea that reduced movement of people results in lower infection rates thanks to less contact between infected and non-infected individuals.", className="card-text"),width = {'size': 8, 'offset': 0}),
                                        dbc.Col(dbc.CardImg(src="/assets/covid_image.jpg", top = True, bottom = False,
                                                                            title="Image by: Alissa Eckert, MSMI; Dan Higgins, MAMS", alt='Learn Dash'),width = {'size': 3, 'offset': 1})

                ]),]),
                ],color ="primary",
                inverse=True,
                outline=False),

                html.Div(html.H5("Data refrences: COVID-19, Mobility"), style={"position": "fixed","bottom": 0,"left": 0,"right": 0,"padding": "1rem 1rem","background-color": "#ECF0F1",},
                ),]),
# ------------------------------------------------------------------------------

#-----------------------------Exploration Tab----------------------------------

                dbc.Tab(label="Data Exploration", label_style={"color": "#18BC9C"},tab_id="tab-2", children = [
                    dbc.Card([dbc.CardBody([html.H4("The left diagram shows a heatmap of  coronavirus infections throughout New York state. It provides two dopdowns, one for infections and second one for a date selection. Information about specific New York county and cases can be obtained by hoovering over the individual counties. The right diagram compares infection data in red and employee mobility in blue. There are two more dropdowns in this figure, first one is a county selector and the last one is a mobility scalar. County selector allows for individual county selection and mobility scalar is introduced in order to scale the mobility axis. Scalar is necessary due to some counties having a large number of cases that lead to drastic change in the y-axis scale. ", className="card-title")]),
                    ]),
#-----------------------------Map Graph Card----------------------------------
#-----------------------------Dropdown Info----------------------------------

                    dbc.Card([dbc.CardBody([dbc.Row([dbc.Col(html.H5("Select Infection Data"), style={"color": "white"},width={'size': 2, "offset": 1}),
                    dbc.Col(html.H5("Select Date"), style={"color": "white"},width={'size': 2, "offset": 1}),
                    dbc.Col(html.H5("Select County"), style={"color": "white"},width={'size': 1, "offset": 1}),
                    dbc.Col(html.H5("Select Infection Data"), style={"color": "white"},width={'size': 2, "offset": 0}),
                    dbc.Col(html.H5("Select Mobility Data Scalar"), style={"color": "white"},width={'size': 2, "offset": 0})
                    ]),




#------------------------------------------------------------------------------
#-----------------------------Dropdowns----------------------------------

                    dbc.Row([dbc.Col(dcc.Dropdown(id='cases_dropdown', placeholder='Select',
                                                 options=[{'label': 'New Infections', 'value': 'New Positives'},
                                                          {'label': 'Cumulative Number of Infections', 'value': 'Cumulative Number of Positives'}],
                                                          value = 'New Positives'),
                                    width={'size': 2, "offset": 1}
                    ),

                    dbc.Col(dcc.DatePickerSingle(
                    id='date-picker-single',
                    display_format='MMM Do, YY',
                    month_format='MMM Do, YY',
                    date=date(2020, 3, 1),
                    min_date_allowed = date(2020,3,1),
                    max_date_allowed = date(2020,10,12),
                    ),
                    width={'size': 2, "offset": 1}
                    ),
                    dbc.Col(dcc.Dropdown(id='county_dropdown', placeholder='Select',
                                         options=[{'label': 'Albany', 'value': 'Albany'},
                                                  {'label': 'Allegany', 'value': 'Allegany'},
                                                  {'label': 'Bronx', 'value': 'Bronx'},
                                                  {'label': 'Broome', 'value': 'Broome'},
                                                  {'label': 'Cattaraugus', 'value': 'Cattaraugus'},
                                                  {'label': 'Cayuga', 'value': 'Cayuga'},
                                                  {'label': 'Chautauqua', 'value': 'Chautauqua'},
                                                  {'label': 'Chenango', 'value': 'Chenango'},
                                                  {'label': 'Clinton', 'value': 'Clinton'},
                                                  {'label': 'Columbia', 'value': 'Columbia'},
                                                  {'label': 'Cortland', 'value': 'Cortland'},
                                                  {'label': 'Delaware', 'value': 'Delaware'},
                                                  {'label': 'Erie', 'value': 'Erie'},
                                                  {'label': 'Essex', 'value': 'Essex'},
                                                  {'label': 'Franklin', 'value': 'Franklin'},
                                                  {'label': 'Fulton', 'value': 'Fulton'},
                                                  {'label': 'Genesee', 'value': 'Genesee'},
                                                  {'label': 'Greene', 'value': 'Greene'},
                                                  {'label': 'Hamilton', 'value': 'Hamilton'},
                                                  {'label': 'Herkimer', 'value': 'Herkimer'},
                                                  {'label': 'Jefferson', 'value': 'Jefferson'},
                                                  {'label': 'Kings', 'value': 'Kings'},
                                                  {'label': 'Lewis', 'value': 'Lewis'},
                                                  {'label': 'Livingston', 'value': 'Livingston'},
                                                  {'label': 'Madison', 'value': 'Madison'},
                                                  {'label': 'Monroe', 'value': 'Monroe'},
                                                  {'label': 'Montgomery', 'value': 'Montgomery'},
                                                  {'label': 'Nassau', 'value': 'Nassau'},
                                                  {'label': 'New York', 'value': 'New York'},
                                                  {'label': 'Niagara', 'value': 'Niagara'},
                                                  {'label': 'Oneida', 'value': 'Oneida'},
                                                  {'label': 'Onondaga', 'value': 'Onondaga'},
                                                  {'label': 'Ontario', 'value': 'Ontario'},
                                                  {'label': 'Orange', 'value': 'Orange'},
                                                  {'label': 'Orleans', 'value': 'Orleans'},
                                                  {'label': 'Oswego', 'value': 'Oswego'},
                                                  {'label': 'Otsego', 'value': 'Otsego'},
                                                  {'label': 'Putnam', 'value': 'Putnam'},
                                                  {'label': 'Queens', 'value': 'Queens'},
                                                  {'label': 'Rensselaer', 'value': 'Rensselaer'},
                                                  {'label': 'Richmond', 'value': 'Richmond'},
                                                  {'label': 'Rockland', 'value': 'Rockland'},
                                                  {'label': 'Saratoga', 'value': 'Saratoga'},
                                                  {'label': 'Schenectady', 'value': 'Schenectady'},
                                                  {'label': 'Schoharie', 'value': 'Schoharie'},
                                                  {'label': 'Schuyler', 'value': 'Schuyler'},
                                                  {'label': 'Seneca', 'value': 'Seneca'},
                                                  {'label': 'St. Lawrence', 'value': 'St. Lawrence'},
                                                  {'label': 'Steuben', 'value': 'Steuben'},
                                                  {'label': 'Suffolk', 'value': 'Suffolk'},
                                                  {'label': 'Sullivan', 'value': 'Sullivan'},
                                                  {'label': 'Tioga', 'value': 'Tioga'},
                                                  {'label': 'Tompkins', 'value': 'Tompkins'},
                                                  {'label': 'Ulster', 'value': 'Ulster'},
                                                  {'label': 'Warren', 'value': 'Warren'},
                                                  {'label': 'Washington', 'value': 'Washington'},
                                                  {'label': 'Wayne', 'value': 'Wayne'},
                                                  {'label': 'Westchester', 'value': 'Westchester'},
                                                  {'label': 'Wyoming', 'value': 'Wyoming'},
                                                  {'label': 'Yates', 'value': 'Yates'}],
                                                  value = 'Albany'),
                            width={'size': 1, "offset": 1},

                    ),
                    dbc.Col(dcc.Dropdown(id='infection_dropdown', placeholder='Select',
                                                 options=[{'label': 'Raw Data', 'value': 'Raw'},
                                                          {'label': 'Three Day Moving Average', 'value': 'TD'}],
                                                          value = 'Raw'),
                                    width={'size': 2, "offset": 0}

                            ),
                    dbc.Col(dcc.Dropdown(id='Mobility_Scalar', placeholder='Select',
                                                 options=[{'label': '5', 'value': 5},
                                                          {'label': '10', 'value': 10}],
                                                          value = 1),
                                    width={'size': 2, "offset": 0}

                            ),

                                        ]),

                    dbc.Row([dbc.Col(dcc.Graph(id='NY_Map', figure={}),
                                width={'size': 6, "offset": 0}

                            ),
                            dbc.Col(dcc.Graph(id='Bar_graph', figure={}),
                                        width={'size': 3, "offset": 0})

                    ]),


                ]),
            ],color ="primary",
            inverse=False,
            outline=False)]
        ),
# ------------------------------------------------------------------------------

#-----------------------------Correlation Tab----------------------------------
                dbc.Tab(label="Correlation Analysis", label_style={"color": "#18BC9C"},tab_id="tab-3", children = [
                    dbc.Card([dbc.CardBody([html.H4("The left diagram shows daily infection data in red and employee mobility in blue. It is accompanied by two dropdowns: a county selector and a shift selector. Shift selector moves the infection graph backwards, in order to explore the lag between the infection and mobility. The correlation between infections and mobility is automatically updated on the right diagram. ", className="card-title")]),
                    ],
                    inverse=False,
                    outline=False),


                dbc.Card([dbc.CardBody([
                dbc.Row([dbc.Col(html.H5("Shift Selector"), style={"color": "white"},width={'size': 2, "offset": 1}),]),
                        dbc.Row([
                            dbc.Col(dcc.Dropdown(id='day_shift_dropdown', placeholder='Select number of days',
                                                         options=[{'label': '1', 'value': 1},
                                                                  {'label': '2', 'value': 2},
                                                                  {'label': '3', 'value': 3},
                                                                  {'label': '4', 'value': 4},
                                                                  {'label': '5', 'value': 5},
                                                                  {'label': '6', 'value': 6},
                                                                  {'label': '7', 'value': 7},
                                                                  {'label': '14', 'value': 14},
                                                                  {'label': '21', 'value': 21},
                                                                  {'label': '28', 'value': 28}],
                                                                  value = 1),
                                            width={'size': 2, "offset": 1}
                                    )
                        ]),

                        dbc.Row([dbc.Col(dcc.Graph(id='Shift_curves', figure={}),
                                    width={'size': 6, "offset": 0}

                                ),
                                dbc.Col(dcc.Graph(id='Correlation_line', figure={}),
                                            width={'size': 3, "offset": 0})

                        ]),


                ]),
                ],color ="primary",
                inverse=False,
                outline=False),



                    ]),
            ],
            id="tabs",
            active_tab="tab-1",

        ),
        html.Div(id="content"),
    ]),




#-----------------------------Application----------------------------------

app.layout = html.Div([
    dbc.Row([dbc.Col(tab_card)])
])
@app.callback(
    Output(component_id='NY_Map', component_property='figure'),
    Output(component_id='Bar_graph', component_property='figure'),
    Output(component_id='Shift_curves', component_property='figure'),
    Output(component_id='Correlation_line', component_property='figure'),
    [Input(component_id='date-picker-single', component_property='date'),
    Input(component_id='county_dropdown', component_property='value'),
    Input(component_id='infection_dropdown', component_property='value'),
    Input(component_id='Mobility_Scalar', component_property='value'),
    Input(component_id='cases_dropdown', component_property='value'),
    Input(component_id='day_shift_dropdown', component_property='value')],
    prevent_initial_call=False
)
def upadate_graph(date_selected, county_selcted, infection_dropdown, Mobility_Scalar, cases_dropdown, day_shift_dropdown):
    start_date = date(2020, 3, 1) #Start Date
    end_date = date(2020, 11, 5) #End Date
    delta = timedelta(days=1)
    temp_start = date(2020, 3, 1)

    A_week_list = []
    while start_date <= end_date:
        A_week_list.append(str(start_date))
        start_date += delta

    tmp = 0
    if Mobility_Scalar == None:
        tmp = 1
    else:
        tmp = Mobility_Scalar
    formatted_date = datetime.strptime(date_selected, '%Y-%m-%d').strftime('%m/%d/%Y')

    selected_date = copy_data_frame[copy_data_frame['Test Date'] == formatted_date]
    if cases_dropdown == 'New Positives':
        if(selected_date['New Positives'].max() == 0):
            scale_max = 1
        else:
            scale_max = selected_date['New Positives'].max()
    elif cases_dropdown == 'Cumulative Number of Positives':
        if(selected_date['Cumulative Number of Positives'].max() == 0):
            scale_max = 1
        else:
            scale_max = selected_date['Cumulative Number of Positives'].max()
    else:
        scale_max = 1

    #-----------------------Map Graph Tab 1----------------------------------
    fig = px.choropleth_mapbox(selected_date, geojson=counties, locations='FIPS', color=cases_dropdown,
                           color_continuous_scale="Reds",
                           width=900, height=800,
                           range_color=(0, scale_max),
                           mapbox_style="carto-darkmatter",
                           zoom=6, center = {"lat": 42.8, "lon": -76},
                           opacity=1,
                           hover_name="County", hover_data={'FIPS' : False, 'New Positives': True},
                           labels={'New Positives':'Cases', 'Cumulative Number of Positives':'Cases','FIPS':'County'},
                           title = "Figure 1"
                          )
    fig.update_layout(margin={"r":30,"t":50,"l":30,"b":50},
                 paper_bgcolor='#2C3E50',
                 plot_bgcolor='#2C3E50',
                 font_color="white",
                 )
    #-----------------------Line Graph Tab 1----------------------------------
    Week_list_temp = A_week_list

    time_covid_data = copy_data_frame[copy_data_frame['County'] == county_selcted]
    xxx = New_York_Mobility_Data_Frame_None[New_York_Mobility_Data_Frame_None['sub_region_2'] == str(county_selcted) + ' County']
    fig2 = go.Figure()
    if infection_dropdown == 'TD':
        fig2.add_trace(go.Scatter(x = xxx['date'], y=xxx['workplaces_percent_change_from_baseline'] * tmp, name = 'Mobility', line=dict(color='#3498DB', width=2)))
        fig2.add_trace(go.Scatter(x = Week_list_temp, y=time_covid_data['Three Day New Positives'], name = 'New Cases', line=dict(color='#E74C3C', width=2)))
        fig2.update_layout(plot_bgcolor="#2C3E50", paper_bgcolor="#2C3E50", font_color="white",width=900, height=800,title = "Figure 2")
        fig2.update_xaxes(showline=True, linewidth=1, linecolor='white')
        fig2.update_yaxes(showline=True, linewidth=1, linecolor='white')
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
        fig2.update_xaxes(title_text='Date')
        fig2.update_yaxes(title_text='')
        fig2.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
        fig2.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')

    elif infection_dropdown == 'Raw':
        fig2.add_trace(go.Scatter(x = xxx['date'], y=xxx['workplaces_percent_change_from_baseline'] * tmp, name = 'Mobility', line=dict(color='#3498DB', width=2)))
        fig2.add_trace(go.Scatter(x = Week_list_temp, y=time_covid_data['New Positives'], name = 'New Cases', line=dict(color='#E74C3C', width=2)))
        fig2.update_layout(plot_bgcolor="#2C3E50", paper_bgcolor="#2C3E50", font_color="white",width=900, height=800,title = "Figure 2")
        fig2.update_xaxes(showline=True, linewidth=1, linecolor='white')
        fig2.update_yaxes(showline=True, linewidth=1, linecolor='white')
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
        fig2.update_xaxes(title_text='Date')
        fig2.update_yaxes(title_text='')
        fig2.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
        fig2.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
    else:
        fig2.update_layout(plot_bgcolor="#2C3E50", paper_bgcolor="#2C3E50", font_color="white",width=900, height=800,title = "Figure 2")
        fig2.update_xaxes(showline=True, linewidth=1, linecolor='white')
        fig2.update_yaxes(showline=True, linewidth=1, linecolor='white')
        fig2.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
        fig2.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
        fig2.update_xaxes(title_text='Date')
        fig2.update_yaxes(title_text='')
        fig2.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
        fig2.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')

    #-----------------------Graphs Tab 2---------------------------------------
    new_stat_date = start_date
    if day_shift_dropdown != None:
        for days in range(day_shift_dropdown):
            new_stat_date -= delta

    A_week_list = []

    while start_date <= end_date:
        A_week_list.append(str(start_date))
        start_date += delta


    xxx = New_York_Mobility_Data_Frame_None[New_York_Mobility_Data_Frame_None['sub_region_2'] == 'Queens' + ' County']
    time_covid_data = copy_data_frame[copy_data_frame['County'] == 'Queens']

    if day_shift_dropdown != None:
        X = xxx['workplaces_percent_change_from_baseline'][0:250-day_shift_dropdown]+100
        Y = time_covid_data['New Positives'][day_shift_dropdown:250]
    else:
        X = xxx['workplaces_percent_change_from_baseline'][0:250]+100
        Y = time_covid_data['New Positives'][0:250]

    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(x = xxx['date'], y=X, name = 'Mobility', line=dict(color='#3498DB', width=2)))
    fig3.add_trace(go.Scatter(x = Week_list_temp, y=Y, name = 'New Cases', line=dict(color='#E74C3C', width=2)))
    fig3.update_layout(plot_bgcolor="#2C3E50", paper_bgcolor="#2C3E50", font_color="white", width=900, height=800,title = "Coronavirus Cases and Mobility in Queens County")
    fig3.update_xaxes(showline=True, linewidth=1, linecolor='white')
    fig3.update_yaxes(showline=True, linewidth=1, linecolor='white')
    fig3.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
    fig3.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
    fig3.update_xaxes(title_text='Date')
    fig3.update_yaxes(title_text='')
    fig3.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
    fig3.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')

    fig4 = px.scatter(x=X, y=Y, trendline="ols")
    fig4.update_layout(plot_bgcolor="#2C3E50", paper_bgcolor="#2C3E50", font_color="white", width=900, height=800, title = "Correlation between Coronavirus Cases and Mobility")
    fig4.update_xaxes(showline=True, linewidth=1, linecolor='white')
    fig4.update_yaxes(showline=True, linewidth=1, linecolor='white')
    fig4.update_xaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
    fig4.update_yaxes(showgrid=True, gridwidth=1, gridcolor='#2C3E50')
    fig4.update_xaxes(title_text='Mobility')
    fig4.update_yaxes(title_text='Coronavirus Cases')
    fig4.update_xaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
    fig4.update_yaxes(zeroline=True, zerolinewidth=1, zerolinecolor='white')
    return fig, fig2, fig3, fig4
# ------------------------------------------------------------------------------


if __name__ == "__main__":
    app.run_server(debug=False)