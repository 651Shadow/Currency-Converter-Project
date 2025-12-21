import math

CONVERSTIONS_TO_M_SQUAR = {
    "sq_m": 1,
    "sq_cm": 10000,
    "sq_mm": 1000000,
    "sq_km": 0.000001,
    "sq_ft": 10.7639,
    "sq_in": 1550.0031,
    "sq_yd": 1.19599,
    "sq_mile": 0.000000386102,
}


def convert_area(square_meters: float, base: str, to: str):
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

    print(convert_area(30, "km2", "mile2"))
