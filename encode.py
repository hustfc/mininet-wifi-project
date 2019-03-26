import GF
import numpy as np

w = 4
total = 2 ** w

gf = GF.GF(w)


def vector_mul(a, b):
    res = 0
    for i in range(len(a)):
        res = gf.add(res, gf.mul(a[i], b[i]))
    return res


def encode(packet):
    size = len(packet)
    k = 0
    while k != size:
        coefficients_matrix = np.random.randint(1, 2 ** w - 1, size=[size, size])
        k = np.linalg.matrix_rank(coefficients_matrix)
    encode_matrix = []
    for i in range(size):
        encode_matrix.append(vector_mul(coefficients_matrix[i], packet))
    return coefficients_matrix, encode_matrix



