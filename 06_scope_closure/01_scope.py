# username = "chaiaurcode"

# def func():
#     username = "chai"
#     print(username)

# print("User:",username)
# func()



x = 99
# def f1():
#     x = 88
#     def f2():
#         print(x)
#     return f2()

# myResult = f1()


# Closure --------------------- ******************
def chaicoder(num):
    print("Num:",num)
    def actual(x):
        print("X:",x)
        return x ** num
    return actual 

f = chaicoder(2) # 2 is num
g = chaicoder(3) # 3 is num

print("Final value of f:", f(4)) # 4 is x
print("Final value of g:", g(5)) # 5 is x

# def test(): 
#     pass

# if True:
#     pass
