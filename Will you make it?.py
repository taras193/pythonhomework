#V1 (Not wortking)
# def zero_fuel(distance_to_pump, mpg, fuel_left):
#     my_fuel=distance_to_pump*fuel_left
#     return True if my_fuel>=50 else False
#V2
def zero_fuel(distance_to_pump, mpg, fuel_left):
    return (bool(distance_to_pump<=fuel_left*mpg))