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
    computer_choice = "paper"
    choices = {"player":player_choice,"computer":computer_choice}
    return choices
