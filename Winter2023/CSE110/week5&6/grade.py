grade=int(input('Please enter your grade percentage: '))
if grade >= 90:
    letter = "A"
elif grade >= 80:
    letter = "B"
elif grade >= 70:
    letter = "C"
elif grade >= 60:
    letter = "D"
else:
    letter = "F"
print(f'Your grade is: {letter}')
if grade >= 70:
    print('You have passed the class! Congrats!')
else:
    print('Sorry, you did not pass the class. You can do better!')
