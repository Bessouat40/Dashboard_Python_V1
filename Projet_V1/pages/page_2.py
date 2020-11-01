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
jeunes_morts = pd.read_csv("C:/Users/Utilisateur/Desktop/cours/Python_pour_la_data/projet/youth_alcohol/bdd_utiles/jeunes_morts_cont.csv")
youth = pd.read_csv("C:/Users/Utilisateur/Desktop/cours/Python_pour_la_data/projet/youth_alcohol/bdd_utiles/youth_cont.csv")
annees = jeunes_morts.Year.unique()
moy = youth.groupby('Continent').mean()
fig = px.bar(moy , y = '15-19 years old, current drinkers both sexes (%)' , color = '15-19 years old, current drinkers both sexes (%)' , color_continuous_scale=px.colors.sequential.Greys)
fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

page_2_layout = html.Div(style = {'backgroundColor' : colors['background']}, children=[
    html.H1(children="Visualisation au niveau continental" ,
            style={
                'textAlign': 'center',
                'color': colors['text']}),
    dcc.Graph(
        style = {'backgroundColor' : colors['background']},
        id='bar',
        figure=fig
    ),

    dcc.Graph(style = {'backgroundColor' : colors['background']},id='bar_moy_cont'),

    dcc.Slider(
    id = 'slide-2',
    min = annees.min(),
    max = annees.max(),
    step = 1,
    value = min(annees)
    ),
    html.Div(style = {'backgroundColor' : colors['background']},id='page-2-content' ),
    #Rajout !!!
    html.H4(children=["Légende des diagrammes : \n AS : Asie , SA : Amérique du Sud , EU : Europe , OC : Océanie" ],
            style={
                'color': colors['text'],
                'textAlign' : 'center'})
])
