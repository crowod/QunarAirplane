import ctypes

def rshift(val, n):
    return (val % 0x100000000) >> n


def lshift(val, n):
    return ctypes.c_int(val << n).value


def ctypes_cov(number):
    return ctypes.c_int(number).value