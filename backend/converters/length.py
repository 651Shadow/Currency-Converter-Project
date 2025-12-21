# Placeholder module for the Conversion Calculator project.
# Conversion 
CONVERSION_FACTORS = {
    "m": 1,
    "km": 0.001,
    "cm": 100,
    "mm": 1000,
    "ft": 3.280839895,
    "inch": 39.37007874,
    "yard": 1.093613298,
    "mile": 0.000621371,
    "lightyear": 1.057000834e-16
}

def convert_length(value, from_unit, to_unit):
    if from_unit not in CONVERSION_FACTORS:
        return f"Error: Unknown unit '{from_unit}'"
    if to_unit not in CONVERSION_FACTORS:
        return f"Error: Unknown unit '{to_unit}'"

    value_in_meters = value / CONVERSION_FACTORS[from_unit]

    result = value_in_meters * CONVERSION_FACTORS[to_unit]

    return result


if __name__ == "__main__":
    print(convert_length(5, "ft", "m"))       
    print(convert_length(100, "cm", "inch"))  
    print(convert_length(2, "mile", "km"))    