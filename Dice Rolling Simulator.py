import random

while(True):
    try:
        RollStatus = int(input("Enter 0 to Exit\nEnter 1 To Roll Dice : "))
        DiceValue = random.randint(1, 6)

        if(RollStatus == 0):
            break
        else:
            print(f"Dice Value is {DiceValue}")
    except:
        print("Wrong Input")
    finally:
        print("--------------------")