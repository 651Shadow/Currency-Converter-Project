def speed_converter(value, from_unit, to_unit):
    to_mps = {
        "m/s": 1,
        "km/h": 1 / 3.6,
        "mph": 0.44704,
        "knot": 0.514444,
        "ft/s": 0.3048,
    }

    from_mps = {
        "m/s": 1, 
        "km/h": 3.6, 
        "mph": 2.23694, 
        "knot": 1.94384, 
        "ft/s": 3.28084
    }

    speed_in_mps = value * to_mps[from_unit]
    result = speed_in_mps * from_mps[to_unit]

    return result


print(speed_converter(100, "km/h", "m/s"))
print(speed_converter(60, "mph", "km/h"))
print(speed_converter(10, "m/s", "ft/s"))
