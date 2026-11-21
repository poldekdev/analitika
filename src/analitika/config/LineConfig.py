from pydantic import BaseModel


class LineConfig(BaseModel):
    x: list[float]
    y: list[float]
    title: str
    marker: str = "o"
