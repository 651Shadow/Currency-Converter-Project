import math

CONVERSTIONS_TO_M_SQUAR = {
    "m2": 1,
    "cm2": 10000,
    "mm2": 1000000,
    "km2": 0.000001,
    "ft2": 10.7639,
    "in2": 1550.0031,
    "yd2": 1.19599,
    "mile2": 0.000000386102,
}


def square_meters_to_square_feet(base: str, to: str, square_meters: float):
    # Conversion factor from square meters to square feet
    base = base.lower()
    to = to.lower()
    if base not in CONVERSTIONS_TO_M_SQUAR or to not in CONVERSTIONS_TO_M_SQUAR:
        raise ValueError("Unsupported unit for conversion")
    # convert anything to M^2
    m = CONVERSTIONS_TO_M_SQUAR[base]
    square_meters_value = square_meters / m
    # convert M^2 to target unit
    v = CONVERSTIONS_TO_M_SQUAR[to]
    value = square_meters_value * v
    return value


if __name__ == "__main__":

    print(square_meters_to_square_feet("km2", "mile2", 30))
