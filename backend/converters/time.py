TIME_PER_HOUR = {
    "second": 3600,
    "minute": 60,
    "hour": 1,
    "day": 0.0416667,
    "week": 0.00595238,
    "microsecond": 3600000000,
    "millisecond": 3600000,
    "year": 0.000114155,
}


def convert_time(value: float, from_unit: str, to_unit: str):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit not in TIME_PER_HOUR or to_unit not in TIME_PER_HOUR:
        raise ValueError(f"Unsupported from_unit: {from_unit}")

    # Convert the input value to hours then convert to the target unit
    hours = value / TIME_PER_HOUR[from_unit]
    converted_value = hours * TIME_PER_HOUR[to_unit]

    return converted_value


if __name__ == "__main__":
    print(convert_time(120, "minute", "hour"))
    print(convert_time(2, "day", "hour"))
    print(convert_time(3600, "second", "hour"))
