from pydantic import BaseModel

from src.analitika.config import BarConfig
from src.analitika.config.LineConfig import LineConfig
from src.analitika.config.PieConfig import PieConfig


class BaseConfig(BaseModel):
    type: str
    module_config: BarConfig.BarConfig | LineConfig | PieConfig
