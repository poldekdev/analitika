import matplotlib.pyplot as plt


def generate_chart(categories: list[str], values: list[float], title: str):
    fig, ax = plt.subplots()
    ax.bar(categories, values)
    ax.set_title(title)

    return fig, ax
