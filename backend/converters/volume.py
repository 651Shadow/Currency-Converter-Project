import math

CONVERSIONS_TO_LITER = {
    "l": 1,
    "ml": 1000,
    "cl": 100,
    "m3": 0.001,
    "cm3": 1000,
    "gal": 0.264172,
    "qt": 1.05669,
    "fl_oz": 33.814,
    "cup": 4.22675,
}


def convert_volume(value: float, base: str, to: str):

    base = base.lower()
    to = to.lower()
    if base not in CONVERSIONS_TO_LITER or to not in CONVERSIONS_TO_LITER:
        raise ValueError("Unsupported unit for conversion")

    liter_value = value / CONVERSIONS_TO_LITER[base]
    target_factor = CONVERSIONS_TO_LITER[to]
    final_value = liter_value * target_factor

    return final_value


if __name__ == "__main__":

    print(f"1 m3 to l: {convert_volume(1, 'm3', 'l')}")

    print(f"1 gal to fl_oz: {convert_volume(1, 'gal', 'fl_oz')}")

    print(f"500 ml to cup: {convert_volume(500, 'ml', 'cup'):.2f}")