from .models import *

corn = Crop(
    name=CropName.CORN, crop_yield=2.5, duration=3, price=3.5, nutrient_impact=2
)
soybean = Crop(
    name=CropName.SOYBEAN, crop_yield=2.0, duration=2, price=3.0, nutrient_impact=1
)
maize = Crop(
    name=CropName.MAIZE, crop_yield=2.2, duration=3, price=3.2, nutrient_impact=3
)
wheat = Crop(
    name=CropName.WHEAT, crop_yield=2.3, duration=3, price=3.3, nutrient_impact=4
)
barley = Crop(
    name=CropName.BARLEY, crop_yield=2.4, duration=3, price=3.4, nutrient_impact=5
)
sunflower = Crop(
    name=CropName.SUNFLOWER, crop_yield=2.6, duration=3, price=3.6, nutrient_impact=6
)

farm = Farm(timeframe=10, fields=4)

allocation = Allocation(
    crops=[corn, soybean, maize, wheat, barley, sunflower],
    farm=farm,
    mapping=[
        [corn, soybean, maize, wheat],
        [soybean, maize, wheat, barley],
        [maize, wheat, barley, sunflower],
        [wheat, barley, sunflower, corn],
        [barley, sunflower, corn, soybean],
        [sunflower, corn, soybean, maize],
        [corn, soybean, maize, wheat],
        [soybean, maize, wheat, barley],
        [maize, wheat, barley, sunflower],
        [wheat, barley, sunflower, corn],
    ],
)
