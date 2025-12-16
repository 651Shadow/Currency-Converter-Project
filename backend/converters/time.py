TIME_PER_HOUR = {
    "seconds": 3600,
    "minutes": 60,
    "hours": 1,
    "days": 0.0416667,
    "weeks": 0.00595238,
    "microseconds": 3600000000,
    "milliseconds": 3600000,
    "years": 0.000114155,
}


def convert_time(value: float, from_unit: str, to_unit: str):
    if from_unit not in TIME_PER_HOUR or to_unit not in TIME_PER_HOUR:
        raise ValueError(f"Unsupported from_unit: {from_unit}")

    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    # Convert the input value to hours then convert to the target unit
    hours = value / TIME_PER_HOUR[from_unit]
    converted_value = hours * TIME_PER_HOUR[to_unit]

    return converted_value


if __name__ == "__main__":
    # Example usage
    print(convert_time(120, "minutes", "hours"))  # Should output 2.0
    print(convert_time(2, "days", "hours"))  # Should output 48.0
    print(convert_time(3600, "seconds", "hours"))  # Should output 1.0
