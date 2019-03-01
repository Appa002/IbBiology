import plotly.offline as py
import plotly.graph_objs as go
import numpy as np


def fun():
    for i in range(0, 10):
        yield i
        print("side effect")

if __name__ == "__main__":
    for i in fun():
        print(i)
    exit(0)
    N = 1000
    random_x = np.abs(np.random.randn(N))
    random_y = np.abs(np.random.randn(N))

    data = [go.Scatter(
        x=random_x,
        y=random_y,
        mode = 'markers'
    )]

    layout = go.Layout(
        title='Sampled Results',
        xaxis=dict(
            title = 'Time [s]'
        ),
        yaxis=dict(
            title='Amount of Sick People [N]'
        ),
    )

    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='histogram.html', auto_open=False)