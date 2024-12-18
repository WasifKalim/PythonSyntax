year = 2024

# if year % 4 == 0:
#     if(year % 100 == 0):
#         if year % 400 == 0:
#             print("Leap year")
#         else:
#             print("Not a Leap Year")
#     else:
#         print("Leap Year")

        
if (year % 400 == 0) or (year % 4 and year % 100 != 0):
    print(year, "is a Leap year")
else:
    print(year, "is not a Leap Year")
