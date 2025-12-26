import time
from functools import wraps

def timeit(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f'⏱ {func.__name__} выполнена за {elapsed:.2f} сек')
        return result
    return wrapper
