fruits = ['apple', 'banana', 'cherry']
letter=input('Enter a letter: ')
for fruit in fruits:
    if letter in fruit:
        print(f'The fruit {fruit} contains the letter {letter}.')
    else:
        print(f'The fruit {fruit} does not contain the letter {letter}.')
