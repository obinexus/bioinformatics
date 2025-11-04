import ctypes, pathlib
clib = ctypes.CDLL(str(pathlib.Path(__file__).with_suffix('.so')))
clib.plp_cart2pol.argtypes = [ctypes.c_double]*2 + [ctypes.POINTER(ctypes.c_double*2)]
