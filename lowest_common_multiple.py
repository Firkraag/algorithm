from gcd import gcd


def lcm(num1: int, num2: int):
    return num1 * num2 // gcd(num1, num2)
