import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
option=[rock,paper,scissors]
print(option[user_choice])
computer_choice = random.randint(0,2)
print(option[computer_choice])
if user_choice == computer_choice:
    print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
    print("Paper covers rock, you lose!")
elif user_choice == 0 and computer_choice == 2:
    print("Rock crushes scissors, you win!")
elif user_choice == 1 and computer_choice == 0:
    print("Paper covers rock, you win!")
elif user_choice == 1 and computer_choice == 2:
    print("Scissors cuts paper, you lose!")
elif user_choice == 2 and computer_choice == 0:
    print("Rock crushes scissors, you lose!")
elif user_choice == 2 and computer_choice == 1:
    print("Scissors cuts paper, you win!")
else:
    print("Invalid input")  # This line is unreachable, but I'll leave it here for
