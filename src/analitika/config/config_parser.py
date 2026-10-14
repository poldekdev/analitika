import src.analitika.config.BarConfig
import src.analitika.config.BaseConfig
import src.analitika.config.LineConfig
import src.analitika.config.PieConfig


def parse_config(
    config: str,
) -> (
    src.analitika.config.BarConfig.BarConfig
    | src.analitika.config.LineConfig.LineConfig
    | src.analitika.config.PieConfig.PieConfig
    | None
):
    baseConfig = src.analitika.config.BaseConfig.BaseConfig.model_validate_json(config)
    match baseConfig.type:
        case "bar":
            return src.analitika.config.BarConfig.BarConfig.model_validate(
                baseConfig.module_config
            )
        case "line":
            return src.analitika.config.LineConfig.LineConfig.model_validate(
                baseConfig.module_config
            )
        case "pie":
            return src.analitika.config.PieConfig.PieConfig.model_validate(
                baseConfig.module_config
            )
    return None
