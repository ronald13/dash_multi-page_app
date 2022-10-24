import os
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html
from sections.overview import overview
from sections.header import header

here = os.path.abspath(os.path.dirname(__file__))
app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}],
    assets_folder=os.path.join(here, "assets"),
)

# This is for docker to find the server
server = app.server

sidebar_header = dbc.Row(
    [
        dbc.Col(html.H2("Logo", className="app__logo")),
        dbc.Col(
            html.Button(
                # use the Bootstrap navbar-toggler classes to style the toggle
                html.Span(className="navbar-toggler-icon"),
                className="navbar-toggler",
                # the navbar-toggler classes don't set color, so we do it here
                style={
                    "color": "rgba(0,0,0,.5)",
                    "border-color": "rgba(0,0,0,.1)",
                },
                id="toggle",
            ),
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
    ]
)

sidebar = html.Div(
    [
        sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
            ],
            id="blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(
            dbc.Nav(
                [
                    dbc.NavLink("Home", href="/", active="exact"),
                    dbc.NavLink("All information", href="/page-1", active="exact"),
                    dbc.NavLink("Personal Information", href="/page-2", active="exact"),
                    dbc.NavLink("Exit", href="/page-3", active="exact"),
                ],
                vertical=True,
                pills=True,
            ),
            id="collapse",
        ),
    ],
    id="sidebar",
)

content = html.Div(id="app__content", className="app__content flex-center")

main = html.Div([header, content], className="app__main")

app.layout = html.Div([dcc.Location(id="url"), sidebar, main])


@app.callback(Output("app__content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return  html.P("HOME")
    elif pathname == "/page-1":
        return html.P("ALL INFO")
    elif pathname == "/page-2":
        return html.P("PERSONAL INFO")
    elif pathname == "/page-3":
        return html.P("EXIT")
    else:
    # If the user tries to reach a different page, return a 404 message
        return html.Div(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            className="p-3 bg-light rounded-3",
        )


@app.callback(
    Output("collapse", "is_open"),
    [Input("toggle", "n_clicks")],
    [State("collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


# don't run when imported, only when standalone
if __name__ == "__main__":
    port = os.getenv("DASH_PORT", 8053)
    app.run_server(debug=True, port=port)
