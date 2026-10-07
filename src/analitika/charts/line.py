import matplotlib.pyplot as plt
import numpy as np

def generate_chart(x: list[float], y: list[float], title: str, marker: str):
    fig, ax = plt.subplots()
    ax.plot(x, y, marker=marker)
    ax.set_title(title)

    return fig, ax
