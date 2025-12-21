DATA_IN_BYTES = {
    "B": 1,
    "KB": 1024,
    "MB": 1024**2,
    "GB": 1024**3,
    "TB": 1024**4,
    "PB": 1024**5,
}


def convert_data_unit(value: float, from_unit: str, to_unit: str):
    if from_unit not in DATA_IN_BYTES or to_unit not in DATA_IN_BYTES:
        raise ValueError(f"Unsupported from_unit: {from_unit} or to_unit: {to_unit}")

    from_unit = from_unit.upper()
    to_unit = to_unit.upper()

    # Convert the input value to bytes then convert to the target unit
    bytes_value = value * DATA_IN_BYTES[from_unit]
    converted_value = bytes_value / DATA_IN_BYTES[to_unit]

    return converted_value


if __name__ == "__main__":
    print(convert_data_unit(1024, "KB", "MB"))
    print(convert_data_unit(1, "GB", "MB"))
    print(convert_data_unit(2048, "MB", "GB"))
