import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

colors = {
    'background': '#636161',
    'text': '#B2ACAB'
}

index_page = html.Div(style={
                'textAlign': 'center',
                'background' : colors['background'],
                'color': colors['text']},children=[
    html.H1(children="Rapport consommation d'alcool/accident de voiture chez les jeunes"),

    html.Div(children='''
        Ceci est un dashboard permettant de voir le lien entre la consommation d'alcool chez les jeunes europpéens et le nombre d'accidents de voiture qu'ils ont.
    '''),
    html.Div(id='homepage-content')
])
