from time import time


# Performance Decorator
def performance(func):
    def wrapper(*args, **kwargs):
        start = time()
        result = func(*args, **kwargs)
        end = time()
        print(f'it took {end - start:.2f} seconds')
        return result

    return wrapper


@performance
def long_time():
    print('1')
    for i in range(1000000000):
        i * 5


@performance
def long_time2():
    print('2')
    for i in list(range(1000000000)):
        i * 5


long_time()
long_time2()
