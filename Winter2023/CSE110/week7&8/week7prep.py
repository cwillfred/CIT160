number = -1

while number < 0:
    number = int(input('Please type a positive number: '))

print(f'The number is {number}')

whiny_kid = ""

while whiny_kid.lower() != 'yes':
    whiny_kid=input('May I have a candy? ')

print('Thank you.')