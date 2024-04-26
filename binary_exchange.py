def char_to_binary(char):
    return format(ord(char), '08b')

def bit_to_char(bits):
    return chr(int(bits, 2))

def convert_data_to_binary(data):
    matrix = []
    for char in data:
        binary = char_to_binary(char)
        first_half = binary[:4]
        second_half = binary[4:]
        first_half_int = [int(bit) for bit in first_half]
        second_half_int = [int(bit) for bit in second_half]
        matrix.append(first_half_int)
        matrix.append(second_half_int)
    return matrix