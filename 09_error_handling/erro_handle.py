file = open('youtube.txt', 'w')

# 1st flow - 
try:
    file.write('chai aur code')
finally:
    file.close()


# 2nd flow - it will close automatically
with open('youtube.txt','w') as file:
    file.write('Chai aur python')