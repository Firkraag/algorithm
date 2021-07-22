def pow1(x, n: int):
    """
    compute x ^ n
    """
    if n == 0:
        return 1
    square = x * x
    if n % 2:
        return pow1(square, n // 2) * x
    return pow1(square, n // 2)


def pow2(x, n: int):
    """
    compute x ^ n
    """
    if n == 0:
        return 1
    tmp = pow2(x, n // 2)
    if n % 2:
        return tmp * tmp * x
    return tmp * tmp
