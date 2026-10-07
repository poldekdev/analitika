from pydantic import BaseModel


class BarConfig(BaseModel):
    categories: list[str]
    values: list[float]
    title: str
