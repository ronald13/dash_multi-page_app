import plotly.graph_objects as go

y_data = ['<b>Element 1</b>', '<b>Element 2</b>', '<b>Element 3</b>', '<b>Element 4</b>']
x_data = [24, 19, 22, 33]

def buble_chart(x_data, y_data):
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x_data,
        y=y_data,
        mode='markers',
        marker=dict(size=50, color=['#C0D8C0', '#F5EEDC', '#DD4A48', '#ECB390']),
        textfont=dict(color='black')
    ))
    fig.add_trace(
        go.Bar(
            x=x_data,
            y=y_data,
            marker=dict(color=['#C0D8C0', '#F5EEDC', '#DD4A48', '#ECB390']),
            orientation="h",
            width=0.5,
            textfont=dict(color='black')))
    #
    fig.update_layout(height=300,
                      template='plotly_white',
                      margin={'t': 20, 'r': 20, 'l': 20, 'b': 20, 'pad':20},
                      showlegend=False)
    fig.update_xaxes(showgrid=False, showticklabels=False, zeroline=False )

    return fig