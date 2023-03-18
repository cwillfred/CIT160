options = ['Add item', 'View cart', 'Remove cart', 'Compute total', 'Quit']
items = []
print("Welcome to the Shopping Cart Program!")
print("Please select one of the following:")
for i, choice in enumerate(options):
    print(f'{i+1}. {options[i]}')
while choice != 5:
    choice=int(input('Please enter an action: '))
    if choice == 1:
        item = input('What item would you like to add? ')
        items.append(item)
        print(f'{item} has been added to the cart.')
    elif choice == 2:
        print('The contents of your shopping cart are: ')
        for contents in items:
            print (items)
    elif choice == 5:
        print('Thank you. Goodbye.')
    else:
        print('Invalid option')