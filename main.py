rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    ____________
---'   _________)
          ______)
          ______)
         _______)
---.____________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)      
---.__(___)
'''
game_images = [rock, paper, scissors]

import random
user_choice = int(input("What do you want to choose? type 0 for rock, 1 for paper or 2 for scissors"))
print(game_images[user_choice])

computer_move = random.randint(0,2)
print("computer choose:")
print(game_images[computer_move])

if user_choice == 3 and user_choice ==0:
  print("you Win!!!!")
elif computer_move == 0 and user_choice ==2:
  print("You Lose XXX")
elif computer_move > user_choice:
  print("You Lose XXX")
elif user_choice > computer_move:
  print("You Win!!!!")
elif computer_move == user_choice:
  print("It's a draw!!")