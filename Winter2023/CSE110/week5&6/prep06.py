#Practice with boolean logic
x=10
y=10
if x==10 and y==10:
    print("True")
if x==20 or y==10:
    print("True")
if x==20 or y==20:
    print("True")
else:
    print("False")

#Practice with nested if statements
first_name = input("What is your first name?")
last_name = input("What is your last name?")
if first_name.lower() == 'carter' and last_name.lower() == 'frederickson':
    print("Hello, Carter Frederickson.")
    city = input("What city are you from?")
    if city.lower() == 'herndon':
        print("You are from Herndon, Virginia")
    else:
        print("Not the right city")
else:
    print("You are not Carter Frederickson")