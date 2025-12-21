import math

CONVERSIONS_TO_KG = {
    "kg": 1,
    "g": 1000,
    "mg": 1000000,
    "ton": 0.001,
    "lb": 2.20462,
    "oz": 35.274,
}


def convert_mass(value: float, base: str, to: str):
    base = base.lower()
    to = to.lower()

    if base not in CONVERSIONS_TO_KG or to not in CONVERSIONS_TO_KG:
        raise ValueError("Unsupported unit for conversion")
    
    kg_value = value / CONVERSIONS_TO_KG[base]
    target_factor = CONVERSIONS_TO_KG[to]
    final_value = kg_value * target_factor

    return final_value


if __name__ == "__main__":
    print(f"5 kg to lb: {convert_mass(5, 'kg', 'lb')}")
    print(f"2000 g to kg: {convert_mass(2000, 'g', 'kg')}")
    print(f"1 ton to oz: {convert_mass(1, 'ton', 'oz')}")
