import ctypes
import time

lenear_congruential_lib = ctypes.CDLL('./libLinearCongruential.so')

lenear_congruential_lib.initialize.argtypes = (ctypes.c_int, ctypes.c_int, ctypes.c_int, ctypes.c_int)
lenear_congruential_lib.initialize.restype = None

lenear_congruential_lib.getNumber.argtypes = None
lenear_congruential_lib.getNumber.restype = ctypes.c_uint

lenear_congruential_lib.getNumberInRange.argtypes = [ctypes.c_int, ctypes.c_int]
lenear_congruential_lib.getNumberInRange.restype = ctypes.c_uint

lenear_congruential_lib.getUD01.argtypes = None
lenear_congruential_lib.getUD01.restype = ctypes.c_double

def initialize(seed=None, a=1664525, c=1013904223, m=4294967296):
    if seed is None:
        seed = 42
    lenear_congruential_lib.initialize(seed, a, c, m)

initialize()

def random(min, max) -> int:
    return lenear_congruential_lib.getNumberInRange(min, max)

def random_list(min, max, length) -> list:
    return [lenear_congruential_lib.getNumberInRange(min, max) for _ in range(length)]

def random01() -> float:
    return lenear_congruential_lib.getUD01()

def random01_list(length) -> list:
    return [lenear_congruential_lib.getUD01() for _ in range(length)]
