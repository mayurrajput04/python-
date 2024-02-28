import time

def timer(func):
    def wrapper(*args):
        start = time.time()
        result = func(*args)
        end = time.time()
        print(f"{func.__name__} took {end-start} time to execute.")
        return result
    return wrapper

@timer
def example_fuction(n):
    time.sleep(n)

example_fuction(2)
