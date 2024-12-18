import math

def area(n):
    area_rad = round(math.pi*n*n, 3)
    circumference = round(2 * math.pi * n, 2)
    return area_rad, circumference

a, c = area(3)

print("Area:", a, "Circumference:", c)