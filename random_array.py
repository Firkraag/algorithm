import random


def random_arrays(array_num=100, array_size=100, array_lowerbound=0, array_upperbound=10000):
    for _ in range(array_num):
        yield [random.randint(array_lowerbound, array_upperbound) for _ in range(array_size)]
