def text_to_binary(text):
    # Converting each character to its binary representation

    binary_result = "".join(format(ord(char), "08b") for char in text)

    return binary_result


def binary_to_text(binary_str):
    # Splitting the binary string into chunks of 8 bits
    chars = [binary_str[i : i + 8] for i in range(0, len(binary_str), 8)]

    text_result = "".join(chr(int(char, 2)) for char in chars)
    print(text_result)

    return text_result


if __name__ == "__main__":
    input_text = "Hel73lo"
    binary_output = text_to_binary(input_text)

    print(f"Original text: {input_text}")
    print(f"Binary output: {binary_output}")

    binary_to_text_output = binary_to_text(binary_output)
    print(f"Converted back to text: {binary_to_text_output[0]}")
