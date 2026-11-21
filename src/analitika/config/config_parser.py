import analitika.config.BarConfig
import analitika.config.BaseConfig
import analitika.config.LineConfig
import analitika.config.PieConfig


def parse_config(
    config: str,
) -> (
    analitika.config.BarConfig.BarConfig
    | analitika.config.LineConfig.LineConfig
    | analitika.config.PieConfig.PieConfig
    | None
):
    baseConfig = analitika.config.BaseConfig.BaseConfig.model_validate_json(config)
    match baseConfig.type:
        case "bar":
            return analitika.config.BarConfig.BarConfig.model_validate(
                baseConfig.module_config
            )
        case "line":
            return analitika.config.LineConfig.LineConfig.model_validate(
                baseConfig.module_config
            )
        case "pie":
            return analitika.config.PieConfig.PieConfig.model_validate(
                baseConfig.module_config
            )
    return None
