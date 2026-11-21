from pydantic import BaseModel



class BaseConfig(BaseModel):
    type: str
    module_config: dict
