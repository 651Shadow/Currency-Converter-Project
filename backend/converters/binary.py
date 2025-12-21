def text_to_binary(text):
    # Converting each character to its binary representation
    binary_result = "".join(format(ord(char), "08b") for char in text)

    return binary_result


if __name__ == "__main__":
    input_text = "Hel73lo"
    binary_output = text_to_binary(input_text)

    print(f"Original text: {input_text}")
    print(f"Binary output: {binary_output}")
