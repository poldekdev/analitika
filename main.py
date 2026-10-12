from src.analitika.config import config_parser
from src.analitika.charts import bar, line, pie
from src.analitika.config.LineConfig import LineConfig
from src.analitika.config.BarConfig import BarConfig
from src.analitika.config.PieConfig import PieConfig
import argparse

def generate_chart(config_path: str, output_path: str):
    with open(config_path, "r") as f:
        config = config_parser.parse_config(f.read())
    if isinstance(config, LineConfig):
        fig, ax = line.generate_chart(config.x, config.y, config.title, config.marker)
        fig.savefig(output_path)
    if isinstance(config, BarConfig):
        fig, ax = bar.generate_chart(config.categories, config.values, config.title)
        fig.savefig(output_path)
    if isinstance(config, PieConfig):
        fig, ax = pie.generate_chart(config.categories, config.values, config.colors, config.title, config.value_label)
parser = argparse.ArgumentParser(
    prog = "analitika",
    description = "Chart generator with JSON configuration"
)
parser.add_argument("config")
parser.add_argument("-o", "--output", default = "chart.png", help = "Path to output file (i.e path to where chart should be saved to)")

args = parser.parse_args()

generate_chart(args.config, args.output)
