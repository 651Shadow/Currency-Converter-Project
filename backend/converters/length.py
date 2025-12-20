def length_converter(value, from_unit, to_unit):
    to_meter = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "mm": 0.001,
        "ft": 0.3048,
        "inch": 0.0254,
    }

    if from_unit not in to_meter or to_unit not in to_meter:
        raise ValueError("Invalid unit")

    value_in_meter = value * to_meter[from_unit]
    result = value_in_meter / to_meter[to_unit]

    return result
