from analitika.config.LineConfig import LineConfig
import matplotlib.pyplot as plt


def generate_chart(config: LineConfig):
    fig, ax = plt.subplots()
    ax.plot(config.x, config.y, marker=config.marker)
    ax.set_title(config.title)

    return fig, ax
