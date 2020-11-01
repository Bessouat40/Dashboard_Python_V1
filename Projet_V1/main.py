import dash
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

from pages import index
from pages import page_1
from pages import page_2
from pages import page_3
from pages import page_test
from pages import navbar

import pandas as pd
import plotly.express as px


print(dcc.__version__) # 0.6.0 or above is required

nav = navbar.Navbar()
app = dash.Dash(external_stylesheets=[dbc.themes.UNITED])
app.config.suppress_callback_exceptions = True

colors = {
    'background': '#636161',
    'text': '#B2ACAB'
}

app.layout = html.Div([
    nav,
    dcc.Location(id='url', refresh=True),
    html.Div(id='page-content')
])

# Page 1 callback
@app.callback(
    Output('indicator-graphic', 'figure'),
    [Input('xaxis-column', 'value')])
def update_graph(xaxis_column_name):
    jeunes_morts = page_1.jeunes_morts
    df = jeunes_morts[jeunes_morts.Country == xaxis_column_name]
    df = df[['Year' , 'Value']].groupby('Year').max()
    fig = px.line(df)
    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')
    fig.update_xaxes(title=xaxis_column_name)
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
)

    return fig

@app.callback(
    Output('bar_moy_cont' , 'figure'),
    [Input('slide-2' , 'value')])
def update_bar_moy_cont(val_slide_2):
    jeunes_morts = page_2.jeunes_morts
    vis_monde = jeunes_morts[jeunes_morts['Year'] == val_slide_2].groupby(['Continent']).mean()
    fig = px.bar(vis_monde , y = 'Value' ,color = 'Value' ,  color_continuous_scale=px.colors.sequential.Greys , title = "Vous voyez le nombre d'accidents en voiture chez les jeunes en : {}".format(val_slide_2))
    fig.update_layout(barmode='stack', xaxis={'categoryorder':'total descending'})
    fig.update_layout(
    plot_bgcolor=colors['background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text']
    )
    print("Vous voyez le nombre d'accidents en voiture chez les jeunes en : {}".format(val_slide_2))
    return fig

@app.callback(
    Output('histo_europe' , 'figure'),
    [Input('choix_eu' , 'value')])
def update_choix_europe(choix_pays):
    accidents_eu = page_3.util
    pays_eu = accidents_eu.Country.unique()
    test = accidents_eu[accidents_eu.Country == str(choix_pays)]
    test = test.drop(['Country' , 'COUNTRY' , 'Continent'] , axis = 'columns')
    test = test.groupby('Year').mean()
    value = test.Value
    annees = accidents_eu.Year.unique()
    fin = pd.DataFrame({'year' : annees , 'value' : value})
    fig = px.bar(fin , x = 'year' , y = 'value' , color= 'value' , color_continuous_scale=px.colors.sequential.Greys)
    fig.update_layout(
        plot_bgcolor=colors['background'],
        paper_bgcolor=colors['background'],
        font_color=colors['text']
    )
    return fig

# Index Page callback
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/page-1':
        return page_1.page_1_layout
    elif pathname == '/homepage' :
        #return homepage.homepage_layout
        return page_1.page_1_layout
    elif pathname == '/page-2':
        return page_2.page_2_layout
    elif pathname == '/page-3' :
        return page_3.page_3_layout
    else:
        #return index.index_page
        return page_1.page_1_layout

if __name__ == '__main__':
    app.run_server(debug=True)
