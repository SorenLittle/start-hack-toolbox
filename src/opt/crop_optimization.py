from docplex.mp.model import Model
from models import CropYieldNutrient, Crop,CropName, AgricultureData


def croptimization(number_of_fields: int, number_of_seasons: int, crops: list[Crop], initial_nutrients: int = 10, min_nutrients: int = 2, max_nutrients: int = 20 ):
    # Fields
    N = number_of_fields #number of fields
    F = range(1, N+1)  # Assuming N fields

    T = range(1, number_of_seasons+1)  # seasons -> 12 season 6 years Winter season Summer Season
    Covercrop = Crop(name=CropName.COVERCROP,crop_yield=0,duration=1, nutrient_impact=1)
    # Crops
    Covercrop = Crop(name=CropName.COVERCROP,crop_yield=0,duration=1, nutrient_impact=1)
    crops.append(Covercrop)
    C = [crop.name for crop in crops]

    C_without_CoverCrop = [crop for crop in C if crop != "CoverCrop"]


    # Parameters
    Duration = {crop.name: 1 for crop in crops}  # Growth duration in months (can adjust BlockingCrop as needed)

    Yield = {crop.name: crop.crop_yield/Duration[crop.name] for crop in crops}  # Yield per crop (BlockingCrop has no yield)
    NutrientDepletion = {crop.name: crop.nutrient_impact/Duration[crop.name] for crop in crops}  # Nutrient impact (BlockingCrop has no impact)
    print(NutrientDepletion)
    InitialNutrients = initial_nutrients
    MinNutrients = min_nutrients  # Minimum nutrients required
    MaxNutrients = max_nutrients  # Maximum nutrients allowed
    # Model
    mdl = Model("Agricultural Scheduling with Nutrient Management")

    # Extend decision variables
    x = mdl.binary_var_cube(C, T, F, name="Plant")
    yield_complete = mdl.continuous_var_matrix(T, F, lb=0, name="YieldComplete")
    nutrient = mdl.continuous_var_matrix(T, F, lb=MinNutrients, ub=MaxNutrients, name="NutrientLevel")

    # Nutrient and Yield Dynamics
    for f in F:
        for t in T:  # Start from second month since the first month's conditions are already set
            # Nutrient level update
            if t != 1:
                nutrient_update_expr = nutrient[t-1, f] + mdl.sum(NutrientDepletion[c] * x[c, t, f] for c in C)
                mdl.add_constraint(nutrient[t,f] == nutrient_update_expr, f"nutrient_update_{t}")
                
                # Yield update
                yield_update_expr = yield_complete[t-1,f] + mdl.sum(Yield[c] * x[c, t,f] for c in C)
                mdl.add_constraint(yield_complete[t,f] == yield_update_expr, f"yield_update_{t}")
            else:
                print(f"Initial Nutrient: {InitialNutrients}")
                print(f"Subtracting: {mdl.sum(NutrientDepletion[c] * x[c, t, f] for c in C)}")
                mdl.add_constraint(nutrient[1, f] == InitialNutrients + mdl.sum(NutrientDepletion[c] * x[c, t, f] for c in C))
                mdl.add_constraint(yield_complete[1, f] == mdl.sum(Yield[c] * x[c, t,f] for c in C), f"initial_yield_{f}")
                print(f"After: {mdl.sum(NutrientDepletion[c] * x[c, t, f] for c in C)}")


    # Ensure single crop planting at a time
    for t in T:
        mdl.add_constraint(mdl.sum(x[c, t,f] for c in C) <= 1, f"single_crop_{t}")


    # Ensure nutrient levels are within bounds
    for f in F:
        for t in T:
            mdl.add_constraint(nutrient[t,f] <= MaxNutrients, f"nutrient_upper_bound_{t}")


    # Ensure at least one harvest each season across all fields
    for t in T:
        mdl.add_constraint(mdl.sum(x[c, t, f] for c in C_without_CoverCrop for f in F) >= 1, f"harvest_each_season_{t}")


            
    # Objective: Maximize total yield across all fields
    mdl.maximize(mdl.sum(yield_complete[t, f] for t in T for f in F))


    # Solve
    solution = mdl.solve(log_output=True)

    # Assuming F, T, C, yield_complete, and nutrient are defined similar to your initial setup
# This might require adjustment based on how you actually obtain yield and nutrient values in your code
    if solution:
        field_season_data = []

        for f in F:
            for t in T:
                crop_planted = [c for c in C if x[c, t, f].solution_value > 0.5]
                planted_crop = crop_planted[0] if crop_planted else "No planting"
                yield_value = yield_complete[t, f].solution_value
                nutrient_value = nutrient[t, f].solution_value

                # Adjust the crop name to match the CropName enum, if necessary
                planted_crop_upper = planted_crop.upper()

                #               Check if t        he uppercase planted crop is a member of CropName
                if planted_crop_upper in CropName.__members__:
                    crop_name = CropName[planted_crop_upper]  # This converts the string to the actual Enum instance
                else:
                    crop_name = "UNKNOWN"  # Handle unknown or no planting case

                # Create a CropYieldNutrient instance
                crop_yield_nutrient = CropYieldNutrient(
                    crop=crop_name,
                    yield_value=round(yield_value,2),
                    nutrient_level=round(nutrient_value,2),
                    field=f,
                    season=t
                )

                field_season_data.append(crop_yield_nutrient)

        # Create the AgricultureData instance
        agriculture_data = AgricultureData(data=field_season_data)
        print(agriculture_data)
        return agriculture_data


# Example usage
number_of_fields = 5
number_of_seasons = 10
crops = [Crop(name=CropName.CORN,crop_yield=4, nutrient_impact=-3), Crop(name=CropName.SOYBEAN,crop_yield=3, nutrient_impact=-2)]

agriculture_data = croptimization(number_of_fields, number_of_seasons, crops)

json_str = agriculture_data.json()

# Save the JSON string to a file
with open("agriculture_data.json", "w") as file:
    file.write(json_str)