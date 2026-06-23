

print('Please enter your 6 digit password ')
password = input('>')

while len(password) != 6:
    print('Please enter 6 digit password')
    print('The password needs 6 digits')
    password = input('>')



a = 0

while str(a) != password:
    print(a)
    a += 1

print("\033[32mFound:\033[0m", a)





    
