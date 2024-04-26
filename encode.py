import numpy as np
import random

def multiply_matrices_binary(matrix1, matrix2):
    try:
        mat1 = np.array(matrix1)
        mat2 = np.array(matrix2)
        if mat1.shape[1] != mat2.shape[0]:
            raise ValueError("No match size between 2 matrix.")
        mat2 = np.transpose(mat2)
        temp_row = []
        for m1 in mat1:
            temp_col = []
            for m2 in mat2:
                temp = np.dot(m1, m2)
                temp = temp % 2
                temp_col.append(int(temp))
            temp_row.append(temp_col)
        result = temp_row
        return result  
    except ValueError as e:
        print(e)
        return None

def transmission_data(data, matrix_trans):
    return multiply_matrices_binary(data, matrix_trans)

def create_jam(bit):
    for d in bit:
        ran_num = random.randint(0, len(d) - 1)
        d[ran_num] = 1 - d[ran_num]