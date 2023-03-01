numbers = []

new_number = ""
sum = 0

print("Enter a list of numbers, type 0 when finished.")

while new_number != 0:
    new_number = int(input('Enter number: '))
    if new_number != 0:
        numbers.append(new_number)
    else:
        for i in numbers:
            sum += i
            average = sum / len(numbers)

print(f'The sum is: {sum}')
print(f'The average is: {average}')