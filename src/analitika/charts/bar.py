from analitika.config.BarConfig import BarConfig
import matplotlib.pyplot as plt


def generate_chart(config: BarConfig):
    fig, ax = plt.subplots()
    ax.bar(config.categories, config.values)
    ax.set_title(config.title)

    return fig, ax
