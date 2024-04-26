import numpy as np
from encode import transmission_data
from binary_exchange import bit_to_char

def checking_data(data_check, matrix_check):
    res = []
    has_false_bit = False
    check = transmission_data(matrix_check, np.transpose(data_check))
    check = np.transpose(check)
    for need_check in check:
        for i in range(matrix_check.shape[1]):
            if (need_check == matrix_check[:,i]).all():
                has_false_bit = True
                break
        if has_false_bit: 
            res.append(i) 
        else: 
            res.append(-1)
    return res

def error_correction(data_error, pos):
    for i in range(len(pos)):
        data_error[i][pos[i]] = 1 - data_error[i][pos[i]]

def decode_list(trans):
    encoder = [[row[2], row[4], row[5], row[6]] for row in trans]
    bit_char = ''.join([''.join(map(str, lst)) for lst in encoder])
    bit_char = [bit_char[i:i+8] for i in range(0, len(bit_char), 8)]
    char_list = [bit_to_char(byte) for byte in bit_char]
    return ''.join(char_list)