import time

def cache(func):
    print("Calling decorator")
    cache_value = {}

    print("Cache: ", cache_value) # it calls only one time

    def wrapper(*args):
        # print("Cache_val: ", cache_value) # it is on every call 
        if args in cache_value:
            return cache_value[args]
        result = func(*args)
        cache_value[args] = result
        # print("Result", result)
        return result
    return wrapper

@cache
def long_running_function(a, b):
    time.sleep(4)
    return a + b

print(long_running_function(2, 4))
print(long_running_function(2, 4))
print(long_running_function(2, 3))