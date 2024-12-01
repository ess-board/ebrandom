import ctypes
import time

mersenne_twister = ctypes.CDLL('./libMersenneTwister.so')

mersenne_twister.initialize.argtypes = [ctypes.c_int]
mersenne_twister.initialize.restype = None

mersenne_twister.getNumber.argtypes = None
mersenne_twister.getNumber.restype = ctypes.c_uint

mersenne_twister.getNumberInRange.argtypes = [ctypes.c_int, ctypes.c_int]
mersenne_twister.getNumberInRange.restype = ctypes.c_uint

mersenne_twister.getUD01.argtypes = None
mersenne_twister.getUD01.restype = ctypes.c_double

def initialize(seed=None):
    if seed is None:
        seed = 42
    mersenne_twister.initialize(seed)

initialize()

def random(min, max) -> int:
    initialize()
    return mersenne_twister.getNumberInRange(min, max)

def random_list(min, max, length) -> list:
    initialize()
    return [mersenne_twister.getNumberInRange(min, max) for _ in range(length)]

def random01() -> float:
    initialize()
    return mersenne_twister.getUD01()

def random01_list(length) -> list:
    initialize()
    return [mersenne_twister.getUD01() for _ in range(length)]

