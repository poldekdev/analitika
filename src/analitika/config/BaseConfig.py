from pydantic import BaseModel
import src.analitika.config.BarConfig as BarConfig
from src.analitika.config.LineConfig import LineConfig

class BaseConfig(BaseModel):
    type: str
    module_config: BarConfig.BarConfig | LineConfig
