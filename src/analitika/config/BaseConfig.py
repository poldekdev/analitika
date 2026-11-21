from pydantic import BaseModel

from analitika.config import BarConfig
from analitika.config.LineConfig import LineConfig
from analitika.config.PieConfig import PieConfig


class BaseConfig(BaseModel):
    type: str
    module_config: BarConfig.BarConfig | LineConfig | PieConfig
