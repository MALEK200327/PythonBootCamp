import random

logo = """
   _____                       _______ _            _   _                 _               
  / ____|                     |__   __| |          | \ | |               | |              
 | |  __ _   _  ___  ___ ___     | |  | |__   ___  |  \| |_   _ _ __ ___ | |__   ___ _ __ 
 | | |_ | | | |/ _ \/ __/ __|    | |  | '_ \ / _ \ | . ` | | | | '_ ` _ \| '_ \ / _ \ '__|
 | |__| | |_| |  __/\__ \__ \    | |  | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |   
  \_____|\__,_|\___||___/___/    |_|  |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|   
                                                                                          
                                                                                          
"""

print(logo)

win = False

def ChooseNumber():
    return random.randint(1,100)

NumberChoice=ChooseNumber()

def status(number):
    if number>NumberChoice:
        return "Too high"
    elif number<NumberChoice:
        return "Too low"
    else:
        return "You win!"
    
while not win:
    guess = int(input("Guess a number between 1 and 100: "))
    print(status(guess))
    if status(guess) == "You win!": 
        win = True
