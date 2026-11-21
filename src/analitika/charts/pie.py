from analitika.config.PieConfig import PieConfig
import matplotlib.pyplot as plt


def generate_chart(config: PieConfig):
    fig, ax = plt.subplots()
    ax.pie(config.values, labels=config.categories, colors=config.colors, autopct=config.value_label)
    if config.title != None:
        ax.set_title(config.title)
    return fig, ax
