can_ride=False

age1=int(input("What is the age of the first rider? "))
height1=int(input("What is the height of the first rider? "))
second_rider=input("Is there a second rider (yes/no) ").lower()=="yes"
if height1<36:
    print("Sorry, you may not ride")
if age1<18 and second_rider=="no":
    print("Sorry, you may not ride.")
if second_rider:
    age2=int(input("What is the age of the second rider? "))
    height2=int(input("What is the height of the second rider? "))
    if age1<18 and age2<18:
        print("Sorry, you may not ride.")
    if height2<36:
        print("Sorry, the second rider may not ride.")
    else:
        print("Welcome to the ride. Please be safe and have fun!")
else:
    print("Welcome to the ride. Please be safe and have fun!")
