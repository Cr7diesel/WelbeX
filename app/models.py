from pydantic import BaseModel


class Route(BaseModel):
    id: int
    points: list[dict[str, int]]
