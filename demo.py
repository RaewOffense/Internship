import random


def sessiorPaperRock():
    itemChoices = ["sessior","paper","rock"]
    choices =input("Enter choice:")
    random_choiceItem = random.choice(itemChoices)
    
    if(choices == "sesior" and random_choiceItem =="paper"):
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("You Won the game")
    elif(choices =="paper" and random_choiceItem =="sessior"):
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("You lose the game.")
    elif (choices == "rock" and random_choiceItem =="sessior"):
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("You Won the game")
    elif (choices == "sessior" and random_choiceItem =="rock"):
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("You lose the game")
    elif(choices =="paper" and random_choiceItem == "rock"):
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("You Won the game.")
    elif(choices == "rock" and random_choiceItem == "paper"):
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("You lose the game.")
    else:
        print(f'You:{choices} = computer:{random_choiceItem}')
        print("Draw Game")

sessiorPaperRock()
