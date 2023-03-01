dog = ''
print('Dog simulator')
while dog != '2':
    action=input('Do you want to 1- Bark or 2- Exit?')
    if dog == '1':
        print('Bark!')
    elif dog == '2':
        print('Goodbye!')
    else:
        print('Bark?')