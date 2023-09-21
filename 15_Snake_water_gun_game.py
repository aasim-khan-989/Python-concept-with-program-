import random
a=input('enter snake(s),gun(g),water(w)\n')
computer=random.randint(1,3)
if computer==1:
    computer="s"
if computer==2:
    computer="w"
if computer==3:
    computer="g"
print(f"computer has entered {computer}")
def game(a,computer):
    if computer=="s":
        if a=="g":
            return "you win"
        if a=="w":
            return "you looss"
        else:
            return "tie"
    if computer=="w":
        if a=="s":
            return "you win"
        if a=="g":
            return "you loss"
        else:
            return "tie"
    if computer=="g":
        if a=="s":
            return "you loss"
        if a=="w":
            return "you win"
        else:
            return "tie"
print(game(a,computer))



