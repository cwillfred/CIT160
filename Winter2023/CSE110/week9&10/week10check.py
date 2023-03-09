# Ask the user for a list of items in a shopping list
shopping_list = []

list_item = input('Item: ')
while list_item.lower()!= 'quit':
    shopping_list.append(list_item)
    list_item = input('Item: ')

print('The shopping list is: ')
for list_item in shopping_list:
    print(list_item)

print('The shopping list with indexes is: ')
for index in range(len(shopping_list)):
    print(f'{index}, {shopping_list[index]}')

change_item_number = input('Which item would you like to change? ')
change_item = input('What is the new item? ')
shopping_list[change_item_number] = change_item

print('The shopping index with indexes is:')
for index in range(len(shopping_list)):
    print(f'{index}, {shopping_list[index]}')