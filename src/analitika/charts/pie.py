import matplotlib.pyplot as plt


def generate_chart(
    categories: list[str],
    values: list[float],
    colors: list[str] | None,
    title: str | None,
    value_label: str | None,
):
    fig, ax = plt.subplots()
    ax.pie(values, labels=categories, colors=colors, autopct=value_label)
    if title != None:
        ax.set_title(title)
    return fig, ax
