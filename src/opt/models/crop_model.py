
from typing import Optional
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
    COVERCROP ="COVERCROP"



class Crop(BaseModel):
    name: CropName
    crop_yield: float
    duration: Optional[int] = None
    price: Optional[float] = None
    nutrient_impact: int


class Farm(BaseModel):
    """The plating "window" for crops. Its dimensions are n time units by m fields."""
    timeframe: int
    fields: int


class Allocation(BaseModel):
    """A planted state. Represents a mapping of a crop to each time, field pair."""
    start_date: datetime = datetime.now()
    crops: list[Crop]
    farm: Farm
    mapping: list[list[Crop]]



class CropYieldNutrient(BaseModel):
    crop: CropName
    yield_value: float
    nutrient_level: float
    field: int
    season: int



class AgricultureData(BaseModel):
    data: list[CropYieldNutrient]
