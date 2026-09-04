# 모듈
# import datetime
# import random

# import func

# from func import *
# cal1()
# cal2()
# cal3()
# # 결과값은 1 2 3



# a = max(1,2,3)
# print(a)        # 결과값은 3


# import sys
# print(sys.builtin_module_names)

import math
print(dir(math))
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 
#  'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'cbrt', 'ceil', 'comb', 
#  'copysign', 'cos', 'cosh', 'degrees', 'dist', 'e', 'erf', 'erfc', 'exp', 'exp2', 
#  'expm1', 'fabs', 'factorial', 'floor', 'fma', 'fmod', 'frexp', 'fsum', 'gamma', 
#  'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'isqrt', 'lcm', 
#  'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'nextafter', 
#  'perm', 'pi', 'pow', 'prod', 'radians', 'remainder', 'sin', 'sinh', 'sqrt', 
#  'sumprod', 'tan', 'tanh', 'tau', 'trunc', 'ulp']

print(math.log(10))             # 결과값은 2.302585092994046
print(math.sin(10))             # 결과값은 -0.5440211108893698
print(math.floor(10.921))       # 버림 / 결과값은 10
print(math.ceil(10.111))        # 올림 / 결과값은 11
print(round(10.542))            # 반올림 / 결과값은 11
print(round(10.542, 2))          # 반올림 / 결과값은 10.54
