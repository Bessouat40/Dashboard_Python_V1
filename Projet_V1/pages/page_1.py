import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import pandas as pd
import plotly.express as px

colors = {
    'background': '#636161',
    'text': '#B2ACAB'
}

youth = pd.read_csv("C:/Users/Utilisateur/Desktop/cours/Python_pour_la_data/projet/youth_alcohol/bdd_utiles/youth_cont.csv")
fig = px.choropleth(youth , locations='Alpha-3 code', color='15-19 years old, current drinkers both sexes (%)',
                           color_continuous_scale=px.colors.sequential.Greys,
                           range_color=(0, 100),
                           scope="world", color_discrete_map = colors['background'],
                           labels={'unemp':'unemployment rate'}
                          )
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

jeunes_morts = pd.read_csv("C:/Users/Utilisateur/Desktop/cours/Python_pour_la_data/projet/youth_alcohol/bdd_utiles/jeunes_morts_cont.csv")
pays_possibles = jeunes_morts.Country.unique()

page_1_layout = html.Div(style = {'backgroundColor' : colors['background']}, children = [
    html.H1(style={
                'textAlign': 'center',
                'background' : colors['background'],
                'color': colors['text']},
                children = "Visualisation au niveau mondial"),



    html.Div(style = {'backgroundColor' : colors['background']}, children=[
        html.H4(children="Part des jeunes qui consomment de l'alcool dans le monde :" ,
                style={
                    #'textAlign': 'center',
                    'color': colors['text']}),
        dcc.Graph(
            style = {'backgroundColor' : colors['background']},
            id='map',
            figure=fig
        ),
        html.H4(children="Evolution des accidents en voiture chez les jeunes dans chaque pays :" ,
                style={
                    #'textAlign': 'center',
                    'color': colors['text']}),
        html.Div(style = {'backgroundColor' : colors['background']},id='page-3-content' )
    ]),

    html.Div([
        html.Div([
            dcc.Dropdown(style = {'backgroundColor' : colors['background']},
                id='xaxis-column',
                options=[{'label': str(i), 'value': str(i)} for i in pays_possibles],
                value='Australia'
            )
        ],
        style={'width': '95%', 'display': 'inline-block'}),

            dcc.Graph(style = {'backgroundColor' : colors['background']},id='indicator-graphic'),
            ])
            ,
])
