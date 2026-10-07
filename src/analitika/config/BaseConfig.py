from pydantic import BaseModel
import src.analitika.config.BarConfig as BarConfig

class BaseConfig(BaseModel):
    type: str
    module_config: BarConfig.BarConfig
