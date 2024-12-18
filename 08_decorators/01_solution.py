import time

def timer(func):
    def wrapper(*args, **kwargs):
        # print("Hello Decorator") # decorator is runnnig every time here
        start = time.time()
        result = func(*args, **kwargs)
        # print("Result", result) # giving none
        end = time.time()
        print(f"{func.__name__} ran in {end-start} time")
        return result
    return wrapper

@timer
def example_function(n):
    print("fn")
    time.sleep(n)

example_function(1)
example_function(2)