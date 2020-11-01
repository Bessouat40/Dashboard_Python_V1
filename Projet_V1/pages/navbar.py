import dash_bootstrap_components as dbc

colors = {
    'background': '#B2ACAB',
    'text': '#7FDBFF'
}

def Navbar():

    navbar = dbc.NavbarSimple(
      children=[
        dbc.DropdownMenu(
            children=[
                dbc.DropdownMenuItem("Pages disponibles", header=True),
                dbc.DropdownMenuItem("Visualisation mondiale" , href = "/page-1"),
                dbc.DropdownMenuItem("Segmentation par continents", href="/page-2"),
                dbc.DropdownMenuItem("Visualisation européenne", href="/page-3")
            ],
            nav=True,
            in_navbar=True,
            label="More",
            direction = 'left'
        ),
        dbc.NavItem(dbc.NavLink("Accueil", href= 'page-content'))
    ],
    brand="Navigation à travers les différentes visualisations",
    brand_href="#",
    color = colors['background'],
    dark=True,
    fluid = True
    )
    return navbar
