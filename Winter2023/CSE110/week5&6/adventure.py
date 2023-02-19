weapon=input('You enter a dark tunnel, with your torch in hand. On the ground, you find two weapons on the ground, a SWORD and an AXE! Which do you choose? ')
if weapon.lower() == "sword":
    print('You pick up the sword and continue on into the tunnel.')
    swordPath=input('As you progress further into the cave, you come across a fork in the road. The path on the LEFT is covered in vines, while the one on the RIGHT is blocked by a rock. Which path do you take? ')
    if swordPath.lower() == "left":
        print('With your sword, you cut down the vines and advance deeper into the tunnel.')
        batAttack=input('At long last, you find the treasure! However, before you are able to grab it, you are attacked by a swarm of bats! Do you RUN from them, FIGHT them, or HIDE? ')
        if batAttack.lower() == "run":
            print('You try to run from them, but they catch up and overwhelm you! You wake up in a hospital bed a week later.')
        elif batAttack.lower() == "fight":
            print('Using your sword, you fight the bats and kill a few, causing the rest to retreat! The treasure is yours!')
        elif batAttack.lower() == "hide":
            print('You quickly find a hiding spot behind a rock. The bats are not able to find you and eventually give up. With them out of the way, you go ahead and get the treasure!')
        else:
            print('The bats eventually overwhelm you and knock you out.')
    elif swordPath.lower() == "right":
        print('Unfortunately, you were not able to move or break the rock. Perhaps the other path might have been better?')
    else:
        print('You choose neither path and instead decide to head home.')    
elif weapon.lower() == "axe":
    print('You pick up the axe and continue on into the tunnel.')
    axePath=input('As you progress further into the cave, you come across a fork in the road. The path on the LEFT is covered in vines, while the one on the RIGHT is blocked by a rock. Which path do you take? ')
    if axePath.lower() == "left":
        print('Your axe is too unwieldy to cut down the vines. Perhaps the other path might have been better?')
    elif axePath.lower() == "right":
        print('With your mighty axe, you crush the rock! You advance deeper into the tunnel.')
        giantAttack=input('Eventually, you come across a slumbering giant guarding the treasure! Do you RUN from it, FIGHT it, or HIDE? ')
        if giantAttack.lower() == "run":
            print('You decide you are no match for the giant! You run out of the tunnel, disappointed that you did not get the treasure, but happy to still be alive.')
        elif giantAttack.lower() == "fight":
            print('You chuck your axe right at his face, knocking him out! Quickly, you grab the treasure and get out of there! ')
        elif giantAttack.lower() == "hide":
            print('You find a hiding spot, waiting patiently until you find an opportunity to sneak around and grab the treasure!')
        else:
            print('The giant wakes up and knocks you out! You wake up in a hospital bed a week later.')
    else:
        print('You choose neither path and instead decide to head home.')
else:
    print('You probably should pick up one of the two weapons.')