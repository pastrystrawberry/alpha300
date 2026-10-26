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

name ="beau"
print(isinstance(name,str))

age = float(2)

print(isinstance(age,float))
number ="biplav"
ag= int(number)
print(isinstance(ag,int))

#arithemetic operators
1+1 #2
2-1#1
2*2 #4
4/2 #2
4%3 #1
4**2#16
5//2#2

boolean operators
 condition1=True
 condition2=False
 not condition1 #False
 condition1 and condition2 # false
 condition1 or condition2 #True
  
print(0 or 1)# 1
print(False or 'hey')## "hey"
print('hi' or 'hello')##hi
print([] on False)##'[]'


is & in operator


ternary operator

def is_adult(age):
    if age>18:
        return True
    else:
        False

def is_adult_2(age):
    return True if age>18 else False

### strings


name="biplav"
phrase=name+"parthasarathi"

print("biplav".upper())#BIPLAV
print("BIPLAV".lower())#biplav
print("biplav parthasarathi".title())#Biplav Parthasarathi

functions

"biplav".islower()#true
"BIPLAV".isupper()#true
.isalpha()if string contains char and not empty
.alnum() chracter or digits
.isdecimal()
startswith()
endswith()
replace()
split()
.strip() to remove spaces
join()#append new letter
find()

'''
from enum import Enum

class State(Enum):
    INACTIVE=0
    ACTIVE=1
print(State.ACTIVE.value)#1
print(State['ACTIVE'])
print(State(1))