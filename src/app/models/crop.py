

from datetime import datetime
from enum import Enum
from pydantic import BaseModel

class CropName(str, Enum):
    CORN = "CORN"
    SOYBEAN = "SOYBEAN"
    MAIZE = "MAIZE"
    WHEAT = "WHEAT"
    BARLEY = "BARLEY"
    SUNFLOWER = "SUNFLOWER"


class Crop(BaseModel):
    name: CropName
    crop_yield: float
    duration: int
    price: float
    nutrient_impact: int


class Window(BaseModel):
    """The plating "window" for crops. Its dimensions are n time units by m fields."""
    timeframe: tuple[int, int]
    fields: tuple[int, int]


class Allocation(BaseModel):
    """A planted state. Represents a mapping of a crop to each time, field pair."""
    start_date: datetime = datetime.now()
    mapping: list[list[Crop]]

