import ctypes
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
so_file_path = os.path.join(current_dir, 'libMidSquare.so')

mid_square_lib = ctypes.CDLL(so_file_path)

mid_square_lib.initialize.argtypes = [ctypes.c_int]
mid_square_lib.initialize.restype = None

mid_square_lib.getNumber.argtypes = None
mid_square_lib.getNumber.restype = ctypes.c_int

mid_square_lib.getNumberInRange.argtypes = [ctypes.c_int, ctypes.c_int]
mid_square_lib.getNumberInRange.restype = ctypes.c_int

mid_square_lib.getUD01.argtypes = None
mid_square_lib.getUD01.restype = ctypes.c_double

def initialize(seed=None):
    if seed is None:
        seed = 42
    mid_square_lib.initialize(seed)

initialize()

def random(min,max) -> int:
    return mid_square_lib.getNumberInRange(min,max)

def random_list(min,max,length) -> list:
    return [mid_square_lib.getNumberInRange(min,max) for _ in range(length)]

def random01() -> float:
    return mid_square_lib.getUD01()

def random01_list(length) -> list:
    return [mid_square_lib.getUD01() for _ in range(length)]