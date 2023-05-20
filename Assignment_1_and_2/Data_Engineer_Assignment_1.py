# Assignment - 1: Understanding Decorators in Python

import time
from functools import wraps

def integers_Sum(integers):
    return sum(integers)

def time_logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Time taken to run {func.__name__}: {end_time - start_time} seconds")
        return result
    return wrapper

def result_cacher(func):
    cache = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

@time_logger
def timed_sum_integers(integers):
    return integers_Sum(integers)

@result_cacher
def cached_sum_integers(integers):
    return integers_Sum(integers)

# Demonstrating the use of decorators
integers = [1, 2, 3, 4, 5]
print(timed_sum_integers(integers))
print(cached_sum_integers(integers))
