def convert_to_correct_types(input_dict):
    converted_dict = {}
    for key, value in input_dict.items():
        try:
            # Try converting to integer first
            converted_value = int(value)
        except ValueError:
            try:
                # If integer conversion fails, try converting to float
                converted_value = float(value)
            except ValueError:
                # If both conversions fail, keep the value as is (could be a string)
                converted_value = value
        converted_dict[key] = converted_value
    return converted_dict
