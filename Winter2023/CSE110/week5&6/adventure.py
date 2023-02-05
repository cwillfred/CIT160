weapon=input('You enter a dark tunnel, with your torch in hand. On the ground, you find two weapons on the ground, a SWORD and an AXE! Which do you choose? ')
if weapon.lower() == "sword":
    print('You pick up the sword and continue on into the tunnel.')
elif weapon.lower() == "axe":
    print('You pick up the axe and continue on into the tunnel.')
else:
    print('You probably should pick up one of the two weapons.')