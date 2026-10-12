from src.analitika.config import config_parser
from src.analitika.charts import bar, line
from src.analitika.config.LineConfig import LineConfig
from src.analitika.config.BarConfig import BarConfig

def main_menu():
    print("Welcome to Analitika")
    print("https://github.com/poldekdev/analitika")
    print("""


        """)
    path = input("Enter path to your config.json file: ")
    output_path = input("Enter output path: ")
    if ".png" not in output_path:
        output_path += ".png"
    if output_path == None:
        output_path = "chart.png"
    with open(path, "r") as f:
        config = config_parser.parse_config(f.read())
    if isinstance(config, LineConfig):
        fig, ax = line.generate_chart(config.x, config.y, config.title, config.marker)
        fig.savefig(output_path)
    if isinstance(config, BarConfig):
        fig, ax = bar.generate_chart(config.categories, config.values, config.title)
        fig.savefig(output_path)
    print("Chart render was saved to " + output_path)
main_menu()
