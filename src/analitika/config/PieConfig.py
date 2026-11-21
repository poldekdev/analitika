from pydantic import BaseModel


class PieConfig(BaseModel):
    categories: list[str]
    values: list[float]
    colors: list[str] | None = None
    title: str | None = None
    value_label: str | None = None
