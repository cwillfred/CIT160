word = "bacon"
hint=""
for letter in word:
    hint += "_"
guess_count = 1

print('Welcome to the word guessing game!')
guess=input('What is your guess? ')

while guess.lower() != "bacon":
    print('Your guess was not correct.')
    print(f'Your hint is: {hint}')
    guess_count = guess_count + 1
    guess=input('What is your guess? ')

print('Congratulations, you guessed it!')
print(f'It took you {guess_count} guesses.')