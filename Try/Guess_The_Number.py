import random

target=random.randint(1,100)

while True:
    userChoice=input("Guess the Number or Quit (type Quit)")
    if userChoice=="Quit":
        break
    UserChoice=int(userChoice)
    if(UserChoice==target):
        print("You Successfully Guessed")
        break
    elif UserChoice<target:
        print("Your no is too small Guess Bigg")
    else:
        print("Your no is too big think small")

print("Game OVER!!")