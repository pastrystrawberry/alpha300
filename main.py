import random
'''
def choices():

    player_choice ="rock"
    computer_choice = "paper"

    return player_choice


def greeting():
    return "Hello"

response = greeting()
choices = choices()
print(choices)
print(response)

### dictonary 

def choices():

    player_choice =input("enter  a choice  rock paper sccissor")
    option=["rock","paper","scissors"]
    computer_choice = random.choice(option)
    choices = {"player":player_choice,"computer":computer_choice}
    return choices


food =["pizza","carrot","eggs"]
dinner = random.choice(food)


choics= choices()

print(choics)
'''

def get_choices():
    player_choice= input("enter a choice (rockk , paper, scissor) :")
    options=["rock","paper","scissors"]
    computer_choice= random.choice(options)
    choices={"player":player_choice,"computer":computer_choice}

    return choices


def check_win(player,computer):
    print(f"you chose {player} ,computer chose {computer}")
    if player==computer:
        return "it's a tie"
    elif player == "rock":
        if computer=="scissors":
            return "rock smashes scissors you win"
        else:
            return "paper covers rock you lose"
    elif player == "paper":
            if computer=="rock":
                return "paper covers rock you win"
            else:
                return "scisccors cut paper you lose"
    elif player == "scissors":
            if computer=="rock":
                return "rock smashes scissors you lose"
            else:
                return "scissors cut  paper you win"

choices = get_choices()
print(check_win(choices["player"],choices["computer"]))