
def var_sum(*args):
    print(args)
    for i in args:
        print(i * 2)
    return sum(args)

print(var_sum(2, 4, 3))
# print(var_sum(2, 4, 33, 5))
# print(var_sum(2, 4, 3, 5, 6, 1))