import argparse

from matplotlib import pyplot as plt

from analitika.charts import bar, line, pie
from analitika.config import config_parser
from analitika.config.BarConfig import BarConfig
from analitika.config.LineConfig import LineConfig
from analitika.config.PieConfig import PieConfig


def generate_chart(config_path: str, output_path: str | None):
    with open(config_path, "r") as f:
        config = config_parser.parse_config(f.read())
    if isinstance(config, LineConfig):
        fig, _ax = line.generate_chart(config)
    if isinstance(config, BarConfig):
        fig, _ax = bar.generate_chart(config)
    if isinstance(config, PieConfig):
        fig, _ax = pie.generate_chart(config)
    if output_path != None:
        fig.savefig(output_path)
    else:
        plt.show()


parser = argparse.ArgumentParser(
    prog="analitika", description="Chart generator with JSON configuration"
)
parser.add_argument("config")
parser.add_argument(
    "-o",
    "--output",
    default=None,
    help="Path to output file (i.e path to where chart should be saved to)",
)

args = parser.parse_args()

generate_chart(args.config, args.output)
