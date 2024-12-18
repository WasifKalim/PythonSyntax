# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# sum = 0
# i = 1

# for item in numbers:
#     for i in range(numbers[i]):
#         print(i)
#         if(item % 2 == 0 and item % i == 0):
#             sum += item

# print("Sum of ", sum)

n = 10
sum = 0

for i in range(1, n+1):
    if i%2 == 0:
        sum += 1

print("Count of even number is: , ", sum)