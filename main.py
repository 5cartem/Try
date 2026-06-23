

print('Please enter your 5 digit password ')
password = input('>')

while len(password) != 5:
    print('Please enter 5 digit password')
    print('The password needs 5 digits')
    password = input('>')



a = 0

while str(a) != password:
    print(a)
    a += 1

print("\033[32mFound:\033[0m", a)





    
