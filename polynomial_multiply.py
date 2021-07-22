import math
import fft


def polynominal_multiply(a, b, precision=0):
    a_len = len(a)
    b_len = len(b)
    length = int(2 ** (1 + math.ceil(math.log(max(a_len, b_len)))))
    print(length)
    extend_a = [0] * length
    extend_b = [0] * length
    for i in range(a_len):
        extend_a[i] = a[i]
    for i in range(a_len, length):
        extend_a[i] = 0
    for i in range(b_len):
        extend_b[i] = b[i]
    for i in range(b_len, length):
        extend_b[i] = 0
    a_fft = fft.recursive_fft(extend_a)
    b_fft = fft.recursive_fft(extend_b)
    m_fft = [a_fft[i] * b_fft[i] for i in range(len(a_fft))]
    ab = fft.recursive_inverse_fft(m_fft)
    return [round(ab[i].real, precision) for i in range(a_len + b_len - 1)]
