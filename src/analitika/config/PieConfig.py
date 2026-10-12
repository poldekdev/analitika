from pydantic import BaseModel


class PieConfig(BaseModel):
    categories: list[str]
    values: list[float]
    colors: list[str] | None
    title: str | None
    value_label: str | None
