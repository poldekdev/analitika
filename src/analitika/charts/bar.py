import matplotlib.pyplot as plt
import numpy as np


def generate_chart(categories: list[str], values: list[float], title: str):
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title(title)

    return fig, ax
