fruits = ['apples', 'bananas', 'cherries', 'grapes', 'lemons']
for i, fruit in enumerate(fruits):
    print(f'{i+1}. {fruits[i]}')
item_change = int(input('Which item would you like to update? '))-1
fruits[item_change] = 'tomato'
for i, fruit in enumerate(fruits):
    print(f'{i+1}. {fruits[i]}')
item_remove = int(input('Which item would you like to remove? '))-1
fruits.pop(item_remove)
for i, fruit in enumerate(fruits):
    print(f'{i+1}. {fruits[i]}')